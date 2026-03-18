Feature: Login Functionality
  As a user
  I want to login to the application
  So that I can purchase products

  Scenario: Successful login with valid credentials
    Given I open the login page
    when I enter valid username and password
    And I click the login button
    Then I should be redirected to the products page

  Scenario Outline: Failed login with invalid credentials
    Given I open the login page
    When I enter invalid username "<username>" and password "<password>"
    And I click the login button
    Then I should see an error message

    Examples:
      | username        | password      |
      | locked_out_user | secret_sauce  |
      | invalid_user    | invalid_pass  |
