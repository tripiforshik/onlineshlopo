from django import forms
from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "Электронная почта",
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]
        labels = {
            "telephone": "Номер телефона",
            "city": "Город",
            "address": "Адрес",
            "birth_day": "Дата рождения",
            "image": "Фото",
            "gender": "Пол"
        }
        widgets = {
            'birth_day': forms.widgets.DateInput(attrs={'type': 'date'}),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label=("Электронная почта"),
        widget=forms.EmailInput(attrs={'placeholder':'Введите действующий email адрес'})
    )
    password1 = forms.CharField(
        label=("Пароль"),
        widget=forms.PasswordInput(attrs={'placeholder':'Пароль не менее 8 символов с буквами, цифрами и знаками'})
    )
    password2 = forms.CharField(
        label=("Подтверждение пароля"),
        widget=forms.PasswordInput(attrs={'placeholder':'Повторите тот же пароль для подтверждения'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            "username": "Имя пользователя",
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'Имя должно содержать только цифры, буквы и @/./+/-/_'}),
        }
        help_texts = {
            'username': (''),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        User = get_user_model()
        values = User.objects.filter(email=email)
        if values:
            raise forms.ValidationError("Этот email уже зарегистрирован.", code="email_taken")
        return email