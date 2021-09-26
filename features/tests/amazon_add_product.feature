Feature: Test Scenarios for Amazon adding to cart functionality

  # test case to add any product you want into the cart, and make sure it’s there

  # Precondition
  #   - User has an Amazon credential already
  #   - User has not signed-in

  Scenario: Verifies that user can add a product to cart
    Given Open Amazon main page
    When Click flyout Signin button on main page
    And Enter Email and Click continue
    And Search and add a product
    Then Cart is not empty


