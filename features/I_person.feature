Feature: Person page

  Scenario: Prepare person
    Given I open main page
    When I click on main menu button
    And I click on portfolio menu point
    And I click on target project title
    And I click on target person title
    Then I stay on information person page

  Scenario: Validate information person page
    Given I stay on information person page
    Then I see correct information person page

  Scenario: Validate document person page
    Given I stay on person page
    When I click on documents button on person page
    Then I see correct documents person page

  Scenario: Validate history person page
    Given I stay on person page
    When I click on history button on person page
    Then I see correct history person page




