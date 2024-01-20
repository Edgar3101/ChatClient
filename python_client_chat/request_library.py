# abstract_request.py

from abc import ABC, abstractmethod
import requests
import urllib
import json

class AbstractRequest(ABC):
    """Abstract class for defining a request.

    This class defines the interface for making HTTP requests.
    Concrete implementations should provide their own implementation
    of the 'make_request' method.
    """

    headers: dict
    url: str

    def configure_request(self, headers: dict, url: str):
        """Configure the request by setting the headers and URL.

        :param headers: The headers to be used in the request.
        :param url: The URL to make the request to.
        """
        self.headers = headers
        self.url = url

    @abstractmethod
    def make_request(self, method:str, data: dict | None) -> dict | str:
        """Make an HTTP request.

        :param method: The HTTP method to use (GET, POST, etc.).
        :param data: The data to send with the request, if any.
        :return: The response from the server as a JSON object or string.
        """
        pass


class ConcreteRequestImplementation(AbstractRequest):
    """Concrete implementation of the AbstractRequest class, using request library"""

    def make_request(self, method : str, data: dict|None) -> any:
        """Make an HTTP request using the 'requests' library.

        :param method: The HTTP method to use (GET, POST, etc.).
        :param data: The data to send with the request, if any.
        :return: The response from the server as a JSON object or string.
        """
        if method.upper() == "GET":
            response = requests.get(url=self.url, headers=self.headers)
            return response.json()
        
        if method.upper() == "POST":
            response = requests.post(url=self.url, headers=self.headers, data=data)
            return response.json()


class ConcreteUrlLibImplementation(AbstractRequest):
    """Concrete implementation of the AbstractRequest class, using urlLib librarys"""

    def make_request(self, method : str, data: dict|None):
        """Make an HTTP request using the 'urllib' library.

        :param method: The HTTP method to use (GET, POST, etc.).
        :param data: The data to send with the request, if any.
        :return: The response from the server as a JSON object or string.
        """
        if method.upper() == "POST":
            data = json.dumps(data)
            req = urllib.request.Request(self.url, data, self.headers)

        if method.upper() ==  "GET":
            req = urllib.request.Request(url=self.url, headers=self.headers)
            
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())  



