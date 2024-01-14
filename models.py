from django.db import models
from django.contrib.auth.hashers import make_password

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(null=True, max_length=128)
    score = models.IntegerField(null=True)
    identifiant = models.CharField(null=True, max_length=255, unique=True)
  
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def save(self, *args, **kwargs):
        # Ensure that the password is hashed before saving to the database
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super(Member, self).save(*args, **kwargs)