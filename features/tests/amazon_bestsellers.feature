Feature: Test Scenarios for Amazon Best Sellers functionality

  Scenario: Verify if number of Best Sellers link in the container
    Given Open Amazon best sellers page
    Then There are 5 links is founded

  Scenario: Verify all Best Sellers links open correct target pages
    Given Open Amazon best sellers page
    Then All Best Sellers links open correct target pages