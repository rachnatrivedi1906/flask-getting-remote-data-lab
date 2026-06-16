import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Make a GET request to `self.url` and return the raw response content.

        Returns bytes (the response body) so tests that compare to a byte
        string will pass.
        """
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content

    def load_json(self):
        """Return the JSON-decoded content of the response.

        Uses `get_response_body` to fetch the data, then decodes bytes to a
        Python object using `json.loads`.
        """
        body = self.get_response_body()
        # response.content is bytes; decode to str then parse
        return json.loads(body.decode('utf-8'))