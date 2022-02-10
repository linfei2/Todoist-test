from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.common.by import By


@fixture
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    yield context.driver
    context.driver.quit()

def before_scenario(context, scenario):
    use_fixture(launch_browser, context)


@fixture
def get_id(context):
    task = context.driver.find_elements(By.XPATH, "//div[@class='task_list_item__content__wrapper']")[-1]
    task_id = task.get_attribute('id')
    return task_id
