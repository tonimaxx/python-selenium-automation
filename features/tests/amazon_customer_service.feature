# Created by tonimaxx at 9/28/21
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: # Verify Customer Service’s page UI elements are present
    #Given Open Amazon main page
    #When Click flyout Signin button on main page
    #And Enter Email and Click continue
    When Open Amazon customer service page
    Then UI Element Title Text is founded
    Then UI Element Main Container is founded
    Then UI Element Search Input is founded
    Then UI Element Help Text is founded
    Then UI Element Support Container is founded
    Then UI Element Promo Image is founded
