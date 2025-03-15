from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Form for user registration
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
    """
    Form for updating user profile
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 
                  'address', 'city', 'state', 'postal_code', 'country', 'profile_image')

class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile without password
    """
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 
                  'address', 'city', 'state', 'postal_code', 'country', 'profile_image')
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class OTPVerificationForm(forms.Form):
    """
    Form for OTP verification
    """
    otp = forms.CharField(
        label='Enter OTP',
        max_length=6,
        min_length=6,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:text-white sm:text-sm',
            'placeholder': 'Enter 6-digit OTP',
            'autocomplete': 'off'
        })
    )

    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        if not otp.isdigit():
            raise forms.ValidationError("OTP must contain only digits")
        return otp 