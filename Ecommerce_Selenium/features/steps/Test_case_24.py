from behave import then, when


@when(u'Je clique sur le Download Invoice')
def step_impl(context):
    context.order_placed.click_download()

@then(u'Je vérifie que le fichier est téléchargé')
def step_impl(context):
    context.order_placed.check_download()

@when(u'Je clique sur le bouton Continue pour poursuivre ma navigation')
def step_impl(context):
    context.order_placed.click_continue()