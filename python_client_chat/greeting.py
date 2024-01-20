from colorama import Fore, Back, Style
import sys
from manage_io import ManageIO

class Greeting:
    """
    Logic class
    """

    def greet(self) -> None:
        """
        Displays a welcome message with green background and white text.
        We set the method as static because there's no reason to instantiate this class
        """
        print("\n" + Fore.WHITE + Back.GREEN + "Welcome to my SUPER CHAT" + Style.RESET_ALL + "\n")

    def create_or_login(self) -> str:
        """
        Displays a list of options to the user to either login or create an account.
        We set the method as static because there's no reason to instantiate this class
        """
        option = ManageIO.manage_options("Do yo want to login or create an account?", [
            "Login",
            "Create Account",
            "Exit"
        ])

        if option == "Exit":
            self.good_bye()
        
        return option

            
    def good_bye(self) -> None:
        """
        Displays a good bye message and we set status 1 to end program
        We set the method as static because there's no reason to instantiate this class
        """

        print("\nGood bye and come soon")
        sys.exit(1)
        
        
