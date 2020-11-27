from locust import HttpUser, task
import random
from data import names


class LoadGenerater(HttpUser):
    @task
    def shorten_url(self):
        name = random.choice(names)
        data = {"url": "https://www.google.com/search?q=" + name}
        self.client.post("/api/createURL", json=data)
