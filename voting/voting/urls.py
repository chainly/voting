from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    # for user
    path('accounts/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # for vote
    re_path(r'^api/', include('api.urls', namespace='api')),
    re_path(r'^web/', include('web.urls', namespace='web')),
]
