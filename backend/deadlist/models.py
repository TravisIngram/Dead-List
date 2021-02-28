from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator

# Unused imports from webserver lab...
# from __future__ import unicode_literals
# from django.contrib.auth.models import User, Group
# from django.contrib import admin
# import base64

# User Model - Username, First Name, Last Name, Email Address, Role


class User(models.Model):
    MEMBER = 'member'
    ADMIN = 'admin'
    ROLE = [
        (MEMBER, 'member'),
        (ADMIN, 'admin'),
    ]
    role = models.CharField(
        max_length=6,
        choices=ROLE,
        default=MEMBER,
    )

    username = models.CharField(max_length=30, blank=False)
    firstName = models.CharField(max_length=30, blank=False)
    lastName = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)


# Deceased Model - Name, Date of Death, Biography, Link


class Deceased(models.Model):
    deceasedName = models.CharField(max_length=200, blank=False)
    biography = models.CharField(max_length=500, blank=False)
    link = models.URLField(max_length=300, blank=True,
                           validators=[URLValidator(schemes=['http', 'https'])])
    dateOfDeath = models.CharField(max_length=200, blank=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.deceasedName)

# Call Model - Title, Source, Comment, created, Rating, Caller (fk), Pun (fk)


class Call(models.Model):
    deceasedName = models.CharField(max_length=200, blank=False)
    dateOfDeath = models.CharField(
        max_length=200, blank=False, default='01/01/2000')
    source = models.URLField(max_length=300, blank=True,
                             validators=[URLValidator(schemes=['http', 'https'])])
    callRating = models.IntegerField(blank=True,
                                     validators=[MaxValueValidator(5), MinValueValidator(1)])
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

# Pun Model - Content, Timestamp, Rating, User (fk), Call (fk)


class Pun(models.Model):
    punContent = models.CharField(max_length=300, blank=False)
    punRating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    call = models.ForeignKey(Call, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)
