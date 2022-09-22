#Create two classes that inherit from another class.
    #each child should have at least two of their own attributes.
    #The parent class should have at least one method (function).
    #Both child classes should utilize polymorphism on the parent class method.
    #Add comments throughout your Python explaining your code.

#Parent class
class game:
    Type = 'card game'
    name = 'Poker'
    Max_Players = 8

    def information(self):
        msg = "\nPoker can be played with a total of {} players".format(self.Max_Players)
        return msg

# child class instance

class board_game:
    Type = 'board game'
    name = 'Catan'
    Max_Players = 6
    Duration: 'Hours'


class sports_game:
    Type = 'Physical Sport'
    name = 'Basketball'
    Max_Players = 10
    Exercise = True
    


if __name__ == "__main__":
    game = game()
    print(game.information())
