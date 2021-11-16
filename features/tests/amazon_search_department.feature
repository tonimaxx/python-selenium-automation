# Created by tonimaxx at 11/16/21
Feature: Test Scenarios for Amazon search for an item in a different Amazon department

  Scenario Outline: Verifies if user can search in a different department
    Given Open Amazon page
    When Select department <departmentToTest>
    When Search product <productToTest>
    Then Verify search result page is displayed
    Examples:
    | departmentToTest  | productToTest  |
    | Books             | Harry Potter  |
    | Alexa Skills      | Crypto        |
    | Appliances        | vacuum cleaner robot |
    | Digital Music     | Ed sheeran    |
    | Video Games       | Mario         |
    | Video Games       | Pokemon       |
    | Video Games       | Pacman        |
    | Video Games       | Final Fantasy |