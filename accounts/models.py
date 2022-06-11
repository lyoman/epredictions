from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    email           = models.EmailField(unique=True, null=True, blank=True)
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = models.CharField(max_length=17, null=True, blank=True) # validators should be a list
    location        = models.CharField(_("Name of the location where thay operate"), max_length=250, null=True, blank=True)
    place_name      = models.CharField(_("Name of the place where they operate"), max_length=250, null=True, blank=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp       = models.DateTimeField(auto_now=False, auto_now_add=True)


    def  __str__(self):
        return self.username
    
    class Meta:
        ordering = ["-timestamp", "-updated"]

    class Meta:
        app_label = 'accounts'
