from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    pass

class Analyst(CustomUser):
    pass

    class Meta:
        verbose_name = "Analyst"