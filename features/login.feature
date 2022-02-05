Feature: Login
  Background: Navigate to login page
    Given  I launch Chrome browser
    And  I open https://todoist.com/pl
    And  I click "Zaloguj się"

  Scenario: Login with valid credentials
    Given I am on login page
    When I enter valid email and password
    And I click "Log in" button
    Then I should be redirected to home page

  Scenario Outline: Login with invalid credentials
    Given I am on login page
    When I enter invalid <email> and <password>
    And I click "Log in" button
    Then Error message is displayed

    Examples:

    | email                    | password   |
    | dmtesting8@gmail.com     | Admin123   |
    | xyz@email.com            | abc        |
    | xyzemail.com             | Admin123   |

