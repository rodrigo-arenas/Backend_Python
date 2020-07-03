import uuid
from locust import HttpUser, TaskSet, task, between

"""
Run locus with:
locust -f ./store/tests/local_load_test.py
"""


class BookstoreLocusTasks(TaskSet):
    @task
    def token_test(self):
        self.client.post('/token', dict(username='test', password='test'))

    #@task
    #def post_user_test(self):
    #    user_dict = {"username": uuid.uuid4().hex,
    #                 "password": uuid.uuid4().hex,
    #                 "mail": "mails@mail.com",
    #                 "role": "admin"}
    #    auth_header = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ0ZXN0Iiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNTkzNzM4MDAzfQ.5sHHslXdGe8PfXBiI_x9VhSsY3igLB2P4HPgv06UZVM'}
    #    self.client.post('/v1/user', json=user_dict, headers=auth_header)


class BookstoreLoadTest(HttpUser):
    tasks = [BookstoreLocusTasks]
    host = 'http://127.0.0.1:5000'
    wait_time = between(4, 10)
    stop_timeout = 20
