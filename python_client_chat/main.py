from .greeting import Greeting
from .credentials_manager import CredentialsManager
from .request_library import ConcreteRequestImplementation
from .auth_manager import AuthManager
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Main:
    """
    Facade pattern implementation for simplified API interaction.
    """

    def __init__(self):
        """
        Initialize all necessary classes.
        """
        self.greeting = Greeting()
        self.credentials_manager = CredentialsManager()
        self.request_manager = ConcreteRequestImplementation()
        self.endpoint = os.getenv("API_ENDPOINT")
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

        # Configure the request manager with the API endpoint and headers
        self.request_manager.configure_request(
            self.endpoint,
            headers={"x-token": 'x-client'}
        )

        # Authenticate the user and get the auth token
        if option == "Login":
            self.auth_token = auth.login()

        # Create a new account and get the auth token
        elif option == "Create Account":
            self.auth_token = auth.create_account()

        # Here you can use the auth_token for further API requests

    


        
        



