Feature: Test Scenarios for Amazon adding to cart functionality

  # test case to add any product you want into the cart, and make sure it’s there
  # Version 2 - Page Object Model

  # Precondition
  #   - User has an Amazon credential already
  #   - User has not signed-in

  Scenario: Verifies that user can add a product to cart
    Given Open Amazon main page
    When Sign in with credential
    And Search and add a product
    Then Cart is not empty




