import os
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('I click "Zaloguj się"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Zaloguj się").click()


@when('Enter valid credentials')
def step_impl(context):
    valid_email = os.environ.get("T_MAIL")
    valid_pwd = os.environ.get("T_PASS")
    context.driver.find_element(By.ID, "email").send_keys(valid_email)
    context.driver.find_element(By.ID, "password").send_keys(valid_pwd)


@given('I am on home page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.title_is("Today: Todoist"))


@when('I click "Add task"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@class='plus_add_button']").click()


@when('Enter {task} and schedule it')
def step_impl(context, task):
    context.driver.find_element \
        (By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']"). \
        send_keys(task)
    context.driver.find_element(By.XPATH, "//button[@class='item_due_selector icon_pill']").click()
    context.driver.find_element(By.XPATH, "//div[text()='Tomorrow']").click()


@when('Click "Add Task"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('The {task} is added')
def step_impl(context, task):
    context.driver.find_element(By.ID, "filter_inbox").click()
    context.driver.find_element(By.XPATH, f"//div[text()='{task}']")