Feature: AI Decision Making
  If the next step cannot be decided by any scenarios listed
  in the basic_decision_making.feature, the logic in this feature
  file will be followed.

  Scenario: None scenario occurs in basic_decision_making
    Given condition 1
    When action 1
    Then assert 1

  Scenario: Find all executable moves
    Given condition 2
    When action 2
    Then assert 2

  Scenario: Find probabilities of all next moves
    Given condition 3
    When action 3
    Then assert 3

  Scenario: Find the best probability among all executable moves
    Given condition 4
    When action 4
    Then assert 4
