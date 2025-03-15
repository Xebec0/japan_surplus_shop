import os
import django
import sys

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'japan_surplus_shop.settings')
django.setup()

from users.models import CustomUser
from users.utils import send_otp_email

def test_otp_generation():
    """
    Test OTP generation and email sending
    """
    print("\n===== OTP Verification Test =====\n")
    
    # Get a test user or create one if it doesn't exist
    email = input("Enter an email address to test OTP verification: ")
    
    try:
        user = CustomUser.objects.get(email=email)
        print(f"Using existing user: {user.username} ({user.email})")
    except CustomUser.DoesNotExist:
        username = email.split('@')[0]
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password='testpassword123',
            is_active=False
        )
        print(f"Created new test user: {user.username} ({user.email})")
    
    # Generate and send OTP
    print("\nGenerating and sending OTP...")
    send_otp_email(user)
    
    print("\nTest completed! Check the console output above for the OTP details.")
    print("In a real scenario, the OTP would be sent to the user's email.")
    print("\nYou can now test the OTP verification by:")
    print("1. Going to http://127.0.0.1:8000/users/verify-otp/")
    print("2. Entering the OTP shown above")
    print("3. Checking that the user's account is activated\n")

if __name__ == "__main__":
    test_otp_generation() 