from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import EmailField, ChoiceField
from .validators import RegisteredEmailValidator
from .models import User, Profile


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'username', 'is_model', 'is_photographer', 'is_men', 'is_women')


class LoginForm(AuthenticationForm):
    username = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))


class VerificationEmailForm(forms.Form):
    email = EmailField(widget=forms.EmailInput(attrs={'autofocus': True}), validators=(EmailField.default_validators + [RegisteredEmailValidator()]))
     # 유효성 검증 필터를 추가해 이미 인증 되거나 가입된 적이 없는 이메일이 입력될 경우 에러 발생.

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name',]


class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False) # 선택적으로 입력할 수 있음.
    class Meta:
        model = Profile
        fields = ['profile_photo', 'height', 'weight',]