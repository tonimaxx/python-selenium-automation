# Created by tonimaxx at 11/16/21
Feature: Test Scenarios for Amazon that the user sees the deals when hovers over New Arrivals

  Scenario: Verify if deals appear when hovers over New Arrival
    Given Go to a product page Legendary-Whitetails-Berber-Hooded-Flannel/dp/B08T9YZD18
    When Hovers over New Arrivals
    Then New Arrivals Flyout appears