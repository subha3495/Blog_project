from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
# Create your views here.

class Mypagepagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'mypage'
    page_size_query_param = 2
    max_page_size = 2
    last_page_strings =('endpages',)

class Mypage_limitoffset(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'mylimit'
    limit_query_param = 'myoffset'
    max_limit = 5

class Mypage_cusore(CursorPagination):
    ordering = '-esal'
    page_size = 2