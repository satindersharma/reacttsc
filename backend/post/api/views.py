import logging

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from post.api.serializers import SerializerAPIPost, SerializerAPIPostList, SerializerAPIPostDetail
from post.models import ModelPost
from base.utils import CustomPageNumberPagination

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewAPIPost
# ---------------------------------------------------------------
class ViewAPIPost(APIView):
    # permission_classes = (AllowAny,)
    serializer_class = SerializerAPIPost

    # ---------------------------------------------------------------
    # get_serializer
    # ---------------------------------------------------------------
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return self.serializer_class(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        queryset = ModelPost.objects.filter(user=request.user)
        response = SerializerAPIPostDetail(queryset, many=True).data

        data = {
                'code': HTTP_200_OK,
                'status': 'success',
                'result': response
            }
        return Response(data, status=HTTP_200_OK)
    # ---------------------------------------------------------------
    # post
    # ---------------------------------------------------------------
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            response = serializer.save()
            data = {
                'code': HTTP_200_OK,
                'status': 'success',
                'result': response
            }
            return Response(data, status=HTTP_200_OK)
        data = {
            'code': HTTP_400_BAD_REQUEST,
            'status': 'error',
            'result': serializer.errors
        }
        return Response(data, status=HTTP_400_BAD_REQUEST)

# ---------------------------------------------------------------
# ViewAPIPostList
# ---------------------------------------------------------------
class ViewAPIPostList(ListAPIView):

    serializer_class = SerializerAPIPostList
    pagination_class = CustomPageNumberPagination
    queryset = ModelPost.objects.all()

    # ---------------------------------------------------------------------------
    # get_serializer_context
    # ---------------------------------------------------------------------------
    def get_serializer_context(self):
        context = ListAPIView.get_serializer_context(self)
        context['request'] = self.request
        return context

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    # ---------------------------------------------------------------------------
    # list
    # ---------------------------------------------------------------------------
    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        response = self.get_serializer(queryset, many=True).data


        data = {
                'code': HTTP_200_OK,
                'status': 'success',
                'result': response
            }
        return Response(data, status=HTTP_200_OK)