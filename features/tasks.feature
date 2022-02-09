Feature: Managing tasks
  Background: Log into the app
    Given I am on https://todoist.com/pl
    When I click "Zaloguj się"
    And I enter valid email and password
    And I click "Log in" button

  Scenario: Add Task
    Given I am on home page
    When I click "+Add task"
    And Enter Sample task and schedule it
    And Click "Add Task"
    Then The Sample task is added

  Scenario: Edit task
    Given I am logged in and there is a task in the inbox
    When I click "Edit task"
    And Change text to Updated task
    And I click "Save"
    Then The task is changed to Updated task

