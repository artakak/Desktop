Feature: Project approval page

  Scenario: Go to approval
    Given I open main page
    When I click on main menu button
    And I click on project approval menu point
    Then I stay on project approval page

  Scenario: Scroll approval list
    Given I stay on project approval page
    When I scroll down list
    Then I see last event with all attributes on project approval page

  Scenario: Validate approval
    Given I stay on project approval page
    When I click on project approval
    Then I see project approval card with correct data

  Scenario: Approve project
    Given I stay on project approval page
    When I click on project card for approving
    And I click on approve button on project approval card
    Then I can fill approve project dialog

  Scenario: Reject project
    Given I stay on project approval page
    When I click on project card for rejecting
    And I click on reject button on project approval card
    Then I can fill reject project dialog

  Scenario: Approved list
    Given I stay on project approval page
    When I click on approved button on project approval page
    Then I see approved project

  Scenario: Rejected list
    Given I stay on project approval page
    When I click on rejected button on project approval page
    Then I see rejected project

  Scenario: Canceled list
    Given I stay on project approval page
    When I click on canceled button on project approval page
    Then I see canceled project





