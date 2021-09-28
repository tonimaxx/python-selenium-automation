# Created by tonimaxx at 9/28/21
Feature: # Test Scenarios for Amazon Best Sellers functionality


  Scenario: # Verify if number of Best Sellers link in the container
  # Sometime Amazon need does not open the Best Sellers page without credential
  # So, this solution is to sign in before testing the target
  # Can we open a test browser with packed credential Eg.Cookie, Session or Profile?
    Given Open Amazon main page
    When Click flyout Signin button on main page
    And Enter Email and Click continue
    And Open Amazon best sellers page
    Then There are 5 links is founded
