from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class UserSerializer(UserCreateSerializer):
    """
    Custom serializer for User model that extends UserCreateSerializer.
    """

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            'id',
            'email',
            'username',
            'is_active',
            'is_staff',
        ]
