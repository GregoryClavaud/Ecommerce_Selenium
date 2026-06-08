from behave import then, when


@when(u'Je clique sur le bouton Add to cart du premier produit')
def step_impl(context):
    context.list_products.click_add_cart(1)

@when(u'Sur le bouton Continue Shopping')
def step_impl(context):
    context.list_products.click_continue_shopping()

@when(u'Je clique sur le bouton Add to cart du second produit')
def step_impl(context):
    context.list_products.click_add_cart(2)
    
@when(u'Je clique sur le bouton View Cart')
def step_impl(context):
    context.list_products.click_view_cart()

@then(u'Je verifie mon panier')
def step_impl(context):
    for row in context.table:
        product_id = row['id'] 
        # Comparaison entre le site et la table du feature
        assert context.cart.get_name(product_id).text.strip() == row['name']
        assert context.cart.get_price(product_id).text.strip() == row['price']
        assert context.cart.get_quantity(product_id).text.strip() == row['quantity']
        assert context.cart.get_total_price(product_id).text.strip() == row['total price']