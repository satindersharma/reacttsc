import logging
from django.db import models
from base.models import ModelAbstractBase
import uuid
from account.models import ModelAccountUser


logger = logging.getLogger(__name__)


class ModelPost(ModelAbstractBase):
    """Post"""
    uid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text="Unique identification number for the user."
    )

    title = models.CharField(
        max_length=100,
        help_text="Post Title"
    )

    body = models.CharField(
        max_length=250,
        help_text="Post Body"
    )

    user = models.ForeignKey(ModelAccountUser, 
        related_name="user_post",
        on_delete=models.CASCADE,
        help_text="The user associated with this post.",)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']


    def __str__(self):
        return self.title
    
    