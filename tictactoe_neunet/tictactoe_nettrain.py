import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
from sklearn.model_selection import train_test_split


def start_training(csv_file):
    ml = TicTacToeNetTrain()
    ml.train_deep_singleneuron(csv_file)
    ml.save_model()
    ml.save_weight()


class TicTacToeNetTrain:
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
        state_output = numpy.abs(game_states[:, 10:])

        self.net_model.add(Dense(90, input_dim=9, activation='relu'))  # hidden layer
        self.net_model.add(Dense(9, activation='sigmoid'))  # output layer
        # hinge loss function for target value set (-1,1)
        # self.net_model.compile(loss='hinge', optimizer='adam', metrics=['accuracy'])
        self.net_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.net_model.summary()
        self.net_model.fit(state_input, state_output, epochs=30, batch_size=500)
        # evaluate the model
        scores = self.net_model.evaluate(state_input, state_output)
        print("\n%s: %.2f%%" % (self.net_model.metrics_names[1], scores[1]*100))

    def train_deep_multineuron(self, csv_file):
        self.file_base = csv_file
        numpy.random.seed(7)
        game_states = numpy.loadtxt(csv_file+'.csv', delimiter=',')
        # expected input and output for neural net
        state_input = game_states[:, 0:9]
        state_output = numpy.abs(game_states[:, 10:])
        state_input_train, state_input_test, state_output_train, state_output_test = \
            train_test_split(state_input, state_output, test_size=0.4, random_state=0)
        state_input_train = state_input     # May be removed to avoid over-fitting
        state_output_train = state_output   # May be removed to avoid over-fitting

        self.net_model.add(Dense(180, input_dim=9, activation='relu'))  # hidden layer 1
        self.net_model.add(Dense(90, activation='relu'))  # hidden layer 2
        self.net_model.add(Dense(9, activation='softmax'))  # output layer
        # hinge loss function for target value set (-1,1), but only can be for single node output
        # self.net_model.compile(loss='hinge', optimizer='adam', metrics=['accuracy'])
        # categorical hinge loss function for target value set (-1,1) for multi-node output
        # self.net_model.compile(loss='categorical_hinge', optimizer='adam', metrics=['accuracy'])
        self.net_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.net_model.summary()
        self.net_model.fit(state_input_train, state_output_train, epochs=90, batch_size=500)
        # evaluate the model
        scores = self.net_model.evaluate(state_input_test, state_output_test)
        print("\n%s: %.2f%%" % (self.net_model.metrics_names[1], scores[1]*100))

    def train_deep_singleneuron(self, csv_file):
        self.file_base = csv_file
        numpy.random.seed(7)
        game_states = numpy.loadtxt(csv_file+'.csv', delimiter=',')
        # expected input and output for neural net
        state_input = game_states[:, 0:9]
        state_output = game_states[:, 10]
        state_input_train, state_input_test, state_output_train, state_output_test = \
            train_test_split(state_input, state_output, test_size=0.4, random_state=0)
        state_input_train = state_input     # May be removed to avoid over-fitting
        state_output_train = state_output   # May be removed to avoid over-fitting

        self.net_model.add(Dense(60, input_dim=9, activation='relu'))  # hidden layer 1
        self.net_model.add(Dense(60, activation='relu'))  # hidden layer 2
        self.net_model.add(Dense(60, activation='relu'))  # hidden layer 3
        self.net_model.add(Dense(60, activation='relu'))  # hidden layer 4
        self.net_model.add(Dense(60, activation='relu'))  # hidden layer 5
        self.net_model.add(Dense(60, activation='relu'))  # hidden layer 6
        self.net_model.add(Dense(1, activation='relu'))  # output layer
        # self.net_model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['accuracy'])
        self.net_model.compile(loss='logcosh', optimizer='adam', metrics=['accuracy'])
        self.net_model.summary()
        self.net_model.fit(state_input_train, state_output_train, epochs=140, batch_size=500)
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
