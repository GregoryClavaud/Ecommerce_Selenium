from behave import then, when

@then(u'RECOMMENDED ITEMS est visible')
def step_impl(context):
    context.home.get_title_recommended_items().is_displayed()

@when(u'J\'ajoute le produit Stylish Dress dans le panier')
def step_impl(context):
    context.list_products.click_add_cart(4)
   