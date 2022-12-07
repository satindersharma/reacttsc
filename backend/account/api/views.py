import logging

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.contrib.auth import logout

from account.api.serializers import SerializerAPIAccountLogin, SerializerAPIAccountSignUp, SerializerAPIAccountLogout
from account.models import ModelAccountUser

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewAPIAccountLogin
# ---------------------------------------------------------------
class ViewAPIAccountLogin(APIView):

    permission_classes = (AllowAny,)
    serializer_class = SerializerAPIAccountLogin

    # ---------------------------------------------------------------
    # get_serializer
    # ---------------------------------------------------------------
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return self.serializer_class(*args, **kwargs)

    # ---------------------------------------------------------------
    # post
    # ---------------------------------------------------------------
    def post(self, request, *args, **kwargs):

        logger.debug('Attempting to login a user.')

        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        if serializer.is_valid():
            response = serializer.login()
            data = {
                'code': 200,
                'status': 'success',
                'result': response
            }
            return Response(data, status=HTTP_200_OK)
        data = {
            'code': 400,
            'status': 'success',
            'result': serializer.errors
        }
        return Response(data, status=HTTP_400_BAD_REQUEST)


# ---------------------------------------------------------------
# ViewAPIAccountSignUp
# ---------------------------------------------------------------
class ViewAPIAccountSignUp(APIView):
    """
    API view for sign up 
    """

    permission_classes = (AllowAny, )
    serializer_class = SerializerAPIAccountSignUp

    # ---------------------------------------------------------------
    # get_serializer
    # ---------------------------------------------------------------
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return self.serializer_class(*args, **kwargs)

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
                'code': 200,
                'status': 'success',
                'result': response
            }
            return Response(data, status=HTTP_200_OK)

        data = {
            'code': 400,
            'status': 'error',
            'result': serializer.errors
        }
        return Response(data, status=HTTP_400_BAD_REQUEST)


# -------------------------------------------------------------------------------
# ViewAPILogout
# -------------------------------------------------------------------------------
class ViewAPIAccountLogout(APIView):

    serializer_class = SerializerAPIAccountLogout

    # ---------------------------------------------------------------
    # get_serializer
    # ---------------------------------------------------------------
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance
        """
        return self.serializer_class(*args, **kwargs)

    # ---------------------------------------------------------------------------
    # post
    # ---------------------------------------------------------------------------
    def post(self, request, *args, **kwargs):

        logger.debug('Attempting to logout a user.')

        serializer = self.serializer_class(
            data=request.data,
            context={'user': request.user}
        )

        if serializer.is_valid():

            logger.debug(
                'Logout.'
            )
            logout(request)

            return Response({}, status=HTTP_200_OK)


        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)