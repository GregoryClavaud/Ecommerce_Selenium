import time
from behave import then, when

@then (u'Login to your account est visible')
def step_impl(context):
    assert context.signup_login.get_titre_login().is_displayed()
    
@when(u'Je mets un email et un mot de passe correct')
def step_impl(context):
    context.signup_login.fill_form_login(context.table)

@when(u'Je clique sur le bouton Login')
def step_impl(context):
    context.signup_login.click_login()