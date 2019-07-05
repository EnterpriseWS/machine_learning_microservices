import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn.model_selection import train_test_split


def start_training(csv_file):
    ml = TicTacToeNetTraining()
    ml.train_deep_multineuron(csv_file)
    ml.save_model()
    ml.save_weight()


class TicTacToeNetTraining:
    net_model = Sequential()
    file_base = ''

    def __init__(self):
        return

    def train_shallow_multineuron(self, csv_file):
        self.file_base = csv_file
        numpy.random.seed(7)
        game_states = numpy.loadtxt(csv_file+'.csv', delimiter=',')
        # expected input and output for neural net
        state_input = game_states[:, 0:9]
        state_output = game_states[:, 10:19]
        state_input_train, state_input_test, state_output_train, state_output_test = \
            train_test_split(state_input, state_output, test_size=0.4, random_state=0)

        self.net_model.add(Dense(90, input_dim=9, activation='relu'))  # hidden layer
        self.net_model.add(Dense(9, activation='tanh'))  # output layer
        self.net_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.net_model.summary()
        # Fit the model
        self.net_model.fit(state_input_train, state_output_train, epochs=30, batch_size=500)
        # evaluate the model
        scores = self.net_model.evaluate(state_input_test, state_output_test)
        print("\n%s: %.2f%%" % (self.net_model.metrics_names[1], scores[1]*100))

    def train_deep_multineuron(self, csv_file):
        self.file_base = csv_file
        numpy.random.seed(7)
        game_states = numpy.loadtxt(csv_file+'.csv', delimiter=',')
        # expected input and output for neural net
        state_input = game_states[:, 0:9]
        state_output = game_states[:, 10:]
        state_input_train, state_input_test, state_output_train, state_output_test = \
            train_test_split(state_input, state_output, test_size=0.4, random_state=0)

        self.net_model.add(Dense(90, input_dim=9, activation='relu'))  # hidden layer 1
        self.net_model.add(Dense(90, activation='relu'))  # hidden layer 2
        # self.net_model.add(Dense(90, activation='relu'))  # hidden layer 3
        self.net_model.add(Dense(9, activation='tanh'))  # output layer
        self.net_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.net_model.summary()
        # Fit the model
        self.net_model.fit(state_input_train, state_output_train, epochs=2, batch_size=500)
        # evaluate the model
        scores = self.net_model.evaluate(state_input_test, state_output_test)
        print("\n%s: %.2f%%" % (self.net_model.metrics_names[1], scores[1]*100))

    def save_model(self):
        model_json = self.net_model.to_json()
        with open(self.file_base + '-model.json', 'w') as json_file:
            json_file.write(model_json)

    def save_weight(self):
        self.net_model.save_weights(self.file_base + '-weight.h5')

    def __del__(self):
        keras.backend.clear_session()


if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 2:
        start_training(sys.argv[1])
    elif len(sys.argv) == 1:
        start_training('tic-tac-toe-x')
