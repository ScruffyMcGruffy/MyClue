
import random 

class GamePlay():
    def intro(self):
       # print(self.dictionary_of_suspects)
        print(self.whodunit)
        print(self.murder_weapon)
        print(self.victim)
        print(self.kill_room)

    def __init__(self):
        self.list_of_weapons = ['knife', 'pipe', 'rope', 'axe', 'katana', '1,000 trained bees']
        self.list_of_rooms = ['kitchen','basement', 'living room', 'dining room', 'entrance hall']
        self.current_player = 0
        self.list_of_suspects = ['Mr.Penguin', 'Ms.Hicks', 'Dr.Walter', 'Marvin', 'Dr. Rowan Marshall PhD', 'Andres Perez']

        self.dictionary_of_suspects = {'Suspect 1': self.list_of_suspects[0],'Suspect 2': self.list_of_suspects[1], 'Suspect 3': self.list_of_suspects[2], 'Suspect 4': self.list_of_suspects[3],'Suspect 5': self.list_of_suspects[4], 'Suspect 6': self.list_of_suspects[5]}
        self.whodunit = {'Criminal': self.list_of_suspects.pop(random.randrange(0, len(self.list_of_suspects)))}
        self.victim ={'Dead body': self.list_of_suspects.pop(random.randrange(0,len(self.list_of_suspects)))}
        self.dictionary_of_weapons = {'Weapon 1' : self.list_of_weapons[0], 'Weapon 2' : self.list_of_weapons[1], 'Weapon 3' : self.list_of_weapons[2], 'Weapon 4' : self.list_of_weapons[3], 'Weapon 5' : self.list_of_weapons[4], 'Weapon 6' : self.list_of_weapons[5]}
        self.murder_weapon ={'murder weapon ': self.list_of_weapons.pop(random.randrange(0,len(self.list_of_weapons))) }
        self.dictionary_of_rooms = {'Room 1' : self.list_of_rooms[0],'Room 2' : self.list_of_rooms[1],'Room 3' : self.list_of_rooms[2], 'Room 4' : self.list_of_rooms[3],'Room 5' : self.list_of_rooms[4]}
        self.kill_room = {'death room ': self.list_of_rooms.pop(random.randrange(0,len(self.list_of_rooms)))}

        self.intro()
if __name__== "__main__":
    GamePlay()