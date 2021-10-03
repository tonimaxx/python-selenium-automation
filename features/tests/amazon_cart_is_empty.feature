Feature: Test Scenarios for Amazon Cart functionality
  # test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Amazon Cart is empty.

  Scenario: Verifies that Amazon Cart is empty
    Given Open Amazon main page
    When Click on cart icon
    Then Cart is empty


