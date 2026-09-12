from django import forms
from .models import Profile
from django.contrib.auth import get_user_model

class UserForm(forms.ModelForm):
    class Meta:
        model=get_user_model()
        fields=["first_name","last_name","email"]
        labels={
            "first_name":"Имя",
            "last_name":"Фамилия",
            "email" :"Электронная почта",

        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=["user"]
        labels={
            "telephone": "Номер телефона",
            "city": "Город",
            "address": "Адрес",
            "birth_day": "Дата рождения",
            "image": "Фото",
            "gender": "Пол"
        }