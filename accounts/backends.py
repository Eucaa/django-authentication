
#  This file contains custom authentication codes.
from django.contrib.auth.models import User

class EmailAuth:
    """Authenticate a user by an exact match on the email and password (see settings.py line 111)."""

    def authenticate(self, username=None, password=None):  # The first parameter of methods (self) is the instance the method is called on (which is about the same as a function works).
                                                           # The username and password is, by default, set on None.
        """Get an instance of 'User' based off the email and verify the password."""

        try:  # Try to get a user by using User.objects.get.
            user = User.objects.get(email=username)  # In this case, the user's email address will be the user's username.

            if user.check_password(password):  # If the password is available, return the user. If not, then return nothing.
                return user
            return None

        except User.DoesNotExist:  # If the user does not exist, return a None as well.
            return None

    def get_user(self, user_id):
        """Used by the Django authentication system to retrieve a user instance"""

        try:
            user = User.objects.get(pk=user_id)  # Here, var user shall have user_id as primary key(pk).

            if user.is_active:
                return user
            return None

        except User.DoesNotExist:
            return None