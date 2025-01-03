from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.edge.options import Options

from get_chrome_driver import GetChromeDriver

#from bs4 import BeautifulSoup

import os
import sys
import time
import argparse
import traceback
import logging
from datetime import datetime
from abc import ABC, abstractmethod


CHROMEDRIVER_DIR = "chromedriver"


class Driver():
    def __init__(self, headlessBool):
        self._headlessBool = headlessBool
        self._driver = None
        self.installDriver()
        self.initDriver()

    def installDriver(self):
        if(not os.path.isdir(CHROMEDRIVER_DIR)):
            get_driver = GetChromeDriver()
            get_driver.install()

    # Init Chrome driver.
    def initDriver(self):
        options = webdriver.ChromeOptions()
        if(self._headlessBool):
            options.add_argument('--headless')
        self._driver = webdriver.Chrome(options=options)
