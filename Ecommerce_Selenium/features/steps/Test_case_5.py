from behave import then, when


@when(u'Je mets le username et l\'email d\'un compte existant')
def step_impl(context):
    context.signup_login.fill_form_signup(context.table)

@then(u'Le message Email Address already exist! est visible')
def step_impl(context):
    assert context.signup_login.get_message_erreur_signup().is_displayed()