from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    yield context.driver
    context.driver.quit()

def before_scenario(context, scenario):
    use_fixture(launch_browser, context)