import logging

from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from post.models import ModelPost


logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# SerializerAPIPost
# ---------------------------------------------------------------
class SerializerAPIPost(serializers.Serializer):
    """
    Represents login data.
    """

    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=250)

    
    # ---------------------------------------------------------------
    # login
    # ---------------------------------------------------------------
    def save(self):
        post = ModelPost.objects.create(
            title=self.validated_data['title'],
            body=self.validated_data['body'],
            user=self.context['request'].user,
            
        )
        
        return SerializerAPIPostDetail(post).data

    
# ---------------------------------------------------------------
# SerializerAPIPostDetail
# ---------------------------------------------------------------
class SerializerAPIPostDetail(serializers.ModelSerializer):

    class Meta:
        model = ModelPost
        fields = ('id','title','body')


class SerializerAPIPostList(serializers.ModelSerializer):

    class Meta:
        model = ModelPost
        fields = ('id','title','body','user')


