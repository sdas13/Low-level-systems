from locust import HttpUser, task, between
import random
from data import names


class LoadGenerater(HttpUser):
    @task
    def shorten_url(self):
        name = random.choice(names)
        data = {"url": "https://www.google.com/search?q=" + name}
        self.client.post("/api/createURL", json=data)

    wait_time = between(0.7, 0.8)
