Feature: Login
  Background: Navigate to login page
    Given  I launch Chrome browser
    And  I open https://todoist.com/pl
    And  I click "Zaloguj się"

  Scenario: Login with valid credentials
    Given I am on login page
    When I enter valid email
    And I enter valid password
    And I click "Log in" button
    Then I should be redirected to home page

  Scenario: Login with invalid credentials
    Given I am on login page
    When I enter invalid email "dmtesting8@gmail.com"
    And I enter invalid password "Admin123"
    And I click "Log in" button
    Then Message "Wrong email or password" is displayed

