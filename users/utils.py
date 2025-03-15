from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
import html
import random
import string

def send_otp_email(user):
    """
    Send OTP verification email to the user
    """
    subject = 'Japan Surplus Shop - Email Verification OTP'
    otp = user.generate_otp()
    user.otp = otp
    user.otp_created_at = timezone.now()
    user.save()
    
    # Create a more visually appealing email message
    message = f"""
Hello {html.escape(user.username)},

Thank you for registering with Japan Surplus Shop!

Your email verification OTP is: {otp}

This OTP is valid for 10 minutes.

Please enter this OTP on the verification page to complete your registration.

If you did not request this, please ignore this email.

Best regards,
Japan Surplus Shop Team
    """
    
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    
    # Send the email
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    
    # Log the OTP to console in development mode with clear visibility
    if settings.DEBUG:
        print("\n" + "="*80)
        print(f"📧 EMAIL SENT TO: {user.email}")
        print(f"📋 SUBJECT: {subject}")
        print("="*80)
        print(message)
        print("="*80)
        print(f"🔑 OTP CODE: {otp}")
        print("="*80 + "\n")
    
    return otp

def is_otp_valid(user):
    """
    Check if the OTP is still valid (not expired)
    """
    if not user.otp_created_at:
        return False
    
    # OTP is valid for 10 minutes
    expiry_time = user.otp_created_at + timedelta(minutes=10)
    return timezone.now() <= expiry_time 