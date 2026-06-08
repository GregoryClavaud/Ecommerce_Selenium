from behave import then, when
from behave.api.pending_step import StepNotImplementedError
@when(u'Je clique sur le bouton Contact US')
def step_impl(context):
    context.menu.click_contact()

@then(u'GET IN TOUCH est visible')
def step_impl(context):
    assert context.contact.get_titre_form().is_displayed()

@when(u'Je mets mes informations à transmettre')
def step_impl(context):
    context.contact.fill_form(context.table)

@when(u'J\'upload un fichier')
def step_impl(context):
    context.contact.upload_file()

@when(u'Je clique sur le bouton Submit')
def step_impl(context):
    context.contact.click_submit()

@when(u'Sur le bouton OK sur la fenêtre qui vient d\'apparaître')
def step_impl(context):
    context.contact.accept_alert()

@then(u'Le message Success! Your details have been submitted successfully est visible')
def step_impl(context):
    context.contact.get_success().is_displayed()

@when(u'Je clique sur le bouton Home')
def step_impl(context):
    context.contact.click_home()