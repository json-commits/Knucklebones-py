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
        self.player1_score = 0
        self.player2_score = 0

    def resolve_board(self):
        # sum all columns
        # check if board is full
        # -if full, check who has the highest score

        pass

    def print_board(self):
        # loop through board_list
        for board in self.board_list:
            # transpose board to a list of rows
            transposed_board = list(map(list, zip(*board)))

            print('---------1')
            for row in transposed_board:
                print(row)
        print('---------2')

        # print scores
        print(f"Player 1 score: {self.player1_score} \n"
              f"Player 2 score: {self.player2_score}")

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
        if self.player1_score > self.player2_score:
            print("Player 1 wins!")
        elif self.player2_score > self.player1_score:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
        print("Game over!")

    def reset_board(self):
        self.__init__()


if __name__ == '__main__':
    game = Game()
    game.play()
