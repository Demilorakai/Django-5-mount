from django.db import models
from django.contrib.auth.models import User

class ConfirmCode(models.Model):
    code = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
