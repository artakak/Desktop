Feature: Portfolio page

  Scenario: Go to portfolio
    Given I open main page
    When I click on main menu button
    And I click on portfolio menu point
    Then I stay on portfolio page

  Scenario: Haven't worksheet
    Given I stay on portfolio page
    When I click on request project title
    Then I see haven't worksheet message

  Scenario: Scroll portfolio list
    Given I stay on portfolio page
    When I scroll down list
    Then I see last project on portfolio page

  Scenario: Change responsibility user
    Given I stay on portfolio page
    When I change user in list
    Then I see project of this user in list

  Scenario: Validate request filter
    Given I stay on portfolio page
    When I click on filter button on portfolio page
    Then I can change request filter in list
    And I see request projects in list

  Scenario: Validate inwork filter
    Given I stay on portfolio page
    When I click on filter button on portfolio page
    Then I can change inwork filter in list
    And I see inwork projects in list

  Scenario: Validate frozen filter
    Given I stay on portfolio page
    When I click on filter button on portfolio page
    Then I can change frozen filter in list
    And I see frozen projects in list

  Scenario: Validate complete filter
    Given I stay on portfolio page
    When I click on filter button on portfolio page
    Then I can change complete filter in list
    And I see complete projects in list

  Scenario: Validate cancelled filter
    Given I stay on portfolio page
    When I click on filter button on portfolio page
    Then I can change cancelled filter in list
    And I see cancelled projects in list

  Scenario: Validate archived filter
    Given I stay on portfolio page
    When I click on filter button on portfolio page
    Then I can change archived filter in list
    And I see archived projects in list

  Scenario: Settings page
    Given I stay on portfolio page
    When I click on settings button on portfolio page
    Then I stay on portfolio settings page

    Scenario: Go to mass portfolio
    When I click on main menu button
    And I click on mass portfolio menu point
    Then I stay on mass portfolio page

  Scenario: Haven't worksheet mass
    Given I stay on mass portfolio page
    When I click on mass request project title
    Then I see haven't worksheet message

  Scenario: Change responsibility user mass
    Given I stay on mass portfolio page
    When I change user in list
    Then I see project of this user in mass list

  Scenario: Validate mass request filter
    Given I stay on mass portfolio page
    When I click on filter button on portfolio page
    Then I can change request filter in list
    And I see mass request projects in list

  Scenario: Validate mass inwork filter
    Given I stay on mass portfolio page
    When I click on filter button on portfolio page
    Then I can change inwork filter in list
    And I see mass inwork projects in list

  Scenario: Validate mass frozen filter
    Given I stay on mass portfolio page
    When I click on filter button on portfolio page
    Then I can change frozen filter in list
    And I see mass frozen projects in list

  Scenario: Validate mass complete filter
    Given I stay on mass portfolio page
    When I click on filter button on portfolio page
    Then I can change complete filter in list
    And I see mass complete projects in list

  Scenario: Validate mass cancelled filter
    Given I stay on mass portfolio page
    When I click on filter button on portfolio page
    Then I can change cancelled filter in list
    And I see mass cancelled projects in list

  Scenario: Validate mass archived filter
    Given I stay on mass portfolio page
    When I click on filter button on portfolio page
    Then I can change archived filter in list
    And I see mass archived projects in list





