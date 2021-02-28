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
        fields = ('punContent', 'punRating', 'username', 'call',
                  'createdAt', 'updatedAt')


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = ('deceasedName', 'callRating', 'username', 'source',
                  'comment', 'dateOfDeath', 'createdAt', 'updatedAt')


class DeceasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deceased
        fields = ('deceasedName', 'username', 'biography', 'link',
                  'dateOfDeath', 'createdAt', 'updatedAt')
