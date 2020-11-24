from locust import HttpUser, task
import random
from data import city_names


class LoadGenerater(HttpUser):
    @task
    def shorten_url(self):
        name = random.choice(city_names)
        data = {"url": "https://www.google.com/search?q=" + name}
        self.client.post("/api/createURL", json=data)
