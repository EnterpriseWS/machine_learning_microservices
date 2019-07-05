from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, null, Integer, String, JSON, DateTime
# -------------------------------------------
# TODO: Research why JSON db data type not working
# from sqlalchemy.dialects.sqlite import JSON
# -------------------------------------------
from datetime import date
import logging
import json
import csv

input_template = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00]
multioutput_template = [0, 0, 0, 0, 0, 0, 0, 0, 0]
singleoutput_template = [0]
x_sequence = [1, 3, 5, 7, 9]
o_sequence = [2, 4, 6, 8]
Base = declarative_base()
engine = create_engine('sqlite:///tic-tac-toe.db', echo=False)
Session = sessionmaker(bind=engine)


def extract_state_single_neuron(cvs_file, winner, begin_id, end_id):
    Base.metadata.create_all(engine)
    session = Session()
    counter = 0

    try:
        # Here game_state is equivalent to game_data variable in
        # heuristic_microservice
        game_states = session.query(GameState) \
            .filter(GameState.winner == winner
                    , GameState.id >= begin_id
                    , GameState.id <= end_id) \
            .order_by(GameState.id) \
            .all()
        for game_state in game_states:
            the_state = json.loads(str(game_state.state))
            step_count = len(the_state) - 1
            winner_sequence = []
            if winner == 'X':
                winner_sequence = x_sequence.copy()
            elif winner == 'O':
                winner_sequence = o_sequence.copy()
            for index in range(len(winner_sequence)):
                if the_state.get(str(winner_sequence[index])) is None:
                    break
                the_input = input_template.copy()
                the_output = singleoutput_template.copy()
                curr_move = winner_sequence[index]
                for sub_index in range(curr_move):
                    position_pair = the_state.get(str(sub_index+1))
                    if position_pair is None:
                        break
                    if curr_move == sub_index + 1:
                        # The most recent move in a state
                        # This is the move to be predicted and cannot be
                        # recorded as a previous move
                        # Prediction a.k.a. feature state
                        if position_pair[1] == 'X' or position_pair[1] == 'O':
                            the_output[0] = int(position_pair[0])
                    else:
                        # All previous moves
                        # Current state a.k.a. observal states
                        if position_pair[1] == 'X':
                            the_input[int(position_pair[0])-1] = 1
                        elif position_pair[1] == 'O':
                            the_input[int(position_pair[0])-1] = -1
                print('Row ID ' + str(game_state.id)
                      + ' convert to ' + str(the_input)
                      + ' output as ' + str(the_output))
                the_input.extend(the_output)
                with open(cvs_file, 'a') as csv_fd:
                    writer = csv.writer(csv_fd)
                    writer.writerow(the_input)
            counter += 1

    except:
        logging.error('convert_to_neural_input query() error: ', sys.exc_info()[0])

    session.close()
    print(str(counter) + ' data set has been converted.')


def extract_state_multiple_neuron(cvs_file, winner, begin_id, end_id):
    Base.metadata.create_all(engine)
    session = Session()
    counter = 0

    try:
        # Here game_state is equivalent to game_data variable in
        # heuristic_microservice
        game_states = session.query(GameState) \
            .filter(GameState.winner == winner
                    , GameState.id >= begin_id
                    , GameState.id <= end_id) \
            .order_by(GameState.id) \
            .all()
        for game_state in game_states:
            the_state = json.loads(str(game_state.state))
            step_count = len(the_state) - 1
            winner_sequence = []
            if winner == 'X':
                winner_sequence = x_sequence.copy()
            elif winner == 'O':
                winner_sequence = o_sequence.copy()
            for index in range(len(winner_sequence)):
                if the_state.get(str(winner_sequence[index])) is None:
                    break
                the_input = input_template.copy()
                the_output = multioutput_template.copy()
                curr_move = winner_sequence[index]
                for sub_index in range(curr_move):
                    position_pair = the_state.get(str(sub_index+1))
                    if position_pair is None:
                        break
                    if curr_move == sub_index + 1:
                        # The most recent move in a state
                        # This is the move to be predicted and cannot be
                        # recorded as a previous move
                        if position_pair[1] == 'X':
                            the_output[int(position_pair[0])-1] = 1
                        elif position_pair[1] == 'O':
                            the_output[int(position_pair[0])-1] = -1
                    else:
                        # All previous moves
                        if position_pair[1] == 'X':
                            the_input[int(position_pair[0])-1] = 1
                        elif position_pair[1] == 'O':
                            the_input[int(position_pair[0])-1] = -1
                print('Row ID ' + str(game_state.id)
                      + ' convert to ' + str(the_input)
                      + ' output as ' + str(the_output))
                the_input.extend(the_output)
                with open(cvs_file, 'a') as csv_fd:
                    writer = csv.writer(csv_fd)
                    writer.writerow(the_input)
            counter += 1

    except:
        logging.error('convert_to_neural_input query() error: ', sys.exc_info()[0])

    session.close()
    print(str(counter) + ' data set has been converted.')


class GameState(Base):
    __tablename__ = 'game_state'
    id = Column(Integer, primary_key=True)
    # state = Column(JSON)
    state = Column(String)
    winner = Column(String(1))
    create_datetime = Column(DateTime)

    def __init__(self, the_state, the_winner):
        self.state = the_state
        self.winner = the_winner
        self.create_datetime = date.today()


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 5:
        extract_state_single_neuron(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
    elif len(sys.argv) == 4:
        extract_state_single_neuron(sys.argv[1], sys.argv[2], int(sys.argv[3]), 99999999)
    else:
        print('Error: Please enter at least two argument')
