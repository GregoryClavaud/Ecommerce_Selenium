from behave import when


@when(u'Je clique sur le bouton Test Cases')
def step_impl(context):
    context.home.click_test_cases()