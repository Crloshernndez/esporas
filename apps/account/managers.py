from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    """
    Custom user account manager for the UserAccount model.
    """
    
    def email_validator(self, email):
        """
        Validates an email address.

        Args:
            email (str): The email address to validate.

        Raises:
            ValueError: If the email address is invalid.

        Returns:
            None
        """
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates and saves a new user with the given username, email, and password.

        Args:
            username (str): The username for the new user.
            email (str): The email address for the new user.
            password (str): The password for the new user.
            extra_fields (dict): Additional fields to be saved in the user model.

        Raises:
            ValueError: If the username is empty or if email is missing or invalid.

        Returns:
            User: The newly created user.
        """
        if not username:
            raise ValueError(_("Users must have a username"))
        
        if email:
            email = self.normalize_email(email).lower()
            self.email_validator(email)
        else:
            raise ValueError(_("User must have an email address"))
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """
        Creates and saves a new superuser with the given username, email, and password.

        Args:
            username (str): The username for the new superuser.
            email (str): The email address for the new superuser.
            password (str): The password for the new superuser.
            extra_fields (dict): Additional fields to be saved in the superuser model.

        Raises:
            ValueError: If the password is missing or empty.

        Returns:
            User: The newly created superuser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if not password:
            raise ValueError(_("Superusers must have a password"))
        
        user, created = self.get_or_create(username=username, email=email, **extra_fields)
        if created:
            user.set_password(password)

        user.is_superuser = True
        user.is_staff = True
        user.is_active = extra_fields.get("is_active", True)

        user.save(using=self._db)
        return user