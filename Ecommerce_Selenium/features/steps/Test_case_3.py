from behave import then, when


@when(u'Je mets un email et un mot de passe incorrect')
def step_impl(context):
    context.signup_login.fill_form_login(context.table)

@then(u'Le message Your email or password is incorrect! est visible')
def step_impl(context):
    assert context.signup_login.get_message_erreur_login().is_displayed()