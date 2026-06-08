from behave import then, when


@when(u'J\'ajoute le produit Sleeveless Dress dans le panier')
def step_impl(context):
    context.list_products.click_add_cart(3)

@when(u'J\'ajoute le produit Winter Top dans le panier')
def step_impl(context):
    context.list_products.click_add_cart(5)

@then(u'Je vérifie que l\'adresse de livraison est la même que celle enregistrée')
def step_impl(context):
    assert context.checkout.get_name_delivery().text == "Mr. Bob David"
    assert context.checkout.get_address_delivery().text == "3 rue des pain"
    assert context.checkout.get_city_delivery().text == "Cergy Val d'oise 95000"
    assert context.checkout.get_country_delivery().text == "Canada"
    assert context.checkout.get_phone_delivery().text == "0123654789"


@then(u'Je vérifie que l\'adresse de paiement est la même que celle enregistrée')
def step_impl(context):
    assert context.checkout.get_name_bill().text == "Mr. Bob David"
    assert context.checkout.get_address_bill().text == "3 rue des pain"
    assert context.checkout.get_city_bill().text == "Cergy Val d'oise 95000"
    assert context.checkout.get_country_bill().text == "Canada"
    assert context.checkout.get_phone_bill().text == "0123654789"