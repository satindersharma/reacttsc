import logging

from django.contrib.auth.models import BaseUserManager



logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ManagerAccountUser
# ---------------------------------------------------------------
class ManagerAccountUser(BaseUserManager):
    """
    Provides manager methods for the user model.
    """

    # ---------------------------------------------------------------
    # create_user
    # ---------------------------------------------------------------
    def create_user(self, email, **kwargs):
        """
        This method creates a new user and its associated profile(empty) 
        that can be updated whenever required.
        """

        if not email:
            raise ValueError('Users must have a valid email address...')

        try:
            password = kwargs.pop('password')
        except KeyError:
            logger.warning("Password for user %s not supplied", email)
            password = ''

        user = self.model(email=self.normalize_email(email), **kwargs)

        # update user password
        user.set_password(password)

        user.is_active = True

        # save the new user
        user.save(using=self._db)

        return user

    # ---------------------------------------------------------------
    # create_superuser
    # ---------------------------------------------------------------
    def create_superuser(self, email, password):
        """
        This method creates a superuser for the system.
        It takes following arguments:
        1) email - email of superuser (required)
        2) password - strong password of superuser (required)
        3) first_name - first name of the superuser (optional)
        4) last_name - last name of superuser (optional)
        """

        logger.info('Creating superuser with email %s', email)

        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        logger.info('Superuser %s successfully created!', user)

        return user

    # ---------------------------------------------------------------
    # signup _process
    # ---------------------------------------------------------------

    def signup_process(self, user_data):
        """
        Signup process performing following steps:
        - Creating ORE Id
        - Registering in database
        - Creating algorand account
        - Generating QR code of user
        """

        # Add User in ORE ID
        # accountName, processId = create_ore_id_user(
        #     user_data
        # )

        # if not accountName:
        #     return None

        # Create user account in database
        user = self.register_user(
            user_data
        )
        
        user.save()
        logger.debug(
            'Signup process completed :: %s', user
        )
        return user

    # ---------------------------------------------------------------
    # register_user
    # ---------------------------------------------------------------
    def register_user(self, user_data):

        logger.debug(
            'Attempting to create a user with data'
        )

        # create the user
        user_email = user_data.pop('email')
        user = self.create_user(user_email, **user_data)

        return user

    # ---------------------------------------------------------------
    # login_user
    # ---------------------------------------------------------------
    def login_user(self, user, request, password=None):
        from authentium.apps.account.api.serializers.user import SerializerAccountUser
        
        # send verification code for ore
        #send_verification_code(email=user.email)

        return {
            'user': SerializerAccountUser(user).data,
            'authenticated': request.user.is_authenticated
        }