"""Module defining classes and functions related to dating websites.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

import account
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

class Website:
    """Represents a typical website.

    Attributes:
        name: A string containing the name of the website.
        url: A string containing the url of the website.
        account: An Account object associated with the website.
        web_driver: The web driver used open and utilize the website.
    """

    def __init__(self, name, url, account, web_driver = None):
        """Initializes Website class with name, url, account, and web driver.

        If web_driver is not specified, a new web driver is created.
        """
        self.name = name
        self.url = url
        self.account = account

        if web_driver is None:
            self.web_driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver.exe")
        else:
            self.web_driver = web_driver

    def open(self):
        """Opens the website using its specified url."""
        self.web_driver.get(self.url)

    def __find_element_by_xpath(self, xpath):
        """Finds a web element by its xpath.

        Searches for the element until a certain time
        limit is reached, after which an exception is raised.

        Args:
            xpath: The xpath of the desired element.

        Returns:
            The element whose xpath matches the user-specified xpath.

        Raises:
            TimeoutException: The element was not found on the webpage
                before the time limit was reached.
        """
        try:
            element = WebDriverWait(self.web_driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
            return element
        except TimeoutException:
            print("Error: Timeout reached. Could not locate element with xpath: " + xpath)

    def click_button(self, xpath):
        """Clicks on an element with the specified xpath.

        Args:
            xpath: The xpath of the desired element.
        """
        self.__find_element_by_xpath(xpath).click()

    def send_keys(self, xpath, input):
        """Sends keyboard input to an element with the a specified xpath.

        Args:
            xpath: The xpath of the desired element.
            input: The keyboard input to send."""
        self.__find_element_by_xpath(xpath).send_keys(input)

    def switch_to_new_window(self):
        """Switches focus to a newly opened browser window."""
        num_windows_before = len(self.web_driver.window_handles)
        WebDriverWait(self.web_driver, 30).until(expected_conditions.number_of_windows_to_be(2))
        self.web_driver.switch_to_window(self.web_driver.window_handles[1])

    def switch_to_window_by_index(self, index):
        """Switches focus to a window by its index.

        Args:
            index: The index of the desired window.
        """
        self.web_driver.switch_to_window(self.web_driver.window_handles[index])

class DatingWebsite(Website):
    """Represents a typical dating website.

    Attributes:
        name: A string containing the name of the dating website.
        url: A string containing the url of the dating website.
        account: An Account object associated with the dating website.
        web_driver: The web driver used open and utilize the dating website.
    """

    def __init__(self, name, url, account, web_driver = None):
        """Initializes DatingWebsite class."""
        super().__init__(name, url, account, web_driver)

    def run_auto_liker(self):
        """Runs the auto liking sequence for a dating website."""
        self.open()
        self.login()
        self.auto_like()

class Tinder(DatingWebsite):
    """Represents Tinder, the dating website.

    Attributes:
        name: A string containing the name of the website.
        url: A string containing the url of the website.
        account: An Account object associated with the website.
        web_driver: The web driver used open and utilize the website.
    """

    def __init__(self, account, web_driver = None):
        """Initializes Tinder class with name, url, account, and web_driver."""
        super().__init__("Tinder", "https://tinder.com/", account, web_driver)

    def login(self):
        """Logs in the user using their email and password from the Tinder
        homepage.
        """
        self.click_button("//button[@aria-label='Log in with Facebook']")

        self.switch_to_new_window()

        self.send_keys("//input[@id='email']", self.account.email)
        self.send_keys("//input[@id='pass']", self.account.password)
        self.click_button("//input[@id='u_0_0']")

    def auto_like(self):
        """Auto likes potential matches after user is logged in."""
        self.switch_to_window_by_index(0)

        self.click_button("//button[@aria-label='Onboarding.great']")
        self.click_button("//button[@aria-label='Enable']")

        while(True):
            self.click_button("//button[@class='button Lts($ls-s) Z(0) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) recsGamepad__button D(b) Bgc(#fff) Wc($transform) recsGamepad__button--like Scale(1.1):h']")
            time.sleep(1)

class OkCupid(DatingWebsite):
    """ Represents OkCupid, the dating website."""

    def __init__(self, account, web_driver = None):
        """Initializes OkCupid class with name, url, account, and web_driver."""
        super().__init__("OkCupid", "https://www.okcupid.com/", account, web_driver)

    def login(self):
        """Logs in the user using their email and password from the Tinder
        homepage.
        """
        self.click_button("//a[@class='splashdtf-header-signin-splashButton']")

        self.click_button("//button[@class='login2017-actions-link']")

        self.switch_to_new_window()

        self.send_keys("//input[@id='email']", self.account.email)
        self.send_keys("//input[@id='pass']", self.account.password)
        self.click_button("//input[@id='u_0_0']")

        # Checks if the Facebook permissions window pops up and, if so, clicks "Continue"
        xpath = "//button[@class='_42ft _4jy0 layerConfirm _1fm0 _51_n autofocus _4jy3 _4jy1 selected _51sy']"
        if (len(self.web_driver.window_handles) > 1 and self.find_elements_by_xpath(xpath).size() > 0):
            self.click_button(xpath)

    def auto_like(self):
        """Auto likes potential matches after user is logged in."""
        self.switch_to_window_by_index(0)
        self.click_button("//a[@href='/doubletake']")

        while (True):
            self.click_button("//button[@class='cardactions-action cardactions-action--like']")
            time.sleep(1)
