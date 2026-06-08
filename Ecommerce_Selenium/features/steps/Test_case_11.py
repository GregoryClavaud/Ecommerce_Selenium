from behave import when


@when(u'Je clique sur le bouton Cart')
def step_impl(context):
    context.menu.click_cart()