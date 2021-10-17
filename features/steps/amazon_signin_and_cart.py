from behave import given, when, then

@when('Click Amazon Orders link')
def click_orders(context):
    context.app.header.click_order_link()


@when('Click on cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()


@then('Verify Sign In page is opened')
def verify_signin(context):
    context.app.signin_page.verify_page_title()


@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_cart_empty(context):
    context.app.cart_page.verify_page_title()

