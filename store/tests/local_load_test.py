from locust import HttpUser, TaskSet, task, between


class BookstoreLocusTasks(TaskSet):
    @task
    def token_test(self):
        self.client.post('/token', dict(username='test', password='test'))


class BookstoreLoadTest(HttpUser):
    tasks = [BookstoreLocusTasks]
    host = 'http://127.0.0.1:5000'
    wait_time = between(3, 10)
