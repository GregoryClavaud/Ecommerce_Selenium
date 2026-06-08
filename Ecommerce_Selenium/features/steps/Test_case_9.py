from behave import then, when


@when(u'Je rentre le nom du produit recherché')
def step_impl(context):
    context.search_product.fill_search(context.table)


@when(u'Je clique sur le bouton Search')
def step_impl(context):
    context.search_product.click_search()


@then(u'SEARCHED PRODUCTS est visible')
def step_impl(context):
    context.search_product.get_titre().is_displayed()