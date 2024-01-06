from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# Create your models here.
class User(AbstractUser):
    """
    create user registration model using abstract user
    """
    mobile_number = models.CharField(max_length=20, blank=True, null=True)


    class Meta:
        ordering = ['id']



class UserSettings(models.Model):
    FIELD_CHOICES = [
        ('optional', 'Optional'),
        ('required', 'Required'),
        ('hidden', 'Hidden'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username_option = models.CharField(max_length=10, null=True, blank=True, choices=FIELD_CHOICES)
    email_option = models.CharField(max_length=10, null=True, blank=True, choices=FIELD_CHOICES)
    password_option = models.CharField(max_length=10, null=True, blank=True, choices=FIELD_CHOICES)
    password2_option = models.CharField(max_length=10, null=True, blank=True, choices=FIELD_CHOICES)
    first_name_option = models.CharField(max_length=10, null=True, blank=True, choices=FIELD_CHOICES)
    last_name_option = models.CharField(max_length=10, null=True, blank=True, choices=FIELD_CHOICES)
    mobile_number_option = models.CharField(max_length=10,null=True, blank=True, choices=FIELD_CHOICES)