Feature: Sing in of Venu Booking

  Scenario Outline: Sing in of Venu Booking
    Given I goto to website "http://52.221.165.78/venue/"
    When I open 'LOGIN'
    Then Pop up window 'modal-content' appears
    And I enter <email> in 'login_email' by 'id'
    And I enter <password> in 'login_password' by 'id'
    And I tap 'Login'
    Then I should see success message
    Examples:
      | email                       | password |
      | 3mnire.be@p4tlfsdfggg69q.gq | eg       |
      | aniasldud@miegrg.ga         | 12345    |
      | #@%^%$@#$@#.com             | 12345    |
      | あいうえお@dmain.com             | 12345    |
      | email@-doain.com            | 12345    |
      | <joesmith@exmple.com>       | 12345    |
      | plainaddess                 | 12345    |
      | @domin.com                  | 12345    |
      | email.omain.com             | 12345    |
      | email@doain@domain.com      | 12345    |
      | email@111.22.333.44444      | abc      |
      | email@doain..com            | 12345    |
      | email@doain                 | 12345    |
      | (empty)                     | 12345    |
      | email@doain                 | (empty)  |