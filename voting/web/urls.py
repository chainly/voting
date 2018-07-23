from django.urls import re_path
from web.views import VoteView

app_name = 'web'
urlpatterns = [
    re_path('^vote/?', VoteView.as_view(), name='vote'),
]
