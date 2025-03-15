import os
import django
import sys

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'japan_surplus_shop.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

def test_email_configuration():
    """
    Test the email configuration by sending a test email
    """
    print("\n===== Email Configuration Test =====\n")
    
    # Check if environment variables are set
    email_user = settings.EMAIL_HOST_USER
    email_password = settings.EMAIL_HOST_PASSWORD
    
    if not email_user or email_user == 'your-gmail-username@gmail.com':
        print("ERROR: EMAIL_HOST_USER is not set correctly in your .env file.")
        print("Please update your .env file with your actual Gmail address.")
        return
    
    if not email_password or email_password == 'your-app-password':
        print("ERROR: EMAIL_HOST_PASSWORD is not set correctly in your .env file.")
        print("Please update your .env file with your actual Gmail App Password.")
        return
    
    subject = 'Test Email from Japan Surplus Shop'
    message = '''
    Hello,
    
    This is a test email to verify that the email configuration is working correctly.
    
    Best regards,
    Japan Surplus Shop Team
    '''
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [input("Enter your email address to receive the test email: ")]
    
    print(f"\nSending test email to {recipient_list[0]}...")
    print(f"From: {from_email}")
    
    try:
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
        print("\n✅ Test email sent successfully!")
        print("\nEmail Configuration Details:")
        print(f"- Email backend: {settings.EMAIL_BACKEND}")
        print(f"- Email host: {settings.EMAIL_HOST}")
        print(f"- Email port: {settings.EMAIL_PORT}")
        print(f"- Email user: {settings.EMAIL_HOST_USER}")
        print(f"- TLS enabled: {settings.EMAIL_USE_TLS}")
        print("\nPlease check your inbox (and spam folder) for the test email.")
    except Exception as e:
        print(f"\n❌ Error sending test email: {e}")
        print("\nTroubleshooting steps:")
        print("1. Check your .env file and make sure your Gmail credentials are correct.")
        print("2. Make sure you're using an App Password, not your regular Gmail password.")
        print("3. Check for typos in your email address.")
        print("4. Make sure 2-Step Verification is enabled for your Google account.")
        print("5. Try generating a new App Password.")
        print("\nFor more information, see OTP_VERIFICATION_README.md")

if __name__ == "__main__":
    test_email_configuration() 