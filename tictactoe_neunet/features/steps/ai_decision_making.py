from behave import *


@given('condition 1')
def step_impl(context):
    pass


@when('action 1')
def step_impl(context):
    assert True is not False


@then('assert 1')
def step_impl(context):
    assert context.failed is False
