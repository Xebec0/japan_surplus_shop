from django.urls import path
from .views import SignUpView, ProfileUpdateView, profile_view, OTPVerificationView, ResendOTPView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('verify-otp/', OTPVerificationView.as_view(), name='verify_otp'),
    path('resend-otp/', ResendOTPView.as_view(), name='resend_otp'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
] 