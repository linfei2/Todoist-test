import os
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@given('I open https://todoist.com/pl')
def step_impl(context):
    context.driver.get("https://todoist.com/pl")


@given('I click "Zaloguj się"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Zaloguj się").click()


@given('I am on login page')
def step_impl(context):
    assert context.driver.title == "Log in to Todoist"


@when('I enter valid email')
def step_impl(context):
    valid_email = os.environ.get("T_MAIL")
    context.driver.find_element(By.ID, "email").send_keys(valid_email)


@when('I enter valid password')
def step_impl(context):
    valid_pass = os.environ.get("T_PASS")
    context.driver.find_element(By.ID, "password").send_keys(valid_pass)


@when('I click "Log in" button')
def step_impl(context):
    context.driver.find_element \
        (By.XPATH, "//button[@class='submit_btn ist_button ist_button_red sel_login']").click()


@then('I should be redirected to home page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.title_is("Today: Todoist"))
    context.driver.close()


@when('I enter invalid email "{email}"')
def step_impl(context, email):
    context.driver.find_element(By.ID, "email").send_keys(email)


@when('I enter invalid password "{pwd}"')
def step_impl(context, pwd):
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@then('Message "Wrong email or password" is displayed')
def step_impl(context):
    msg = WebDriverWait(context.driver, 10).until \
        (EC.presence_of_element_located((By.XPATH, "//div[@class='error_msg']")))
    assert msg.get_attribute("innerText") == "Wrong email or password."
    context.driver.close()
