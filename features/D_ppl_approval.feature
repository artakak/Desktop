Feature: People approval page

  Scenario: Go to approval
    Given I open main page
    When I click on main menu button
    And I click on people approval menu point
    Then I stay on people approval page

  Scenario: Validate approval list
    Given I stay on people approval page
    When I click second pagination page
    Then I see last event with all attributes on people approval page

  Scenario: Validate approval
    Given I stay on people approval page
    When I click on people approval
    Then I see people approval card with correct data

  Scenario: Approve people
    Given I stay on people approval page
    When I click on people card for approving
    And I click on approve button on people approval card
    Then I can fill approve people dialog

  Scenario: Reject people
    Given I stay on people approval page
    When I click on people card for rejecting
    And I click on reject button on people approval card
    Then I can fill reject people dialog

  Scenario: Approved list
    Given I stay on people approval page
    When I click on approved button on people approval page
    Then I see approved people

  Scenario: Rejected list
    Given I stay on people approval page
    When I click on rejected button on people approval page
    Then I see rejected people

  Scenario: Canceled list
    Given I stay on people approval page
    When I click on canceled button on people approval page
    Then I see canceled people





