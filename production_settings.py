# Production Email Settings for Japan Surplus Shop
# Copy these settings to your settings.py file when you're ready to use Gmail SMTP

# Email settings for production (Gmail SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-gmail@gmail.com'  # Replace with your actual Gmail address
EMAIL_HOST_PASSWORD = 'your-app-password'  # Replace with your actual App Password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Alternative configuration using SSL (if TLS doesn't work)
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False

"""
To use these settings:

1. Generate an App Password for your Gmail account:
   - Go to https://myaccount.google.com/security
   - Enable 2-Step Verification if not already enabled
   - Go to App Passwords
   - Select "Mail" and "Other (Custom name)"
   - Enter "Japan Surplus Shop" as the name
   - Click "Generate" and copy the 16-character password

2. Replace the placeholders above with your actual Gmail address and App Password

3. Copy these settings to your settings.py file, replacing the existing email settings

4. Restart your Django server
""" 