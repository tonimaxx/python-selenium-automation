from behave import given, when, then


@when('Sign in with credential')
def sign_in(context):
    context.app.header.sign_in()


@when('Search and add a product')
def search_and_add_product(context):
    context.app.header.search_and_add_product()


@then('Cart is not empty')
def verify_if_cart_is_not_empty(context):
    context.app.cart_page.verify_if_cart_is_not_empty()
