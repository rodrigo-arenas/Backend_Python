import uuid
from locust import HttpUser, TaskSet, task, between
from store.tests.endpoints_test import get_auth_header
"""
Run locus with:
locust -f ./store/tests/local_load_test.py
"""


class BookstoreLocusTasks(TaskSet):
    #@task
    #def token_test(self):
    #    self.client.post('/token', dict(username='test', password='test'))

    @task
    def post_user_test(self):
        user_dict = {"username": uuid.uuid4().hex,
                     "password": uuid.uuid4().hex,
                     "mail": "mails@mail.com",
                     "role": "admin"}
        auth_header = get_auth_header()
        self.client.post('/v1/user', json=user_dict, headers=auth_header)


class BookstoreLoadTest(HttpUser):
    tasks = [BookstoreLocusTasks]
    host = 'http://127.0.0.1:5000'
    wait_time = between(1, 3)
    stop_timeout = 20
