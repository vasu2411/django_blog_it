from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.email_id
    class Meta:
        verbose_name_plural = "Users"