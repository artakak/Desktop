Feature: Project page

  Scenario: Go to project card
    Given I open main page
    When I click on main menu button
    And I click on portfolio menu point
    And I click on filter button on portfolio page
    And I can change complete filter in list
    And I choose target project from list
    Then I stay on information project page

  Scenario: Validate information project page
    Given I stay on information project page
    Then I see correct information project page

  Scenario: Validate documents project page
    Given I stay on project page
    When I click on documents button on project page
    Then I see correct documents project page

  Scenario: Go to mass project card
    Given I open main page
    When I click on main menu button
    And I click on mass portfolio menu point
    And I click on filter button on portfolio page
    And I can change inwork filter in list
    And I choose target project from list
    Then I stay on mass information project page

  Scenario: Validate mass information project page
    Given I stay on mass information project page
    Then I see correct mass information project page

  Scenario: Validate mass documents project page
    Given I stay on mass project page
    When I click on documents button on project page
    Then I see correct mass documents project page





