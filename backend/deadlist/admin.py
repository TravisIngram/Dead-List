from django.contrib import admin
from .models import Call, Pun, Deceased, User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'firstName', 'lastName', 'email')


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    fields = ('username', 'deceasedName', 'source',
              'dateOfDeath', 'comment', 'callRating')


@admin.register(Deceased)
class DeceasedAdmin(admin.ModelAdmin):
    fields = ('username', 'deceasedName', 'link',
              'dateOfDeath', 'biography')


@admin.register(Pun)
class PunAdmin(admin.ModelAdmin):
    fields = ('username', 'punContent', 'punRating', 'call')

    # list_display = ['title', 'author', 'description']
