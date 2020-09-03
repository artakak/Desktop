Feature: Auth

  Scenario: Login without password
    Given I stay on login screen
    When I fill "Username" without "Password"
    And I click on "Login" button
    Then I see "Validate" message

  Scenario: Incorrect login data
    Given I stay on login screen
    When I fill incorrect "Username" and "Password"
    And I click on "Login" button
    Then I see "Incorrect" message

  Scenario: Got a captcha
    When I click on "Login" button 5 times
    Then I see "Captcha" message

  Scenario: Forgot password
    Given I stay on login screen
    When I click on forgot link
    Then I stay on recovery screen

  Scenario: Send recovery mail
    Given I stay on recovery screen
    When I fill email field
    And I click reset button
    Then I see success message

  Scenario: Check recovery link
    Given I open recovery link
    When I enter same password
    And I click reset button
    Then I see same password message

  Scenario: Correct login data
    Given I stay on login screen
    When I fill correct "Username" and "Password"
    And I click on "Login" button
    And I enable push option
    Then I stay on "Not done" page

