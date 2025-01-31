from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("verify-otp/", verify_otp, name="verify_otp"),
    path("verification-required/<email>/", verification_required, name="verification_required"),  # ✅ New page
    path("resend-verification/<email>/", resend_verification, name="resend_verification"),  # ✅ Resend email
]
