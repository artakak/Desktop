Feature: WorkSheet page

  Scenario: Prepare worksheet
    Given I open main page
    When I click on main menu button
    And I click on portfolio menu point
    And I click on target project title
    Then I stay on worksheet page

  Scenario: Scroll worksheet list
    Given I stay on worksheet page
    When I scroll down list
    Then I see last people on worksheet page

 Scenario: Validate candidate filter
    Given I stay on worksheet page
    When I click on filter button on worksheet page
    Then I can change candidate filter in list on worksheet page
    And I see candidate people in list

  Scenario: Validate applicant filter
    Given I stay on worksheet page
    When I click on filter button on worksheet page
    Then I can change applicant filter in list on worksheet page
    And I see applicant people in list

  Scenario: Validate out_applicant filter
    Given I stay on worksheet page
    When I click on filter button on worksheet page
    Then I can change out applicant filter in list on worksheet page
    And I see out_applicant people in list

  Scenario: Validate employed filter
    Given I stay on worksheet page
    When I click on filter button on worksheet page
    Then I can change employed filter in list on worksheet page
    And I see employed people in list

  Scenario: Validate finalist filter
    Given I stay on worksheet page
    When I click on filter button on worksheet page
    Then I can change finalist filter in list on worksheet page
    And I see finalist people in list

  Scenario: Prepare mass worksheet
    Given I open main page
    And I click on main menu button
    And I click on mass portfolio menu point
    And I click on target mass project title
    Then I stay on mass worksheet page

  Scenario: People to next stage
    Given I stay on mass worksheet page
    When I check box with event
    And I click on stage button on worksheet page
    Then I can fill change stage dialog
    And I see mass people on next stage

  Scenario: Settings page
    Given I stay on mass worksheet page
    When I click on settings button on portfolio page
    Then I stay on worksheet settings page





