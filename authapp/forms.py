from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    
    password1 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput,
    help_text="Password must be at least 8 characters long and secure."
    )    
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data['full_name']
        first_name, last_name = full_name.split(" ", 1) if " " in full_name else (full_name, "")
        user.first_name = first_name
        user.last_name = last_name
        user.username = user.email  # ✅ Set username as email
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")  # ✅ Override username to use email

class OTPVerificationForm(forms.Form):
    # email = forms.EmailField()
    otp = forms.CharField(max_length=6)
