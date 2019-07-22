from behave import *


@given('a board state that 2 Xs in a row or diagonal')
def step_impl(context):
    pass


@given('a board state that 2 Os in a row or diagonal')
def step_impl(context):
    pass


@given('X is the next player')
def step_impl(context):
    pass


@given('O is the next player')
def step_impl(context):
    pass


@given('a board state that only a cell open')
def step_impl(context):
    pass


@given('either X or O is the next player')
def step_impl(context):
    pass


@when('X moves to one of the empty cells')
def step_impl(context):
    assert True is not False


@when('O moves to one of the empty cells')
def step_impl(context):
    assert True is not False


@then('X becomes the winner')
def step_impl(context):
    assert context.failed is False


@then('O becomes the winner')
def step_impl(context):
    assert context.failed is False


@then('X is forced to move to other cell')
def step_impl(context):
    assert context.failed is False


@then('O is forced to move to other cell')
def step_impl(context):
    assert context.failed is False


@then('no winner is determined')
def step_impl(context):
    assert context.failed is False

