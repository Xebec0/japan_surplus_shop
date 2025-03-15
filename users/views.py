from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.conf import settings
from .forms import CustomUserCreationForm, ProfileUpdateForm, OTPVerificationForm
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.views import View
from .models import CustomUser
from .utils import send_otp_email, is_otp_valid

# Create your views here.

class SignUpView(CreateView):
    """
    View for user registration
    """
    form_class = CustomUserCreationForm
    template_name = 'users/signup.html'
    
    def form_valid(self, form):
        # Save the user but don't log them in yet
        user = form.save(commit=False)
        user.is_active = False  # Deactivate user until email is verified
        user.save()
        
        # Send OTP to user's email
        send_otp_email(user)
        
        # Store user_id in session for verification
        self.request.session['user_id_to_verify'] = user.id
        
        # Redirect to OTP verification page
        return redirect(reverse('users:verify_otp'))

class OTPVerificationView(FormView):
    """
    View for OTP verification
    """
    form_class = OTPVerificationForm
    template_name = 'users/verify_otp.html'
    success_url = reverse_lazy('account_login')
    
    def dispatch(self, request, *args, **kwargs):
        # Check if there's a user to verify
        if 'user_id_to_verify' not in request.session:
            messages.error(request, 'No verification in progress. Please sign up first.')
            return redirect('users:signup')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user_id = self.request.session['user_id_to_verify']
        user = get_object_or_404(CustomUser, id=user_id)
        
        # Verify OTP
        submitted_otp = form.cleaned_data['otp']
        
        if not is_otp_valid(user):
            messages.error(self.request, 'OTP has expired. Please request a new one.')
            return self.form_invalid(form)
        
        if user.otp != submitted_otp:
            messages.error(self.request, 'Invalid OTP. Please try again.')
            return self.form_invalid(form)
        
        # OTP is valid, activate user
        user.is_active = True
        user.email_verified = True
        user.save()
        
        # Clear session
        if 'user_id_to_verify' in self.request.session:
            del self.request.session['user_id_to_verify']
        
        messages.success(self.request, 'Email verified successfully. You can now log in.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.session.get('user_id_to_verify')
        if user_id:
            user = get_object_or_404(CustomUser, id=user_id)
            context['email'] = user.email
            
            # In development mode, display the OTP for testing
            if settings.DEBUG:
                context['debug_otp'] = user.otp
                
        return context

class ResendOTPView(View):
    """
    View for resending OTP
    """
    def get(self, request, *args, **kwargs):
        if 'user_id_to_verify' not in request.session:
            messages.error(request, 'No verification in progress. Please sign up first.')
            return redirect('users:signup')
        
        user_id = request.session['user_id_to_verify']
        user = get_object_or_404(CustomUser, id=user_id)
        
        # Send new OTP
        send_otp_email(user)
        
        messages.success(request, 'A new OTP has been sent to your email.')
        return redirect('users:verify_otp')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating user profile
    """
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    
    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated successfully.')
        return super().form_valid(form)

@login_required
def profile_view(request):
    """
    View for displaying user profile
    """
    return render(request, 'users/profile_detail.html', {'user': request.user})
