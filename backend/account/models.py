import logging
from django.db import models
import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from account.manager import ManagerAccountUser
from base.models import ModelAbstractBase


logger = logging.getLogger(__name__)


# ------------------------------------------------------------------------------
# ModelAccountUser
# ------------------------------------------------------------------------------
class ModelAccountUser(AbstractBaseUser, ModelAbstractBase, PermissionsMixin):
    """
    Stores authentication information about a user of the system.
    """

    uid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text="Unique identification number for the user."
    )
    email = models.EmailField(
        max_length=225,
        unique=True,
        help_text="Email of the user."
    )

    phone_number = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        help_text="What is the user's phone number?"
    )

    first_name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        help_text="What is the user's first name?"
    )

    last_name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        help_text="what is the user's last name?"
    )

    country = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="What is the user's country?"
    )

    city = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="What is the user's city?"
    )

    is_active = models.BooleanField(
        default=False,
        help_text="Is the user active?"
    )

    is_staff = models.BooleanField(
        default=False,
        help_text="Is the user as a staff member?"
    )

    is_superuser = models.BooleanField(
        default=False,
        help_text="Is the user a super user?"
    )

    objects = ManagerAccountUser()

    USERNAME_FIELD = 'email'


    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:
        db_table = "account_user"
        verbose_name = "User"
        verbose_name_plural = "Users"


    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the user object.
        """
        return self.email


    # ---------------------------------------------------------------------------
    # full_name
    # ---------------------------------------------------------------------------
    @property
    def full_name(self):
        """
        Method to return user's full name
        """

        if self.first_name and self.last_name:
            return "{} {}".format(self.first_name, self.last_name).title()
        else:
            return self.email