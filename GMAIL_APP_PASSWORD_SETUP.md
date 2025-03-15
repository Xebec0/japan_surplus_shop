# Setting Up Gmail App Password for Japan Surplus Shop

This guide will walk you through the process of setting up a Gmail App Password for use with the Japan Surplus Shop OTP verification system.

## Prerequisites

1. A Gmail account (you're using `helloharith9@gmail.com`)
2. 2-Step Verification enabled on your Google account

## Step 1: Enable 2-Step Verification (if not already enabled)

1. Go to your Google Account: https://myaccount.google.com/
2. Click on "Security" in the left sidebar
3. Scroll down to "Signing in to Google"
4. Click on "2-Step Verification"
5. Follow the prompts to enable 2-Step Verification
6. You may need to verify your identity with a code sent to your phone

## Step 2: Generate an App Password

1. Go to your Google Account: https://myaccount.google.com/
2. Click on "Security" in the left sidebar
3. Scroll down to "Signing in to Google"
4. Click on "App passwords" (this option only appears if 2-Step Verification is enabled)
5. You may need to sign in again to verify your identity
6. At the bottom, select "Select app" and choose "Mail"
7. Select "Other (Custom name)" from the "Select device" dropdown
8. Enter "Japan Surplus Shop" as the name
9. Click "Generate"
10. Google will display a 16-character password (without spaces)
11. **Copy this password immediately** - you won't be able to see it again!

## Step 3: Update Your .env File

1. Open the `.env` file in your project directory
2. Find the line that says `EMAIL_HOST_PASSWORD=your-app-password-here`
3. Replace `your-app-password-here` with the 16-character App Password you just generated
4. Save the file

Example:
```
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```

## Step 4: Update Your settings.py File

1. Open the `japan_surplus_shop/settings.py` file
2. Find the commented-out email settings section
3. Uncomment the code by removing the triple quotes (`"""`) at the beginning and end of the section
4. Save the file

## Step 5: Test Your Configuration

1. Restart your Django development server
2. Go to the signup page and create a new account
3. Check your email for the OTP
4. Enter the OTP to verify your account

## Troubleshooting

If you're still seeing authentication errors:

1. **Double-check your App Password**: Make sure you've copied it correctly without any spaces
2. **Check your Gmail address**: Ensure it's spelled correctly in the `.env` file
3. **Check for less secure app access**: This shouldn't be an issue with App Passwords, but make sure your Google account doesn't have any security restrictions that might block the connection
4. **Try a different port**: If port 587 doesn't work, you can try port 465 with SSL instead of TLS:
   ```
   EMAIL_PORT=465
   EMAIL_USE_SSL=True
   EMAIL_USE_TLS=False
   ```
5. **Check your internet connection**: Make sure your computer can connect to Gmail's SMTP servers
6. **Check firewall settings**: Make sure your firewall isn't blocking outgoing connections to Gmail's SMTP servers

## Security Considerations

- App Passwords provide a way for less secure apps to access your Google account without compromising your main password
- Each App Password is specific to a single application
- You can revoke App Passwords at any time from your Google Account security settings
- Never share your App Password with anyone
- In a production environment, you should use environment variables or a secure secrets management system to store your App Password, not a `.env` file 