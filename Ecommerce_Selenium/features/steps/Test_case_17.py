from behave import then, when


@when(u'Je clique sur la croix pour vider mon panier')
def step_impl(context):
    context.cart.click_delete_all_products()


@then(u'Mon panier est vide')
def step_impl(context):
    context.cart.get_empty().is_displayed()