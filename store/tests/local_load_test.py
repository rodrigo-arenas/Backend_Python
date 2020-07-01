from locust import HttpUser, TaskSet, task, between

"""
Run locus with:
locust -f ./store/tests/local_load_test.py
"""


class BookstoreLocusTasks(TaskSet):
    @task
    def token_test(self):
        self.client.post('/token', dict(username='test', password='test'))


class BookstoreLoadTest(HttpUser):
    tasks = [BookstoreLocusTasks]
    host = 'http://127.0.0.1:5000'
    wait_time = between(3, 5)
    stop_timeout = 20
