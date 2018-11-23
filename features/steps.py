import time

from lettuce import step, world
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from util import *

'''
    ********************
    *** Login Module ***
    ********************
'''


@step('I goto to website "([^"]*)"')
def step_impl(step, site):
    # Open the site by in browser
    world.browser.get(site)


@step('I tap \'([^\']*)\'')
def step_impl(step, button):
    if button == 'Login':
        assert click_element("xpath", "/html/body/div[2]/div/div/div/div/div[1]/div[1]/form/div/div/div[4]/button")


@step('Pop up window \'([^\']*)\' appears')
def pop_up_appears(step, container):
    # Check if window opened or not
    assert pop_up_window(container)


@step('I enter ([^"]+) in \'([^\']*)\' by \'([^\']*)\'')
def enter_value(step, value, field, locator):
    # Check if value is empty
    value = get_empty_value(value)

    assert type_input(value, locator, field)


@step('I open \'([^\']*)\'')
def step_impl(step, link_text):
    assert click_element("link", link_text)


@step('I should see success message')
def step_impl(step):
    try:
        # Waiting to be login for 8 seconds, If it does not login within 8 seconds it will throw exception
        WebDriverWait(world.browser, 8).until(EC.presence_of_element_located((By.LINK_TEXT, "LOGOUT")))

        set_result("succeeded", "Login successfully")

        # Make LOGOUT
        assert make_logout()
    except TimeoutException:
        # Set the result
        set_result("failed", "Dashboard didn't appear in 8 seconds")

        # Get bootstrap error
        error_message = get_server_msg("id", "loginErrorResponse")

        # Get validation error
        if error_message is None or error_message == "":
            error_message = get_validation_error()

        set_result("failed", "Unknown error occurred" if error_message is None else error_message)
