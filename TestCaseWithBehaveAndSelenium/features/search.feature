Feature: Google searching

  Scenario: Searching dupa word
    Given Google homepage is open
    When Search word dupa is entered
    And Button search is clicked
    Then Webpage with results is visible
    And The following results are shown
      | related |
      | dupa1   |
      | dupa2   |
      | dupa3   |