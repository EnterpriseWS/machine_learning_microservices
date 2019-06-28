from flask import Flask
from keras.models import model_from_json
# # Just disables the warning, doesn't enable AVX/FMA
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2

api = Flask(__name__)


def start_game(is_max):
    return


def get_next_move(opponent_move):
    ml = TicTacToePredict()
    ml.predict_by_matrix()
    return


def get_next_move_by_matrix(input_matrix):
    ml = TicTacToePredict()
    ml.predict_by_matrix(input_matrix)
    return


class TicTacToePredict:
    weight_file = ''
    model_file = ''

    def __init__(self):
        self.model_file = 'tic-tac-toe-x-model.json'
        self.weight_file = 'tic-tac-toe-x-weight.h5'
        return

    def __init__(self, model, weight):
        self.model_file = model
        self.weight_file = weight
        return

    def predict(self, input_array):
        return

    def predict_by_matrix(self, input_matrix):
        # load json and create model
        json_file = open(self.model_file, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        # load weights into new model
        loaded_model.load_weights(self.weight_file)
        print("Loaded model from disk")

        output_matrix = loaded_model.predict(input_matrix)
        # output_matrix = loaded_model.predict_proba(input_matrix)
        print(output_matrix)


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2:
        get_next_move_by_matrix(sys.argv[1])
    elif len(sys.argv) == 1:
        get_next_move_by_matrix('tic-tac-toe-x')
