# Created by tonimaxx at 9/25/21
Feature: # Test Scenarios for Amazon Help Search functionality
  # User can search for solutions of Cancelling an order on Amazon

  Scenario: # Verifies if user can search for Cancelling an order
    Given Open Amazon help page
    When Search for Cancel orders
    Then Cancel orders is shown