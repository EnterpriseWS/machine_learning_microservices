Feature: AI Assisted Decision Flow
  If the next step cannot be decided by any scenarios listed
  in the basic_decision_making.feature, the logic in this feature
  file will be followed.

  Scenario: Not any of Xs basic decision flow scenarios is applicable
    Given a list of board states below after O moves
    | game |    state     |
    |  1   |X,O,X,O,,,O,X,|
    |  2   |O,X,O,,X,,,O,X|
    And X is the next player
    When start applying all scenarios of basic decisions to all available moves
    Then none of the Xs basic decision scenarios applies

  Scenario: Not any of Os basic decision flow scenarios is applicable
    Given a list of board states below after X moves
    | game |     state     |
    |  1   |O,X,X,X,O,O,,,X|
    |  2   |X,,,O,,X,X,,O  |
    And O is the next player
    When start applying all scenarios of basic decisions to all available moves
    Then none of the Os basic decision scenarios applies

  Scenario: Find the best probability of Xs available moves
    Given none of the Xs basic decision scenarios applies
    And X is the next player
    When find X probability of all available moves
    Then get the best X move

  Scenario: Find the best probability of Os available moves
    Given none of the Os basic decision scenarios applies
    And O is the next player
    When find O probability of all available moves
    Then get the best O move
