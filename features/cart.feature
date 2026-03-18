Feature: Shopping Cart
  As a logged-in user
  I want to add products to my cart
  So that I can purchase them later

  Background:
    Given I am logged in as a standard user

  Scenario: Add a single item to the cart
    When I add the "Sauce Labs Backpack" to my cart
    Then the cart badge should show "1" item
    And the cart page should display the "Sauce Labs Backpack"

  Scenario: Remove an item from the cart
    Given I have added the "Sauce Labs Bike Light" to my cart
    When I remove the "Sauce Labs Bike Light" from the cart
    Then the cart badge should be empty
    And the cart page should not display the "Sauce Labs Bike Light"
