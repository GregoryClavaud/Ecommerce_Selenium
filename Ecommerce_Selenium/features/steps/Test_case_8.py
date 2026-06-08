from behave import then, when


@when(u'Je clique sur le bouton Products')
def step_impl(context):
    context.menu.click_products()


@then(u'La liste des produits est visible')
def step_impl(context):
    for product in context.list_products.get_list_products():
        # On travaille sur un élément de la liste
        assert context.list_products.get_product(product).is_displayed()


@when(u'Je clique sur View Product du premier produits')
def step_impl(context):
    context.list_products.click_view_product(1)


@then(u'Je vérifie que les détails du produit sont visibles')
def step_impl(context):
    #assert context.product_detail.get_name().text == context.table[0]["name"]
    assert context.product_detail.get_category() == context.table[0]["category"]
    assert context.product_detail.get_price().text == context.table[0]["price"]
    assert context.product_detail.get_availability() == context.table[0]["availability"]
    assert context.product_detail.get_condition() == context.table[0]["condition"]
    assert context.product_detail.get_brand() == context.table[0]["brand"]