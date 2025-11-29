from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Rozszerzony model użytkownika dla studentów.
    """
    phone = models.CharField('Telefon', max_length=15, blank=True)
    university = models.CharField('Uczelnia', max_length=100, blank=True)
    bio = models.TextField('O mnie', blank=True)
    avatar = models.ImageField('Zdjęcie profilowe', upload_to='avatars/', blank=True, null=True)
    created_at = models.DateTimeField('Data rejestracji', auto_now_add=True)
    updated_at = models.DateTimeField('Ostatnia aktualizacja', auto_now=True)

    class Meta:
        verbose_name = 'Użytkownik'
        verbose_name_plural = 'Użytkownicy'

    def __str__(self):
        return self.username

    def get_full_name_or_username(self):
        """Zwraca pełne imię i nazwisko lub username."""
        full_name = self.get_full_name()
        return full_name if full_name else self.username
