from behave import given, when, then

@given(u'I launch Chrome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I launch Chrome browser')


@given(u'I open https://todoist.com/pl')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I open https://todoist.com/pl')


@given(u'I click "Zaloguj się"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I click "Zaloguj się"')


@given(u'I am on login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on login page')


@when(u'I enter valid email')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid email')


@when(u'I enter valid password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid password')


@when(u'I click "Log in" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click "Log in" button')


@then(u'I should be redirected to home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be redirected to home page')


@when(u'I enter <invalid email>')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter <invalid email>')


@when(u'I enter <invalid password>')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter <invalid password>')


@then(u'Message "Wrong email or password" is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Message "Wrong email or password" is displayed')
