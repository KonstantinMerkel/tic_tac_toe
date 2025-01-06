class TicTacToe:
    def __init__(self):
        self.game = [[None, None, None], [None, None, None], [None, None, None]]
        self.move = 'x'
        self.gameover = False
        self.moved = 0
        self.won_by = None
        print('Willkommen im Spiel')

    def make_move(self, x, y):
        if self.game[x][y] is not None:
            print('Illegal move')
            return

        self.game[x][y] = self.move
        self.print_game()
        self.moved += 1
        self.gameover = self.winner()

        if self.gameover:
            self.won_by = self.move
            print(f'{self.move} has won the game')
        else:
            self.gameover = self.stale_game()

        # Switch player
        self.move = 'o' if self.move == 'x' else 'x'

    def winner(self):
        # Check rows and columns
        for x in range(3):
            if self.game[x] == ['x', 'x', 'x'] or self.game[x] == ['o', 'o', 'o']:
                return True
            elif self.game[0][x] == self.game[1][x] == self.game[2][x] and self.game[2][x] is not None:
                return True

        # Check diagonals
        if self.game[0][0] == self.game[1][1] == self.game[2][2] and self.game[2][2] is not None:
            return True
        if self.game[0][2] == self.game[1][1] == self.game[2][0] and self.game[2][0] is not None:
            return True

        return False

    def stale_game(self):
        # Check for a stale game (no winner and no empty spaces left)
        for row in self.game:
            if None in row:
                return False
        print('Unentschieden ')
        return True

    def print_game(self):
        for row in self.game:
            print(f"\t {' \t | '.join([str(cell) if cell else ' ' for cell in row])} \t")
        print()

class PointCounter:
    def __init__(self):
        self.counter = {'x': 0, 'o': 0}

    def add_win(self, winner):
        if winner in self.counter:
            self.counter[winner] += 1

    def print_game_count(self):
        print(f"x hat {self.counter['x']} mal gewonnen; o hat {self.counter['o']} mal gewonnen\n")

# Main game loop
instance = TicTacToe()
counter_instance = PointCounter()
first_move = 'x'

print('Gebe mit 1-3 die Zeile an und dann mit 1-3 die Spalte an:')
print("(1|1) | (1|2) | (1|3)\n(2|1) | (2|2) | (2|3)\n(3|1) | (3|2) | (3|3)")

while True:
    while not instance.gameover:
        try:
            x = int(input(f"{instance.move.upper()}: Gebe Zeile (1-3): ")) - 1
            y = int(input(f"{instance.move.upper()}: Gebe Spalte (1-3): ")) - 1
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Ungültige Eingabe. Wählen Sie eine Zahl zwischen 1 und 3.")
                continue
            instance.make_move(x, y)
        except ValueError:
            print("Ungültige Eingabe. Geben Sie bitte eine Zahl ein.")
    
    # After game is over
    if instance.won_by:
        counter_instance.add_win(instance.won_by)

    rematch = input('Erneut spielen? (y/n): ').strip().lower()
    if rematch == 'n':
        break

    counter_instance.print_game_count()

    # Reset game for rematch
    instance.game = [[None, None, None], [None, None, None], [None, None, None]]
    instance.gameover = False
    instance.moved = 0
    instance.won_by = None
    instance.move = 'o' if first_move == 'x' else 'x'
    first_move = instance.move

    print(f"Die neue Runde wird von {first_move.upper()} begonnen\n")