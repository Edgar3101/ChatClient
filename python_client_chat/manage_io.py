import inquirer
import getpass

class ManageIO:
    """
    This class Manages all input and output related things.
    Implementation class
    """

    @staticmethod
    def manage_options(message: str, options: list[str]) -> str :
        """
        This method displays a list of options to the user with the given message and returns the
        user's selection as a string or integer (depending on the options provided).

        :param message: The message to display to the user
        :param options: A list of strings representing the available options
        :return: The user's selection as a string
        """

        questions = [inquirer.List('option',
                                  message=message,
                                  choices=options
                                  )]
        
        awnsers = inquirer.prompt(questions=questions)
        return awnsers['option']
    
    @staticmethod
    def input_string(question: str, style: list | None, password : bool = False) -> str | Exception:
        """
        This method prompts the user to enter a string value with the given question.
        If password is True, the input will be hidden. The style parameter is not implemented yet


        :param question: The question to display to the user.
        :param style: A list of style directives for the input prompt. Not implemented.
        :param password: If True, the input will be hidden (e.g. for passwords).
        :return: The user's input as a string or integer, or an Exception if password is True and style is not None.
        """
        if password and style:
            raise Exception("Sorry, you cannot style password input")

        if password:
            data = getpass.getpass(question)
        else:
            data = input(question)

        
        if not data:
            raise ValueError("Input was empty")
        return data



