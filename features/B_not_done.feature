Feature: Not done page

  Scenario: Validate event list
    Given I open main page
    When I stay on "Not done" page
    Then I see last event with all attributes on Not done page

  Scenario: Go to enter result page
    Given I stay on "Not done" page
    When I check box with event
    And I click enter result button
    Then I stay on event page

  Scenario: Go to event page
    Given I stay on "Not done" page
    When I click on event title
    Then I stay on event page

  Scenario: Go to project page
    Given I stay on "Not done" page
    When I click on project title
    Then I stay on project page

  Scenario: Go to person page
    Given I stay on "Not done" page
    When I click on person title
    Then I stay on person page

  Scenario: Call main menu
    Given I stay on "Not done" page
    When I click on main menu button
    Then I see main menu page
    And I click on main menu button



