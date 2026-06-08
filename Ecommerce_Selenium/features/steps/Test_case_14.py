from selenium.webdriver.common.by import By
from behave import then, when


@when(u'Je clique sur le bouton Proceed to checkout')
def step_impl(context):
 context.cart.click_checkout()

@when(u'Je clique sur Register/Login de l\'alerte qui vient d\'apparaître')
def step_impl(context):
    context.cart.click_register_login() 

@then(u'Je vérifie que l\'adresse et les produits sont les bons')
def step_impl(context):
 # Vérifie les informations du client
 assert context.checkout.get_name_delivery().text == "Mr. Bob David"
 assert context.checkout.get_address_delivery().text == "3 rue des pain"
 assert context.checkout.get_city_delivery().text == "Cergy Val d'oise 95000"
 assert context.checkout.get_country_delivery().text == "Canada"
 assert context.checkout.get_phone_delivery().text == "0123654789"

 # Vérfie les produits
 for i, row in enumerate(context.table, start=1):
        assert context.cart.get_name(i).text  == row["name"]
        assert context.cart.get_price(i).text  == row["price"]
        assert context.cart.get_quantity(i).text  == row["quantity"]
        assert context.cart.get_total_price(i).text  == row["total price"]

@then(u'Je mets une description')
def step_impl(context):
    context.checkout.fill_description(context.table)

@when(u'Je clique sur le bouton Place order')
def step_impl(context):
    context.checkout.click_order()

@when(u'Je rentre les informations de paiements')
def step_impl(context):
    context.payment.fill_form(context.table)

@when(u'Je clique sur le bouton Pay and confirm')
def step_impl(context):
    context.payment.click_pay()

@then(u'Le message Your order has been placed successfully! est visible')
def step_impl(context):
    context.payment.get_success()