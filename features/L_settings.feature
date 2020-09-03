Feature: Settings page

  Scenario: Go to settings
    Given I open main page
    When I click on main menu button
    And I click on settings menu point
    Then I see all points of settings

  Scenario: Change Language
    When I stay on settings page
    And I click on change language point
    Then I see russian menu

  Scenario: Validate counts
    When I click on main menu button
    Then I see all counts are correct