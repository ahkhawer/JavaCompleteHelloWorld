import datetime
import time

from lettuce import before, world, after
from selenium import webdriver

# Time delay
time_delay = 0.5


class console_color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@before.all
def step_impl():
    # Initialize broswer
    # world.browser = webdriver.Firefox()
    world.browser = webdriver.Chrome()

    # Start time for feature
    print console_color.HEADER + "Start time: " + str(datetime.datetime.now())


@after.each_step
def step_impl(step):
    # Delay after each step
    time.sleep(time_delay)


def show_result():
    # Status of scenario
    print (console_color.FAIL if world.STATUS == "failed" else console_color.OKGREEN) + "Status: " + world.STATUS

    # Message of scenario
    print "Message: " + str(world.MESSAGE.encode('utf-8'))

    # Clear values
    world.STATUS = ""
    world.MESSAGE = ""


@after.each_outline
def step_impl(scenario, outline):
    show_result()


@after.each_scenario
def step_impl(scenario):
    show_result()


@after.all
def step_impl(feature):
    # Quit browser
    world.browser.quit()

    time.sleep(4)

    # End time for feature
    print   "End time: " + str(datetime.datetime.now())
