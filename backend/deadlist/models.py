from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
    email = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return str(self.username)

# Call Model - Title, Source, Comment, created, Rating, Caller (fk), Pun (fk)


class Call(models.Model):
    title = models.CharField(max_length=100, blank=False)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    caller = models.ForeignKey(User, on_delete=models.CASCADE)
    pun = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
