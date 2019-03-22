# from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from polls import apiview, apiviewsets


class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.view = apiviewsets.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='823w74ytrh3948gh!'
        )

    def test_list(self):
        request = self.factory.get(
            self.uri,
            HTTP_AUTHORIZATION='Token {}'.format(self.token.key)
        )
        request.user = self.user
        response = self.view(request)
        self.assertEqual(
            response.status_code, 
            200,
            '预期200状态的响应，但响应码为{}.'.format(response.status_code)
        )

    def test_list2(self):
        # self.client.login(username='test', password='823w74ytrh3948gh!')
        self.client.force_authenticate(user=self.user, token=self.token)
        response = self.client.get('/api-polls/polls/')
        self.assertEqual(
            response.status_code,
            200,
            '预期200状态的响应，但响应码为{}.'.format(response.status_code)
        )

    def test_create(self):
        self.client.login(username='test', password='823w74ytrh3948gh!')
        params = {
            'question': '如何看待第一届杨超越杯编程大赛？',
            'created_by': self.user.id
        }
        response = self.client.post('/api-polls' + self.uri, params)
        self.assertEqual(
            response.status_code,
            201,
            '预期201状态的响应，但响应码为{}.'.format(response.status_code)
        )
