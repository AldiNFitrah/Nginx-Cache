import random

from locust import HttpUser
from locust import between
from locust import task


npms = [10000000000000000000, 1]


class AppUser(HttpUser):
    wait_time = between(1, 1)

    @task
    def get_homepage(self):
        npm = random.choice(npms)
        self.client.get("/read/{}/1".format(npm))
