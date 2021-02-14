from rest_framework import serializers
from deadlist.models import User, Pun, Call, Deceased


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'role',
                  'createdAt', 'updatedAt')


class PunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pun
        fields = ('content', 'punRating', 'username',
                  'createdAt', 'updatedAt')


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('title', 'callRating', 'username', 'pun',
                  'comment', 'createdAt', 'updatedAt')


class DeceasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deceased
        fields = ('deceasedName', 'username', 'biography', 'link',
                  'dateOfDeath', 'createdAt', 'updatedAt')
