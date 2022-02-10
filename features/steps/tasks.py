from behave import given, when, then, use_fixture
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from features.environment import get_id


@given('I am on home page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.title_is("Today: Todoist"))


@when('I click "+Add task"')
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


@given('I am logged in and there is a task in the inbox')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "filter_inbox"))).click()
    tasks = context.driver.find_elements(By.XPATH, "//li//div[@class='markdown_content task_content']")
    if tasks:
        pass
    else:
        context.execute_steps('''given I am on home page
        when I click "+Add task"
        and Enter Sample task and schedule it
        and Click "Add Task"
        then The Sample task is added''')


@when('I click "Edit task"')
def step_impl(context):
    task_id = use_fixture(get_id, context)
    task_to_edit = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[@id='{task_id}']")))
    ActionChains(context.driver).move_to_element(task_to_edit).perform()
    context.driver.find_element(By.XPATH, "//button[@aria-label='Edit']").click()


@when('Change text to {updated}')
def step_impl(context, updated):
    text_field = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable
        ((By.XPATH, "//div[@class='notranslate public-DraftEditor-content']")))
    text_field.send_keys(Keys.CONTROL, 'a')
    text_field.send_keys(updated)


@when('I click "Save"')
def step_impl(context):
     WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable
        ((By.XPATH, "//button[@class='reactist_button reactist_button--primary']"))).click()


@then('The task is changed to {updated}')
def step_impl(context, updated):
    task_id = use_fixture(get_id, context)
    updated_task = context.driver.find_element(By.ID, task_id)
    assert updated_task.text == updated


@when('I click "More task actions"')
def step_impl(context):
    task_id = use_fixture(get_id, context)
    task_to_delete = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//div[@id='{task_id}']")))
    ActionChains(context.driver).move_to_element(task_to_delete).perform()
    context.driver.find_element(By.XPATH, "//button[@data-testid='more_menu']").click()


@when('Click "Delete task"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[text()='Delete task']").click()
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()


@then('Task is deleted')
def step_impl(context):
    deleted_task_id = use_fixture(get_id, context)
    try:
        context.driver.find_element(By.ID, deleted_task_id)
    except NoSuchElementException:
        pass
