from request_library import AbstractRequest


class AuthManager:
    """
    This class is responsible for managing authentication-related operations such as login and creating a new account.
    It uses an AbstractRequest object to make HTTP requests to the specified endpoint.
    """

    def __init__(self, email: str, password: str, endpoint: str,
                 request: AbstractRequest):
        """
        Initialize an AuthManager object with an email, password, and endpoint. Optionally, an AbstractRequest object
        can be provided. If not, a ConcreteRequestImplementation object will be used by default.

        :param email: The user's email address
        :param password: The user's password
        :param endpoint: The base URL endpoint for authentication-related requests
        :param request: An AbstractRequest object for making HTTP requests
        """
        self.email = email
        self.password = password
        self.request = request
        self.endpoint = endpoint

    def __auth(self, url) -> dict:
        """
        Send an authentication request to the specified URL with the user's email and password.

        :param url: The URL to send the authentication request to
        :return: The response from the server
        """

        self.request.configure_request(url=url, headers={'x-token': 'x-value'})
        response = self.request.make_request(method="POST", data={"email": self.email, "password": self.password})
        return response

    def login(self) -> dict:
        """
        Send a login request to the server with the user's email and password.

        :return: The response from the server
        """
        url = self.endpoint + "/auth"
        return self.__auth(url)

    def create_account(self) -> dict:
        """
        Send a request to the server to create a new account with the user's email and password.

        :return: The response from the server
        """
        url = self.endpoint + "/create-account"
        return self.__auth(url)
