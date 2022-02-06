import os
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I am on https://todoist.com/pl')
def step_impl(context):
    context.driver.get("https://todoist.com/pl")


@given('I click "Zaloguj się"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Zaloguj się").click()


@given('I am on login page')
def step_impl(context):
    assert context.driver.title == "Log in to Todoist"


@when('I enter valid email and password')
def step_impl(context):
    valid_email = os.environ.get("T_MAIL")
    valid_pwd = os.environ.get("T_PASS")
    context.driver.find_element(By.ID, "email").send_keys(valid_email)
    context.driver.find_element(By.ID, "password").send_keys(valid_pwd)


@when('I click "Log in" button')
def step_impl(context):
    context.driver.find_element \
        (By.XPATH, "//button[@class='submit_btn ist_button ist_button_red sel_login']").click()


@then('I should be redirected to home page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.title_is("Today: Todoist"))


@when('I enter invalid {email} and {pwd}')
def step_impl(context, email, pwd):
    context.driver.find_element(By.ID, "email").send_keys(email)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@then('Error message is displayed')
def step_impl(context):
    error_msgs = ["Wrong email or password.", "Invalid email address."]
    msg = WebDriverWait(context.driver, 10).until \
        (EC.presence_of_element_located((By.XPATH, "//div[@class='error_msg']")))
    assert msg.get_attribute("innerText") in error_msgs
