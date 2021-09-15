# Created by Svetlana at 4/4/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input iphone13 into search field
    And Click on search icon
    Then Product results for iphone13 are shown
