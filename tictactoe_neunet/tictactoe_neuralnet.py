from flask import Flask
from keras.models import model_from_json
# # Just disables the warning, doesn't enable AVX/FMA
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2

api = Flask(__name__)


def start_game(is_max):
    return


def get_next_move(opponent_move):
    return


class TicTacToePredict:
    def __init__(self):
        return

    def get_best_probability(self):
        # load json and create model
        json_file = open('tic-tac-toe-x-model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        # load weights into new model
        loaded_model.load_weights("tic-tac-toe-x-weight.h5")
        print("Loaded model from disk")

        # evaluate loaded model on test data
        # score = loaded_model.evaluate(X, Y, verbose=0)
        print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))
        ynew = model.predict(Xnew)
        ynew = model.predict_proba(Xnew)
        # show the inputs and predicted outputs
        for i in range(len(Xnew)):
            print("X=%s, Predicted=%s" % (Xnew[i], ynew[i]))