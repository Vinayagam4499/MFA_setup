import io
import base64
import pyotp
import qrcode
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TwoFactorAuth

@login_required
def home(request):
    # Ensure the user has passed 2FA before showing the home page
    if not request.session.get('is_2fa_authenticated'):
        return redirect('verify_2fa')
    return render(request, 'twofa_app/home.html')

@login_required
def setup_2fa(request):
    # Get or create the 2FA record for the user
    twofa, created = TwoFactorAuth.objects.get_or_create(user=request.user)
    totp = pyotp.TOTP(twofa.otp_secret)
    
    # Generate the provisioning URI for the authenticator app
    provisioning_uri = totp.provisioning_uri(name=request.user.email, issuer_name="MySite")
    
    # Generate a QR code image from the provisioning URI
    qr_img = qrcode.make(provisioning_uri)
    buffered = io.BytesIO()
    qr_img.save(buffered, format="PNG")
    qr_code_data = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    context = {
        "qr_code": qr_code_data,
        "otp_secret": twofa.otp_secret,
    }
    return render(request, 'twofa_app/setup_2fa.html', context)

@login_required
def verify_2fa(request):
    if request.method == "POST":
        token = request.POST.get("token")
        try:
            twofa = TwoFactorAuth.objects.get(user=request.user)
        except TwoFactorAuth.DoesNotExist:
            messages.error(request, "2FA is not set up for your account.")
            return redirect('setup_2fa')
        totp = pyotp.TOTP(twofa.otp_secret)
        if totp.verify(token):
            # Mark the session as 2FA authenticated
            request.session['is_2fa_authenticated'] = True
            messages.success(request, "Two-factor authentication successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid token. Please try again.")
            return redirect('verify_2fa')
    return render(request, 'twofa_app/verify_2fa.html')


def profile(request):
    return render(request, 'profile.html')