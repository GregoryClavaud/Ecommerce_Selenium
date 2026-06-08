from behave import then, when


@when(u'J\'augmente la quantité à 4')
def step_impl(context):
    context.product_detail.add_quantity(4)


@when(u'Je clique sur le bouton Add to cart')
def step_impl(context):
    context.product_detail.click_add_cart()
    
@then(u'Je verifie mon panier contient la bonne quantité est de 4')
def step_impl(context):
    assert context.cart.get_quantity(1).text  == "4"