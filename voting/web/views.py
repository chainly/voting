import requests
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse
from django.db import transaction
from api.models import Vote, RadioQuestion, Answer

@method_decorator(login_required, name='dispatch')
class VoteView(TemplateView):
    template_name = 'web/vote.html'
    
    def get(self, request, *args, **kwargs):
        last_vote = Vote.objects.filter(owner=self.request.user).first()
       
        return render(
            request,
            self.template_name,
            {
                'msg': '',
                'user': self.request.user,
                'question': RadioQuestion.objects.filter(id=1).first(),
                'answer': Answer.objects.filter(question__id=1),
                'vote': reverse('web:vote'),
                'last_vote': last_vote and last_vote.answer.content,
            }
        )

    # seem dead lock if use atomic
    #@transaction.non_atomic_requests
    def post(self, request, *args, **kwargs):
        # @TODO use js later
        msg = 'done'
        try:
            cookies = {
                "sessionid": request.COOKIES["sessionid"],
                "csrftoken": request.COOKIES["csrftoken"],
            }
            headers = {
                "X-CSRFTOKEN":  request.COOKIES["csrftoken"],
            }
            json = {
                "answer": request.POST.get('answer')
            }
            data = requests.post('http://' + request.get_host() + reverse('api:vote-list'),
                                 json=json, cookies=cookies, headers=headers)
        except Exception as err:
            msg = repr(err)
        else:
            msg = data.content
        last_vote = Vote.objects.filter(owner=self.request.user).first()
        return render(
            request,
            self.template_name,
            {
                'msg': msg,           
                'user': self.request.user,
                'question': RadioQuestion.objects.filter(id=1).first(),
                'answer': Answer.objects.filter(question__id=1),
                'vote': reverse('web:vote'),
                'last_vote': last_vote and last_vote.answer.content,
            }
        )