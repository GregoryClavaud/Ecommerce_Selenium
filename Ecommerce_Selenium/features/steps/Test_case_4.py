from behave import then, when


@when(u'Je clique sur le bouton Logout')
def step_impl(context):
    context.menu.click_logout()


@then(u'Je suis sur la page "{expected_url}"')
def step_impl(context, expected_url):
    assert context.driver.current_url == expected_url