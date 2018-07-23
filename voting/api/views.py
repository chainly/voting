from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from api.models import RadioQuestion, Answer, Vote
from api.serializers import RadioQuestionSerializer, AnswerSerializer, VoteSerializer
from api.permissions import OwnerOnly


class RadioQuestionViewSet(viewsets.ModelViewSet):
    """about radio question"""
    queryset = RadioQuestion.objects.all()
    serializer_class = RadioQuestionSerializer
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)    
    
    
class AnswerViewSet(viewsets.ModelViewSet):
    """about answer"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'question')
    

class VoteViewSet(viewsets.ModelViewSet):
    """About vote"""
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          OwnerOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'answer')
    
    def create(self, request, *args, **kwargs):
        if hasattr(request.data, '_mutable'):
            request.data._mutable = True
            request.data.fromkeys('owner', self.request.user.id)
            request.data._mutable = False
        else:
            request.data['owner'] = self.request.user.id
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False, renderer_classes=(renderers.StaticHTMLRenderer,), permission_classes = (permissions.IsAdminUser,))
    def truncate(self, request, *args, **kwargs):
        # @TODO: how to add permissions in action
        assert str(request.user) != 'AnonymousUser', 'login!!!'
        return Response(repr(self.queryset.delete()))


