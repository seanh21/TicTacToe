class TicTacToe:
    def __init__(self):
        self.list_dis = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.player1, self.player2 = self.init_game()
        self.win = False
        self.positions = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
        self.player1_pos = []
        self.player2_pos = []
        self.win_conditions = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22'], ['00', '10', '20'],
                               ['01', '11', '21'], ['02', '12', '22'], ['00', '11', '22'], ['03', '11', '30']]

    def display_print(self):
        for i in self.list_dis:
            print(f"{i[0]} {i[1]} {i[2]}")

    def player(self, symbol, pos_list):
        position = input(f"Choose a position Player {symbol}: ")
        if position in self.positions:
            if self.list_dis[int(position[0])][int(position[1])] == '-':
                self.list_dis[int(position[0])][int(position[1])] = symbol
                pos_list.append(position)
                self.display_print()
            else:
                print('Choose another position')
                self.player(symbol, pos_list)
        else:
            print("Choose a valid position")
            self.player(symbol, pos_list)

    def init_game(self):
        player1 = input("Player 1, Choose a symbol (X, O): ").upper()
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        return player1, player2

    def win_cond(self, pos_list):
        for i in self.win_conditions:
            if set(i).issubset(pos_list):
                return True

    def play_game(self):
        print('working')
        while not self.win:
            print('working1')
            self.player(self.player1, self.player1_pos)
            if self.win_cond(self.player1_pos):
                print("Player 1 wins")
                self.win = True
                break
            self.player(self.player2, self.player2_pos)
            if self.win_cond(self.player2_pos):
                print("Player 2 wins")
                self.win = True


game = TicTacToe()
game.display_print()
game.play_game()
