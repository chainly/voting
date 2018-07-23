from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_changed
from rest_framework import serializers
from api.models import RadioQuestion, Answer, Vote
from api.constant import SECONDSOFONEDAY

class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=(RadioQuestion.objects.all()))
    _link = serializers.HyperlinkedIdentityField(
            many=False,
            read_only=True,
            view_name='api:answer-detail',
            lookup_field='pk',
        )

    class Meta:
        model = Answer
        exclude = ()


class RadioQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    _link = serializers.HyperlinkedIdentityField(
            many=False,
            read_only=True,
            view_name='api:radioquestion-detail',
            lookup_field='pk',
        )

    class Meta:
        model = RadioQuestion
        exclude = ()
        

class VoteSerializer(serializers.ModelSerializer):
    _link = serializers.HyperlinkedIdentityField(
            many=False,
            read_only=True,
            view_name='api:vote-detail',
            lookup_field='pk',
        )

    def validate(self, data):
        # Should only allow the web user to submit one vote per 24 hour period
        all_answer = Answer.objects.filter(question=data["answer"].question).all()
        last_vote = Vote.objects.filter(owner=data["owner"], answer__in=all_answer).first()
        if last_vote:
            # https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/#concepts
            now = timezone.now()
            itv = (now - last_vote.updated).total_seconds()
            if itv < 0:
                serializers.ValidationError('time error: %s' % last_vote.updated)
            if itv < SECONDSOFONEDAY:
                raise serializers.ValidationError('vote time left: %s seconds' % (SECONDSOFONEDAY - itv))

        return data
    
    class Meta:
        model = Vote
        exclude = ()