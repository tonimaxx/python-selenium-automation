Feature: Test Scenarios for Amazon Best Sellers functionality

  Scenario: Verify if number of Best Sellers link in the container
    Given Open Amazon main page
    When Click flyout Signin button on main page
    And Enter Email and Click continue
    And Open Amazon best sellers page
    Then There are 5 links is founded
