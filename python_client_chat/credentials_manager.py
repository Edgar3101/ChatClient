from manage_io import ManageIO
from abc import ABC, abstractmethod

class AbstractCredentialsManager(ABC):
    """
    Abstract base class for managing user credentials, such as email and password.
    You cannot instantiate this class, if you want to define your own class of credetials manager
    you should inherite this class and crete your own.
    """

    email: str
    password: str
    repeat_password: str

    @abstractmethod
    def get_credentials(self, option) -> tuple:
        """
        Abstract method to create and user or login based on option.
        :param option: The option to choose between logging in or creating a new account.
        :return: A tuple with email and password.
        """
        pass

    @abstractmethod
    def __login(self) -> None:
        """
        Abstract method to handle user login, prompting the user to enter their email and password.
        :return: None
        """
        pass

    @abstractmethod
    def __create_user(self) -> None:
        """
        Abstract method to create a new user, prompting the user to enter their email, password, and repeat the password.
        :return: None
        """
        pass


class CredentialsManager(AbstractCredentialsManager):
    """
    Logic class for handling user-related operations, such as logging in and creating new accounts.
    """

    # email of the user
    email: str
    # password of the user
    password: str
    # repeated password of the user
    repeat_password: str

    
    def get_credentials(self, option) -> tuple:
        """
        Gets the user's email and password, depending on the given option.

        :param option: The option to choose between logging in or creating a new account.
        :return: A tuple containing the user's email and password.
        """
        if option == "Login":
            self.__login()

        if option == "Create Account":
            self.__create_user()

        return (self.email, self.password)


    def __login(self) ->  None :
        """
        Prompts the user to enter their email and password for logging in.

        :return: None
        """
        self.email = ManageIO.input_string(question="Please enter your email: ")
        self.password = ManageIO.input_string(question="Please Provide your password: ", password=True)
    
    def __create_user(self) -> None :
        """
        Creates a new user by prompting the user to enter their email, password, and repeating the password.
        If the repeated password does not match the original password, an exception is raised.

        :return: None
        """
        self.__login()
        self.repeat_password= ManageIO.input_string(question="Please repeat your password: ", password=True)
        if self.password != self.repeat_password:
            raise Exception("Sorry, the passwords do not match")
        
