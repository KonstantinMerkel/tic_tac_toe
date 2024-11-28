class tictactoe:

    gameover = False
    game = [[None,None,None], [None,None,None], [None,None,None]]
    move = 'x'
    moved = 0
    won_by = None

    def __init__(self):
        print('Willkommen im Spiel')

    def make_move(self, x, y):
        game = self.game
        move = self.move

        if game[x][y] != None:  
            print('illegal move')
            return
        game[x][y] = move
        self.print_game()
        self.moved += 1
        self.gameover = self.winner()
        if self.gameover:
            self.won_by = move
        else: 
            self.gameover = self.stale_game()

        if move == 'x':
            self.move = 'o'
        else:
            self.move='x'

    
    def winner(self):
        game = self.game

        for x in range(3):
            if game[x] == ['x','x','x'] or game[x] == ['o','o','o']:
                return True
            elif game[0][x] == game[1][x] and game[1][x] == game[2][x] and game[2][x] != None:
                return True
        if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[2][2] != None:
            return True

        if game[0][2] == game[1][1] and game[1][1] == game[2][0]and game[2][0] != None:
            print('winner')
            return True


    def stale_game(self):
        game = self.game
        list3 = [
         [game[0][0], game[0][1], game[0][2]],
         [game[1][0], game[1][1], game[1][2]],
         [game[2][0], game[2][1], game[2][2]],
         [game[0][0], game[1][0], game[2][0]],
         [game[0][1], game[1][1], game[2][1]],
         [game[0][2], game[1][2], game[2][2]],
         [game[0][0], game[1][1], game[2][2]],
         [game[0][2], game[1][1], game[2][0]]
        ]
        for element in list3:
            if not 'x' in element or not 'o' in element:
                return False
        print('unentschieden niemand kann mehr gewinnen')
        return True



    def print_game(self):
        game = self.game
        move = self.move
        for x in range(3):
            one = game[x][0]
            two = game[x][1]
            three = game[x][2]
            print(f'\t {one} \t | \t {two} \t | \t {three}')
        print()
        
class point_counter:

    counter = [0,0]
    
    def __init__(self):
        counter = self.counter
    
    def addwin(self, winner):

        counter = self.counter

        if winner == 'x':
            counter[0] += 1
        elif winner == 'o':
            counter[1] += 1
    
    def print_gamecount(self):
        counter = self.counter
        print(f"x hat {counter[0]} mal gewonnen; o hat {counter[1]} mal gewonnen\n")


instance = tictactoe()
counter_instance = point_counter()
first_move = 'x'
print('gebe mit 1-3 die Zeile an und dann mit 1-3 die Spalte \n (1|1) | (1|2) | (1|3) \n (2|1) | (2|2) | (2|3) \n (3|1) | (3|2) | (3|3)')
while True:

    while(not instance.gameover):
        x = int(input('x: ')) - 1
        y = int(input('y: ')) - 1
        instance.make_move(x, y)

    rematch = input('Erneut spielen? (y/n)')

    if rematch.upper() =='N':
        break
    else:
        if instance.won_by == 'x':
            counter_instance.addwin('x')
        if instance.won_by == 'o':
            counter_instance.addwin('o')
        
        counter_instance.print_gamecount()
        print

        instance.game = [[None,None,None], [None,None,None], [None,None,None]]
        instance.gameover = False
        instance.moved = 0
        instance.won_by = None
        if first_move == 'x':
            instance.move = 'o' 
            first_move = 'o'
        elif first_move == 'o':
            instance.move = 'x' 
            first_move = 'x'
        print(f"Die neue Runde wird von {first_move} begonnen\n")
