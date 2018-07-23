from django.test import LiveServerTestCase
from django.test.client import Client
 
class SimpleTest(LiveServerTestCase):
    """simple test for web/vote after all set"""
    def setUp(self):
        # user
        self.username = 'test'
        self.passwd = '~!@#QWER'
        self.email = '1@1.com'
        from django.contrib.auth.models import User
        user = User.objects.create_superuser(self.username, self.email, self.passwd)
        
        # Every test needs a client.
        self.client = Client()
        self.login()
    
    def login(self):
        # login
        response = self.client.get('/web/vote')
        self.assertRedirects(response, '/accounts/login/?next=/web/vote')
        r = self.client.login(username=self.username ,password=self.passwd)
        self.assertEqual(r, True)
        
    def test_vote(self):
        # vote question
        self.client.post('/api/radio-question/', {"content": 'What is the best video game of all time?'})
        
        response = self.client.get('/web/vote')
        self.assertIn(b'What is the best video game of all time?', response.content)
        self.vote_limit()
        
    def vote_limit(self):
        # vote answer
        self.client.post('/api/answer/', {"question": 1, "content": 'Overwatch'})
        self.client.post('/api/answer/', {"question": 1, "content": 'World of Warcraft'})
        self.client.post('/api/answer/', {"question": 1, "content": 'PUBG'})
        self.client.post('/api/answer/', {"question": 1, "content": 'League of Legends'})
        
        # set HOST
        headers = {"HTTP_HOST": self.live_server_url[7:]}
        response = self.client.post('/web/vote', {'answer': '1'}, **headers)
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/web/vote', {'answer': '1'}, **headers)
        self.assertIn(b'vote time left:', response.content)
