Feature: Requests page

  Scenario: Go to requests
    Given I open main page
    When I click on main menu button
    And I click on requests menu point
    Then I stay on requests page

  Scenario: Validate requests list
    Given I stay on requests page
    When I scroll down list
    Then I see last event with all attrubutes on Requests page

  Scenario: Approved list
    Given I stay on requests page
    When I click on approved button on Requests page
    Then I see approved requests

  Scenario: Rejected list
    Given I stay on requests page
    When I click on rejected button on Requests page
    Then I see rejected requests

  Scenario: Go to send request page
    Given I stay on requests page
    When I click on main menu button
    And I click on send requests menu point
    Then I stay on create request page

  Scenario: Send new request
    Given I stay on create request page
    When I fill all fields on create request page
    And I click send request button on create request page
    Then I stay on requests page
    And I see my new request in list

  Scenario: Validate request
    Given I stay on requests page
    When I open my new request
    Then I stay on my request page
    And All fields are correct

  Scenario: Cancel request
    Given I stay on my request page
    When I click on delete button on request page
    Then I can fill delete request dialog

  Scenario: Canceled list
    Given I stay on requests page
    When I click on canceled button on Requests page
    Then I see canceled requests



