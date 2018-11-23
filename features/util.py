from lettuce import world
from selenium.webdriver.common.by import By


# from selenium import webdriver
# browser = webdriver.Firefox()


# Open link with text
def open_link(link_text):
    return click_element("link", link_text)


# Set the result to Global
def set_result(status, message):
    world.STATUS = status
    world.MESSAGE = message


# Make the logout
def make_logout():
    return open_link("LOGOUT")


# For HTML5 validation error
def get_validation_error():
    try:
        # Switch to invalid element
        act_ele = world.browser.switch_to.active_element

        # Get validation error
        return "\"" + act_ele.get_attribute("validationMessage") + "\" in \"" + act_ele.get_attribute(
            "placeholder") + "\" field"
    except:
        return None


# If 'value' is '(empty)' return empty string
def get_empty_value(value):
    # To set field empty
    return "" if value == "(empty)" else value


# For server response
def get_server_msg(locator, identifier):
    try:
        # Find bootstrap error element and return text
        return get_element(locator, identifier).text
    except:
        # Didn't find bootstrap error element
        return None


# Input 'value' in 'field'
def type_input(value, locator, field):
    field_element = get_element(locator, field)

    try:
        # Empty the element if any value is there
        field_element.clear()

        # Typing in found element
        field_element.send_keys(value)

        # Input successfully
        return True
    except AttributeError:
        return False
    except:
        set_result("failed", "Unknown error for " + field)
        return False


# Select value from Spinner
def select_spnr_value(field, value):
    # Click the value in Spinner
    list_element = get_element("id", field)

    # Iterate to all the options
    for option in list_element.find_elements_by_tag_name('li'):
        # Check option contain any part of value
        if value.strip() in option.text.strip():
            # Choose that value
            option.click()
            break


ele_loc = {
    "id": By.ID,
    "xpath": By.XPATH,
    "link": By.LINK_TEXT,
    "partial_link": By.PARTIAL_LINK_TEXT,
    "name": By.NAME,
    "tag": By.TAG_NAME,
    "class": By.CLASS_NAME,
    "css": By.CSS_SELECTOR
}


def get_element(by, identifier):
    try:
        return world.browser.find_element(ele_loc.get(by), identifier)
    except:
        set_result("failed", "Could not find the " + identifier + " with " + by)
        return None


def click_element(by, identifier):
    # Find the element
    element = get_element(by, identifier)

    try:
        # Tap element
        element.click()

        # Element clicked
        return True
    except:
        # Set the result
        set_result("failed", "Could not tap " + identifier)

        # Could not click the element
        return False


def pop_up_window(container):
    return get_element("class", container) is not None

