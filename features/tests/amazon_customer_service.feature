Feature: Test Scenarios for Amazon Customer Service functionality

  Scenario: Verify Customer Service’s page UI elements are present
    When Open Amazon customer service page
    Then UI Element Title Text is founded
    Then UI Element Main Container is founded
    Then UI Element Search Input is founded
    Then UI Element Help Text is founded
    Then UI Element Support Container is founded
    Then UI Element Promo Image is founded
