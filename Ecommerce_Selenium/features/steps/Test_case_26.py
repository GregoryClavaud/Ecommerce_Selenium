import time
from behave import when

@when(u'Je scroll en haut de page')
def step_impl(context):
    time.sleep(1)
    context.home.scroll_to_top()