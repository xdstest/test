# -*- coding: utf-8 -*-

import shutil
from django.conf import settings

import os
import pytest
from selenium import webdriver


def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        browser = item.funcargs.get('browser', None)
        log_dir = item.funcargs.get('log_dir', None)
        if browser and log_dir:
            browser.get_screenshot_as_file(os.path.join(
                log_dir, '{}_{}.png'.format(item.cls.__name__, item.name)
            ))


@pytest.fixture(scope='session')
def log_dir(request):
    logs = os.path.join(settings.TESTS_REPORTS_ROOT, 'selenium')
    if os.path.isdir(logs):
        for f in os.listdir(logs):
            src_name = os.path.join(logs, f)
            if os.path.islink(src_name) or os.path.isdir(src_name):
                raise Exception('Check TESTS_REPORTS_ROOT var in settings')
        shutil.rmtree(logs)
    os.makedirs(logs)
    return logs


@pytest.yield_fixture(scope='session')
def browser(request, log_dir):
    driver = webdriver.PhantomJS(
        service_args=['--ignore-ssl-errors=true'],
        service_log_path=os.path.join(log_dir, 'ghostdriver.log')
    )
    driver.set_window_size(1280, 1024)

    yield driver

    driver.quit()