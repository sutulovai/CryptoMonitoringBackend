from django.db import models


class ApplicationUser(models.Model):
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=40)
    date_register = models.DateTimeField(null=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, auto_now=True)


class FavoriteCurrency(models.Model):
    currency_id = models.CharField(max_length=100)
    application_user = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)
