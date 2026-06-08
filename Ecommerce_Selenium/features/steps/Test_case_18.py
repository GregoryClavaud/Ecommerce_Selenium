from behave import then, when

@then(u'Les catégories sont visibles sur la side bar à gauche')
def step_impl(context):
    context.search_product.get_category().is_displayed()

@when(u'Je clique sur la catégorie Women')
def step_impl(context):
    context.search_product.click_women_category()


@when(u'Je clique sur la sous catégorie Tops')
def step_impl(context):
    context.search_product.click_sub_women_category(2)


@then(u'Le texte WOMEN - TOPS PRODUCTS est visible')
def step_impl(context):
    context.search_product.get_title_sub_category().text == "WOMEN - TOPS PRODUCTS"


@when(u'Je clique sur la catégorie Men')
def step_impl(context):
    context.search_product.click_men_category()


@when(u'Je clique sur la sous catégorie Tshirts')
def step_impl(context):
    context.search_product.click_sub_men_category(3)