# -*- coding:utf-8 -*-

import pytest
from selenium.webdriver.common.keys import Keys


class TestLoginPage(object):

    @pytest.mark.functional
    @pytest.mark.parametrize("url,show_form_first", (
        ('http://{}'.format(STAGING_SITE_HOST), True),
        ('http://chelyabinsk.{}'.format(STAGING_SITE_HOST), True),
        ('https://{}/user/login/'.format(STAGING_SITE_HOST), False),
    ))
    def test_login_on_any_page(self, browser, url, show_form_first):
        browser.delete_all_cookies()
        browser.get(url)

        if show_form_first:
            browser.find_element_by_class_name('js-login-button').click()

        username = "kvartirka@kvartirka.com"
        password = "kvartirka@kvartirka.com"
        expected_url = 'http://{}/user/'.format(STAGING_SITE_HOST)

        email = browser.find_element_by_class_name('js-loginform-email')
        email.send_keys(username)

        pw = browser.find_element_by_class_name('js-loginform-password')
        pw.send_keys(password)
        pw.send_keys(Keys.ENTER)

        assert browser.current_url == expected_url
        assert (browser.find_element_by_class_name('js-user-name').text ==
                username)

    @pytest.mark.functional
    @pytest.mark.parametrize('username,password,error_message', (
        ("kvartirka@kvartirka.com", 'wrongpassword',
         u"Неправильный логин или пароль."),
        ("nosuchemail@kvartirka.com", "kvartirka@kvartirka.com",
         u"Неправильный логин или пароль."),
    ))
    def test_login_with_wrong_credentials(self, browser, username, password,
                                          error_message):

        login_url = "https://{}/user/login/".format(STAGING_SITE_HOST)
        browser.delete_all_cookies()
        browser.get(login_url)

        email = browser.find_element_by_class_name('js-loginform-email')
        email.send_keys(username)

        pw = browser.find_element_by_class_name('js-loginform-password')
        pw.send_keys(password)

        with wait_for_page_load(browser, timeout=15):
            pw.send_keys(Keys.ENTER)

        assert browser.current_url == login_url
        assert error_message in browser.page_source