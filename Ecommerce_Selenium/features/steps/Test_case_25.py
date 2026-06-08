from behave import then, when


@when(u'Je clique sur la flèche située en bas à droite pour remonter')
def step_impl(context):
    context.home.click_arrow_up()

@then(u'Le texte Full-Fledged practice website for Automation Engineers est visible')
def step_impl(context):
    context.home.get_title_full_fledged().is_displayed()