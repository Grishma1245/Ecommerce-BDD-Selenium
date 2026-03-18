Feature: Checkout Process
  As a user with items in my cart
  I want to complete the checkout process
  So that I can place my order

  Background:
    Given I am logged in as a standard user
    And I have added the "Sauce Labs Backpack" to my cart

  Scenario: Successful checkout with valid information
    Given I am on the checkout information page
    When I fill in my personal information
    And I continue to the checkout overview
    And I finish the checkout
    Then I should see a success message "Thank you for your order!"
