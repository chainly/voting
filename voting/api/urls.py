from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views

app_name = 'api'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'radio-question', views.RadioQuestionViewSet)
router.register(r'answer', views.AnswerViewSet)
router.register(r'vote', views.VoteViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls), name='api-root')
]
