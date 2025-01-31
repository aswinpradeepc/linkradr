from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from .forms import SignUpForm, LoginForm, OTPVerificationForm
from django.contrib.auth import logout

User = get_user_model()

def login_view(request):
    """Handles user login."""
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if not user.is_verified:
                    return redirect("verification_required", email=email)  # ✅ Redirect to verification page
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()
    return render(request, "auth_login/login.html", {"form": form})

def send_verification_email(user, request):
    """Sends an email with an activation link and OTP."""
    user.generate_otp()  # ✅ Generate OTP before sending email
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    domain = get_current_site(request).domain
    link = f"http://{domain}/activate/{uid}/{token}/"

    subject = "Verify Your Account"
    message = f"""
    Hi {user.first_name},
    
    Click the link below to activate your account:
    {link}
    
    OR
    
    Use this OTP to verify: {user.otp_code}
    
    If you did not sign up, please ignore this email.
    """

    send_mail(subject, message, "noreply@example.com", [user.email])

def verification_required(request, email):
    """Page for unverified users to request a verification email."""
    return render(request, "auth_login/verification_required.html", {"email": email})

def resend_verification(request, email):
    """Resends a verification email when requested."""
    try:
        user = User.objects.get(email=email)
        if not user.is_verified:
            send_verification_email(user, request)
            return HttpResponse("A new verification email has been sent to your email address.")
    except User.DoesNotExist:
        return HttpResponse("Invalid request.")
    return redirect("login")


def signup(request):
    """Handles user registration."""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # ✅ Prevent login before verification
            user.username = user.email  # ✅ Ensure username is set to email
            user.save()
            send_verification_email(user, request)  # ✅ Send verification email
            return HttpResponse("Check your email for an activation link or OTP.")
    else:
        form = SignUpForm()
    return render(request, "auth_login/signup.html", {"form": form})

def activate(request, uidb64, token):
    """Verifies user via activation link."""
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return HttpResponse("Invalid activation link.")

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_verified = True
        user.otp_code = None  # ✅ Clear OTP after verification
        user.save()
        return HttpResponse("Account activated! You can now log in.")
    else:
        return HttpResponse("Activation link is invalid or expired.")

def verify_otp(request):
    """Verifies user via OTP."""
    if request.method == "POST":
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            otp = form.cleaned_data["otp"]
            try:
                user = User.objects.get(email=email, otp_code=otp)
                user.is_active = True
                user.is_verified = True
                user.otp_code = None  # ✅ Clear OTP after successful verification
                user.save()
                return HttpResponse("OTP verified! You can now log in.")
            except User.DoesNotExist:
                return HttpResponse("Invalid OTP or email.")
    else:
        form = OTPVerificationForm()
    return render(request, "auth_login/verify_otp.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect('home')