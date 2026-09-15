from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    class Gender(models.TextChoices):
        UNSPEC = ("unspec", "не указан")
        MALE = ("male", "мужской")
        FEMALE = ("female", "женский")

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=150, blank=True)
    birth_day = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=12, choices=Gender, default=Gender.UNSPEC)
    image=models.ImageField(blank=True,upload_to='accounts')

    def __str__(self):

        return f'{self.user.username},{self.telephone}'