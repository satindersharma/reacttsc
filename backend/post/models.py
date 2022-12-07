import logging
from django.db import models
from base.models import ModelAbstractBase
import uuid

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

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
        return self.title
    
    