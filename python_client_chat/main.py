from greeting import Greeting
from credentials_manager import CredentialsManager
from request_library import ConcreteRequestImplementation, ConcreteUrlLibImplementation
from auth_manager import AuthManager


class AuthFacade:
    """
    Facade pattern implementation for simplified API interaction.
    """

    def __init__(self, api_endpoint: str, concrete_request_manager: str = "requests"):
        """
        Initialize all necessary classes.

        :param api_endpoint: The API end_point where we're going to manage request ops
        :param concrete_request_manager: The interface to manage request. If "requests" is passed we'll use requests \
        and if "urllib" is passed we'll use urllib
        """
        self.greeting = Greeting()
        self.credentials_manager = CredentialsManager()

        # We choose our manager request for further operations
        if concrete_request_manager == "requests":
            self.request_manager = ConcreteRequestImplementation()
        if concrete_request_manager == "urllib":
            self.request_manager = ConcreteUrlLibImplementation()

        self.endpoint = api_endpoint
        self.auth_token = ""

    def main(self):
        """
        Execute the main process of the application.
        """
        # Print the welcome message
        self.greeting.greet()

        # Print the options for the user
        option = self.greeting.create_or_login()

        # Get the user's credentials based on the selected option
        (email, password) = self.credentials_manager.get_credentials(option=option)

        # Initialize the AuthManager with the user's email, password, and request manager
        auth = AuthManager(email, password, request=self.request_manager, endpoint=self.endpoint)

        response = None

        # Authenticate the user and get the auth token
        if option == "Login":
            response = auth.login()

        # Create a new account and get the auth token
        elif option == "Create Account":
            response = auth.create_account()

        # Even if the responde is None Or false, it's means authentitation is failed
        if not response.get("isAuth"):
            raise Exception("Lo siento, no pudimos autenticarte correctamente")

        self.auth_token = response.get("token")
