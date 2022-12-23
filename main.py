import copy
import random


class Game:
    def __init__(self, board_size=3):
        self.game_ongoing = True

        # the board is a list of columns
        self.board_size = board_size
        board_template = [[0 for i in range(board_size)] for j in range(board_size)]
        # board_list is a list of 2 board_templates
        self.board_list = [copy.deepcopy(board_template), copy.deepcopy(board_template)]

        self.turn = 0
        self.player_scores = [0, 0]

    def resolve_board(self):
        # move all 0s to the top of the board
        for i, board in enumerate(self.board_list):
            for j, _ in enumerate(board):
                zeros = board[j].count(0)

                for _ in range(zeros):
                    self.board_list[i][j].remove(0)

                for _ in range(zeros):
                    self.board_list[i][j].insert(0, 0)

        # sum all columns
        self.player_scores = [0, 0]
        for index, board in enumerate(self.board_list):
            for column in board:
                # frequency of each number in column
                column_frequency = [column.count(i) for i in range(1, 7)]
                for i, frequency in enumerate(column_frequency):
                    self.player_scores[index] += (i + 1) * pow(frequency, 2)

        # check if board is full
        self.game_ongoing = False
        for board in self.board_list:
            for column in board:
                if 0 in column:
                    self.game_ongoing = True

    def print_board(self):
        # loop through board_list
        for i, board in enumerate(self.board_list):
            # transpose board to a list of rows
            transposed_board = list(map(list, zip(*board)))

            print(f'p{i + 1}-------')
            for row in transposed_board:
                print(row)
        print('---------')

        # print scores
        print(f"Player 1 score: {self.player_scores[0]} \n"
              f"Player 2 score: {self.player_scores[1]} \n")

    def player_move(self, player):
        dice_roll = random.randint(1, 6)
        opponent = 1 if player == 0 else 0
        player_display = player + 1
        while True:
            try:
                print(f"Player {player_display} rolled a {dice_roll}")
                column_input = int(input(f"Player {player_display} please enter a column: ")) - 1

                if 0 not in self.board_list[player][column_input]:
                    print("Column is full, please choose another column")
                    continue

                self.board_list[player][column_input][self.board_list[player][column_input].index(0)] = dice_roll

                while dice_roll in self.board_list[opponent][column_input]:
                    # replace list value with dice_roll with 0
                    self.board_list[opponent][column_input][
                        self.board_list[opponent][column_input].index(dice_roll)] = 0

                self.turn = opponent
                break

            except ValueError:
                print("Please enter a number")
            except IndexError:
                print(f"Please enter a number between 1 and {self.board_size}")

    def play(self):
        while self.game_ongoing:
            self.resolve_board()
            self.print_board()
            self.player_move(self.turn)

        # winner check
        if self.player_scores[0] > self.player_scores[1]:
            print("Player 1 wins!")
        elif self.player_scores[1] > self.player_scores[0]:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
        print("Game over!")

    def reset_board(self):
        self.__init__()


if __name__ == '__main__':
    game = Game()
    game.play()
