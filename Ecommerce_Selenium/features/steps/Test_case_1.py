from behave import given, then, when

@given(u'Je suis le site "{expected_url}"')
def step_impl(context, expected_url):
    assert context.driver.current_url == expected_url

@then(u'La page d\'accueil est visible')
def step_impl(context):
    assert context.home.get_logo().is_displayed()

@when(u'Je clique sur le bouton Signup/Login')
def step_impl(context):
    context.menu.click_signup_login()

@then(u'New User Signup! est visible')
def step_impl(context):
    assert context.signup_login.get_titre_signup().is_displayed()

@when(u'Je mets le username et l\'email')
def step_impl(context):
    context.signup_login.fill_form_signup(context.table)

@when(u'Je clique sur le bouton Signup')
def step_impl(context):
    context.signup_login.click_signup()

@then(u'ENTER ACCOUNT INFORMATION est visible')
def step_impl(context):
    assert context.signup.get_titre().is_displayed()
    
@when(u'Je mets les informations d\'inscription')
def step_impl(context):
    context.signup.fill_form(context.table)

@when(u'Je clique sur le bouton Create ACCOUNT')
def step_impl(context):
    context.signup.click_create()

@then(u'ACCOUNT CREATED! est visible')
def step_impl(context):
    assert context.account_created.get_titre().is_displayed()

@when(u'Je clique sur le bouton Continue pour finaliser l\'inscription')
def step_impl(context):
    context.account_created.click_continue()

@then(u'Logged in as username est visible sur la page d\'accueil')
def step_impl(context):
    assert context.menu.get_username_logged().is_displayed()

@when(u'Je clique sur le bouton Delete Account')
def step_impl(context):
    context.menu.click_delete_account()

@then(u'ACCOUNT DELETED! est visible')
def step_impl(context):
    assert context.deleted_account.get_titre().is_displayed()

@then(u'Je clique sur le bouton Continue pour finaliser la suppression')
def step_impl(context):
    context.deleted_account.click_continue()