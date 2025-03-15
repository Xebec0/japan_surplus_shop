# OTP Verification System for Japan Surplus Shop

This document provides instructions on how to set up and use the OTP (One-Time Password) verification system for the Japan Surplus Shop project.

## Overview

The OTP verification system enhances security by requiring email verification before account activation. When a user signs up, an OTP is sent to their email address. The user must enter this OTP to verify their email and activate their account.

## Setup Instructions

### 1. Environment Configuration

1. Create a `.env` file in the root directory of the project with the following content:
   ```
   EMAIL_HOST_USER=your-gmail-username@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   ```

2. Replace `your-gmail-username@gmail.com` with your actual Gmail address and `your-app-password` with your Gmail App Password.

3. The system will automatically detect if these environment variables are set:
   - If both variables are set, it will use Gmail SMTP for sending emails (production mode)
   - If either variable is missing or set to default values, it will use the console backend for sending emails (development mode)

### 2. Gmail App Password Setup

To generate an App Password for Gmail:

1. Go to your Google Account settings: https://myaccount.google.com/
2. Select "Security" from the left menu
3. Under "Signing in to Google," select "2-Step Verification" (enable it if not already enabled)
4. Scroll down and select "App passwords"
5. Select "Mail" as the app and "Other (Custom name)" as the device
6. Enter "Japan Surplus Shop" as the name
7. Click "Generate" and copy the 16-character password
8. Paste the password in your `.env` file (without spaces)

### 3. Testing Email Configuration

1. Run the test script to verify that your email configuration is working correctly:
   ```
   python test_email.py
   ```

2. The script will check if your environment variables are set correctly and provide detailed error messages if there are any issues.

3. Enter your email address when prompted to receive a test email.

4. Check your email inbox for the test email. If you don't receive it, check your spam folder.

## Development vs. Production

### Development Mode

In development mode, the system will:
- Use the console backend for sending emails (emails will be printed to the console)
- Display the OTP on the verification page for testing purposes
- Log the OTP to the console

To enable development mode, either:
- Don't create a `.env` file, or
- Set `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` to their default values in the `.env` file

### Production Mode

In production mode, the system will:
- Use Gmail SMTP for sending emails
- Not display the OTP on the verification page
- Send the OTP to the user's email address

To enable production mode:
- Create a `.env` file with your actual Gmail credentials
- Make sure both `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` are set correctly

## OTP Verification Flow

1. User signs up with their email address and other required information.
2. An OTP is generated and sent to the user's email address.
3. User is redirected to the OTP verification page.
4. User enters the OTP received in their email.
5. If the OTP is valid, the user's account is activated and they can log in.
6. If the OTP is invalid or expired, the user can request a new OTP.

## Troubleshooting

### OTP Email Not Received

1. Check your spam folder.
2. Verify that your email configuration is correct in the `.env` file.
3. Run the test script to verify that your email configuration is working correctly.
4. Check the console output for any error messages.
5. Make sure you're using an App Password, not your regular Gmail password.
6. Check for typos in your email address.
7. Make sure 2-Step Verification is enabled for your Google account.

### Invalid OTP Error

1. Make sure you are entering the correct OTP.
2. OTPs expire after 10 minutes. If your OTP has expired, request a new one.
3. If you're still having issues, try signing up again with a different email address.

### Common Gmail SMTP Errors

1. **"Username and Password not accepted"**:
   - Make sure you're using an App Password, not your regular Gmail password.
   - Check for typos in your email address.
   - Try generating a new App Password.

2. **"SMTP connection failed"**:
   - Check your internet connection.
   - Make sure your firewall is not blocking the SMTP connection.
   - Try using a different port (465 instead of 587) and set `EMAIL_USE_SSL = True` instead of `EMAIL_USE_TLS = True`.

## Security Considerations

1. OTPs expire after 10 minutes for security reasons.
2. OTPs are stored securely in the database.
3. Email verification is required before account activation.
4. App Passwords are used for Gmail authentication to enhance security.
5. Environment variables are used to store sensitive credentials.

## Additional Resources

- [Django Documentation on Email](https://docs.djangoproject.com/en/4.2/topics/email/)
- [Google App Passwords](https://support.google.com/accounts/answer/185833)
- [Django AllAuth Documentation](https://django-allauth.readthedocs.io/en/latest/) 