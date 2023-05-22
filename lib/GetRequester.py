import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        resp = requests.get(self.url)
        return resp.content

    def load_json(self):
        resp = json.loads(self.get_response_body())
        return resp