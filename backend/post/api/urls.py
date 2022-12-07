from django.urls import path, include
from post.api.views import ViewAPIPost, ViewAPIPostList


urlpatterns = [
    path('',
         ViewAPIPost.as_view(),
         name='post'
         ),
         
    path('all/',
         ViewAPIPostList.as_view(),
         name='posts'
         )
]
