import logging

import json
import os
from collections import OrderedDict
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

logger = logging.getLogger(__name__)



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


from _collections import OrderedDict
import logging

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

logger = logging.getLogger(__name__)


# -------------------------------------------------------------------------------
# CustomPageNumberPagination
# -------------------------------------------------------------------------------
class CustomPageNumberPagination(PageNumberPagination):

    page_size = 5
    current_page = 1
    page_size_query_param = 'page_size'

    # ---------------------------------------------------------------------------
    # get_paginated_response
    # ---------------------------------------------------------------------------
    def get_paginated_response(self, data):

        previous_page_number = next_page_number = 0
        logger.info(self.get_next_link())
        if self.get_next_link():
            next_page_number = self.page.number + 1

        if self.get_previous_link():
            previous_page_number = self.page.number - 1 if self.page.number > 0 else 1

        pagination = OrderedDict([
            ('lastPage', self.page.paginator.num_pages),
            ('last_page', self.page.paginator.num_pages),
            ('pageSize', self.page_size),
            ('page_size', self.page_size),
            ('totalItems', self.page.paginator.count),
            ('total_items', self.page.paginator.count),
            ('current', self.page.number),
            ('next', next_page_number),
            ('previous', previous_page_number),
            ('previous_page_link', self.get_previous_link()),
            ('next_page_link', self.get_next_link())
        ])

        return Response(
            OrderedDict([
                ('pagination', pagination),
                ('result', data),
            ])
        )
