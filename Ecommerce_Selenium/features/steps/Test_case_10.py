from behave import then, when


@when(u'Je scroll en bas de page')
def step_impl(context):
    context.home.scroll_to_bottom()


@then(u'SUBSCRIPTION est visible')
def step_impl(context):
    context.footer.get_titre().is_displayed()


@when(u'Je rentre un email')
def step_impl(context):
    context.footer.fill_form(context.table)


@when(u'Je clique sur la flèche à coté')
def step_impl(context):
    context.footer.click_subscribe()

@then(u'You have been successfully subscribed! est visible')
def step_impl(context):
    context.footer.get_success().is_displayed()