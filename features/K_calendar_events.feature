Feature: Calendar events page

  Scenario: Go to events
    Given I open main page
    When I click on main menu button
    And I click on events menu point
    Then I stay on events page

  Scenario: Select user
    Given I stay on events page
    When I click select user button on calendar page
    Then I can select user

  Scenario: Create calendar event
    Given I stay on events page
    When I click on create event button on calendar page
    Then I stay on create calendar event dialog page
    And I can create new calendar event

  Scenario: Validate planer list
    Given I stay on events page
    Then I see correct list of planer events

  Scenario: Validate contact list
    Given I stay on events page
    When I select contact filter
    Then I see correct list of contact events

  Scenario: Validate meeting list
    Given I stay on events page
    When I select meeting filter
    Then I see correct list of meeting events

  Scenario: Validate private list
    Given I stay on events page
    When I select private filter
    Then I see correct list of private events

  Scenario: Create low priority task
    Given I stay on events page
    When I click create task button on tasks page
    Then I stay on create task dialog page
    And I can create new low priority task

  Scenario: Create medium priority task
    Given I stay on events page
    When I click create task button on tasks page
    Then I stay on create task dialog page
    And I can create new medium priority task

  Scenario: Create high priority task
    Given I stay on events page
    When I click create task button on tasks page
    Then I stay on create task dialog page
    And I can create new high priority task

  Scenario: Validate tasks list
    Given I stay on events page
    Then I see correct list of tasks




