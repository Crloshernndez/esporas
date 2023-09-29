from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Create a custom UserCreationForm class that inherits from UserCreationForm
    """
    class Meta(UserCreationForm):
        # Associate this form with the User model
        model = User

        # Specify the fields to include in the form (email and username)
        fields = ["email", "username"]

        # Define a custom CSS class for displaying errors (usually an error message)
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    """
    Create a custom UserChangeForm class that inherits from UserChangeForm
    """
    class Meta:
        # Associate this form with the User model
        model = User

        # Specify the fields to include in the form (email and username)
        fields = ["email", "username"]

        # Define a custom CSS class for displaying errors (usually an error message)
        error_class = "error"
