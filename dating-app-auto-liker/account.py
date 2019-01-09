"""Module defining classes and functions related to website accounts.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

class Account:
    """Represents a website account.

    Attributes:
        password: A string containing the password of the user's account.
        username: An (optional) string containing the username of the
            user's account.
        email: An (optional) string containing the email of the user's
            account.
    """

    def __init__(self, password, username = None, email = None):
        """Initializes Account class with password and, optionally,
        username and email.
        """
        self.password = password
        self.username = email
        self.email = email
