from behave import then, when

@when(u'J\'ajoute le produit Men Tshirt')
def step_impl(context):
    context.list_products.click_add_cart(2)


@when(u'J\'ajoute le produit Pure Cotton V-Neck T-Shirt')
def step_impl(context):
    context.list_products.click_add_cart(28)