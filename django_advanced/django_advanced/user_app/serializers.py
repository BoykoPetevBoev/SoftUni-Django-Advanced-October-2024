from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email', 'password']

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            **validated_data
        )
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password', None)
        return representation