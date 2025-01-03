from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from abc import ABC, abstractmethod

from driver import Driver


class Bot(ABC):
    FILLIN_TEXT = "fillin_text"
    CLICK = "click"
    TEXT = "text"

    def __init__(self, headlessBool=True):
        self._driver = Driver(headlessBool)._driver
        self._threadsPool = []

    @abstractmethod
    def scraperWorker(self):
        pass

    @abstractmethod
    def runScraper(self):
        pass

    @abstractmethod
    def run(self):
        pass

    # Perform an action on the given element.
    def performOnElement(self, action, xpath, delay, log_text, fillin_text=""):
        element = self._driver.find_element(By.XPATH, xpath)
        if(action == Bot.FILLIN_TEXT):
            element.send_keys(fillin_text)
        if(action == Bot.CLICK):
            element.click()
        print(log_text)
        time.sleep(delay)

    # Get a param from the given element.
    def getFromElement(self, param, xpath, delay):
        element = self._driver.find_element(By.XPATH, xpath)
        if(param == Bot.TEXT):
            return element.text
        time.sleep(delay)
        return ""

    def shutdownPool(self):
        for tI in self._threadsPool:
            tI.join()

    def shutdown(self):
        self.shutdownPool()
        self._driver.quit()
