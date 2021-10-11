Feature: Google searching

  Scenario: Searching proba word
    Given Google homepage is open
    When Search word proba  is entered
    And Button search is clicked
    Then Webpage with results is visible
    And The following results are shown
      | related |
      | proba1  |
      | proba2  |
      | proba3  |