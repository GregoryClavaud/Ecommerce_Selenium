from behave import then, when

@then(u'Write Your Review est visible')
def step_impl(context):
    context.product_detail.get_title_review().is_displayed


@when(u'Je rentre le nom du client, l\'email et une Review')
def step_impl(context):
    context.product_detail.fill_review(context.table)
    
@when(u'Je valide la review en cliquant sur le bouton Submit')
def step_impl(context):
    context.product_detail.click_submit()

@then(u'Thank you for your review est visible')
def step_impl(context):
    context.product_detail.get_message_success_review().is_displayed