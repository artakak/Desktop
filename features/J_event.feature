Feature: Event page

  Scenario: Prepare event
    Given I open main page
    When I click on main menu button
    And I click on portfolio menu point
    And I click on target project title
    Then I stay on worksheet page

  Scenario: Create conversation event
    Given I stay on worksheet page
    When I check box with event
    And I click new event button
    Then I stay on create event dialog page
    And I can create new conversation event

  Scenario: Create reference check event
    Given I stay on worksheet page
    When I check box with event
    And I click new event button
    Then I stay on create event dialog page
    And I can create new reference check event

  Scenario: Create interview with line manager event
    Given I stay on worksheet page
    When I check box with event
    And I click new event button
    Then I stay on create event dialog page
    And I can create new interview event

  Scenario: Create interview with recruter event
    Given I stay on worksheet page
    When I check box with event
    And I click new event button
    Then I stay on create event dialog page
    And I can create new interview with recruter event

  Scenario: Create custom event
    Given I stay on worksheet page
    When I check box with event
    And I click new event button
    Then I stay on create event dialog page
    And I can create new custom event

  Scenario: Edit conversation event
    Given I stay on worksheet page
    When I click on conversation event title
    Then I stay on conversation event page
    And I can edit this event

  Scenario: Enter result of conversation event
    Given I stay on worksheet page
    When I click on conversation event title
    And I click on enter result button
    And I enter conversation result
    Then I see all correct data on conversation event page

  Scenario: Enter result of reference check event
    Given I stay on worksheet page
    When I click on reference check event title
    And I click on enter result button
    And I enter reference check result
    Then I see all correct data on reference check event page

  Scenario: Enter result of interview with line manager event
    Given I stay on worksheet page
    When I click on interview event title
    And I click on enter result button
    And I enter interview result
    Then I see all correct data on interview event page

  Scenario: Enter result of interview with recruter event
    Given I stay on worksheet page
    When I click on interview with recruter event title
    And I click on enter result button
    And I enter interview with recruter result
    Then I see all correct data on interview with recruter event page

  Scenario: Enter result of custom event
    Given I stay on worksheet page
    When I click on custom event title
    And I click on enter result button
    And I enter custom result
    Then I see all correct data on custom event page



