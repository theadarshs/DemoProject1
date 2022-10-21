from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

from pageObjects.SearchObject import SearchPage
from pageObjects.loginPage import LoginPage
from tests.conftest import driver
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log=self.getLogger()
        loginid= LoginPage.login(self)
        log.info("login id or paasword")
        time.sleep(5)
        search=SearchPage.search(self)
        log.info("searching done")
