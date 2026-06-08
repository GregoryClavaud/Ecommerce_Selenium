from behave import then, when

@then(u'Les marques sont visibles sur la side bar à gauche')
def step_impl(context):
    context.search_product.get_brand().is_displayed()

@when(u'Je clique sur la marque Polo')
def step_impl(context):
    context.search_product.click_sub_brand("Polo")


@when(u'Je clique sur la marque Babyhug')
def step_impl(context):
    context.search_product.click_sub_brand("Babyhug")