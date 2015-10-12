# -*- coding:utf-8 -*-

import pytest
import time
from selenium.webdriver.common.keys import Keys


class TestLoginPage(object):
    @pytest.mark.functional
    @pytest.mark.parametrize('username,password,error_message', (
        ("admin", 'admin', u"Sign out"),
        ("admin", "test", u"Please enter a correct username and password. Note that both fields may be case-sensitive."),
    ))
    def test_login_with_wrong_credentials(self, browser, username, password, error_message):
        login_url = "http://localhost/login/"
        browser.delete_all_cookies()
        browser.get(login_url)

        email = browser.find_element_by_id('id_username')
        email.send_keys(username)

        pw = browser.find_element_by_id('id_password')
        pw.send_keys(password)

        time.sleep(1)
        pw.send_keys(Keys.ENTER)
        time.sleep(1)

        assert error_message in browser.page_source