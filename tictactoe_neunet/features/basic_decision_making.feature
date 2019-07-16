Feature: Basic Decision Making
  Some basic decisions in a board game can be check quickly without
  applying artificial intelligence. Such as checking winner and draw.

  Scenario: X is the winner
    Given a board state that 2 Xs in a row or diagonal
    |    state    |
    |X,O,X,X.O,,,,|
    |X,O,,O,X,X,,,|
    And X is the next player
    When X moves to one of the empty cells
    Then X becomes the winner

  Scenario: O is the winner
    Given a board state that 2 Os in a row or diagonal
    |    state    |
    |X,O,X,X.O,,,,|
    |X,O,,O,X,X,,,|
    And O is the next player
    When O moves to one of the empty cells
    Then O becomes the winner

  Scenario: Block X
    Given a board state that 2 Xs in a row or diagonal
    |    state    |
    |X,O,X,X.O,,,,|
    |X,O,,O,X,X,,,|
    And O is the next player
    When O moves to one of the empty cells
    Then X is forced to move to other cell

  Scenario: Block O
    Given a board state that 2 Os in a row or diagonal
    |    state    |
    |X,O,X,X.O,,,,|
    |X,O,,O,X,X,,,|
    And X is the next player
    When X moves to one of the empty cells
    Then O is forced to move to other cell

  Scenario: Game is draw
    Given a board state that only a cell open
    And either X or O is the next player
    When X or O moves to the only empty cell
    Then no winner is determined
