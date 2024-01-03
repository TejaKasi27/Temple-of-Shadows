"""
This class is the main class of the "Temple of Shadows:Evacuated Labrynth" application.
'Temple of Shadows' is a very simple, text based adventure game.

"""



from text_ui import TextUI
from player import Player
import time
import random

class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.textUI = TextUI()
        self.player = Player()

    def play(self):
        """
            The main play loop.
        :return: None
        """
        self.print_welcome()
        finished = False
        while not finished:
            command = self.textUI.get_command()  # Returns a 2-tuple
            finished = self.process_command(command)

    def print_welcome(self):
        """
            Displays a welcome message.
        :return: None
        """
        self.textUI.print_to_textUI("Welcome to the Temple of Shadows:Evacuated labyrinth.")
        self.textUI.print_to_textUI("This game include an ancient mystical evacuated Indian temple of Lord Krishna hiding lots of secrets within it's mind boggling architecture.")
        self.textUI.print_to_textUI("The Indian sages in the Hindu Puranas mention about a mysterious stone which is capable of solving any health condition of all the times.")
        self.textUI.print_to_textUI("Your mission is to collect the mystery stone along with the illuminator which is the house of ancient Indian wisdom which can guide humanity and is the manual for the mystery stone.")
        self.textUI.print_to_textUI("what you waiting for? Let's explore this mysterious house of ancient wisdom !!")
        self.textUI.print_to_textUI(f'Choose your action: {self.show_command_words()}')
    def show_command_words(self):
        """
            Show a list of available commands.
        :return: None
        """
        return ['help', 'start', 'quit']

    def start(self):
        """
            Starts the game
        :return: method
        """
        return self.temple_mandapa()

    def quit(self):
        """
            Quits the game
        :return: bool
        """
        self.textUI.print_to_textUI('Thanks for playing!')
        return True

    def process_command(self, command):
        """
            Process a command from the TextUI.
        :param command: a single string
        :return: True if the game has been quit, False otherwise
        """
        command_word = command
        if command_word != None:
            command_word = command_word.upper()
        if command_word == "HELP":
            return self.print_help()
        elif command_word == "START":
            return self.start()
        elif command_word == "QUIT":
            return self.quit()
        else:
            self.textUI.print_to_textUI("Don't know what you mean.")

    def print_help(self):
        """
            Display some useful help text.
        :return: None
        """
        self.textUI.print_to_textUI("Welcome to the Temple of Shadows:Evacuated labyrinth.")
        self.textUI.print_to_textUI("This game include an ancient mystical evacuated Indian temple of Lord Krishna hiding lots of secrets within it's mind boggling architecture.")
        self.textUI.print_to_textUI("The Indian sages in the Hindu Puranas mention about a mysterious stone which is capable of solving any health condition of all the times.")
        self.textUI.print_to_textUI("Your mission is to collect the mystery stone along with the illuminator which is the house of ancient Indian wisdom which can guide humanity and is the manual for the mystery stone.")
        self.textUI.print_to_textUI(f'Choose your action: {self.show_command_words()}')

    def temple_mandapa(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print("The temple mandapam is at the entrance of the temple facing the main deity room built in Dravidian architecture style")
        #assign backpack
        print('{} you are being assigned a backpack of capacity of {} kg'.format(self.player.screen_name,self.player.backpack.capacity))
        directions = {"right", 'left', 'forward', 'backward'}
        print(f'Your directions are:{directions}')
        direction = input("Enter direction:")

        while True:
            if direction in directions:
                if direction == 'right':
                    return self.stairs_demon()
                elif direction == 'left':
                    return self.stairs_dark()
                elif direction == 'forward':
                    return self.main_deity_room()
                else:
                    print("You are facing the dead end wall")
                break
            else:
                print("Invalid direction!")
                direction = input("Enter direction:")


    def main_deity_room(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print("This room is the main altar of Lord Ranganathaswami(Krishna),the greatest mystic is the centre of all the mysteries. ")
        directions = {'right', 'left', 'forward', 'backward'}
        print('This main deity room is the proof of the advanced ancient Indian architecture which is a sign of their unparalleled wisdom.')
        print("You can solve the mystery of this room with the help of mystery stone guarded by the god's from the dark creatures and demons")
        print("Get the mystery stone from the god's by fighting the demons and the dark creatures.")
        print("Mystery stone is the key for you to escape from the mind boggling web of illusions created by this temple sanctum")
        print('Your exits are:', list(directions))
        direction = input("Enter direction:")
        while True:
            if direction in directions:
                if direction == 'right':
                    return self.stairs_guardian()
                elif direction == 'left':
                    return self.stairs_locker()
                elif direction == 'forward':
                    if self.player.backpack.check_item("Mystery stone") and self.player.backpack.check_item('Illuminator'):
                        print("Congratulation on getting the amazing mysterious stone and the illuminator!!")
                        print("You are out of the temple")
                        return self.quit()
                    else:
                        print("You lost!!")
                        return self.quit()
                else:
                    return self.temple_mandapa()

            else:
                print("Invalid direction")
                direction = input("Enter direction:")

    def stairs_guardian(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print("These magical stairs connect the main deity room with the guardian's room")
        directions = {'upstairs', 'backward'}
        print(f'Your directions are:{directions}')
        direction = input("Enter direction:")
        while True:
            if direction in directions:
                if direction == 'upstairs':
                    if self.player.backpack.check_item('Mystery stone'):
                        return self.guardians_room()

                    else:
                        return self.main_deity_room()
                else:
                    return self.main_deity_room()
            else:
                print("Invalid direction!")
                direction = input("Enter direction:")

    def stairs_locker(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print("These are the stairs to the locker room")
        directions = {'upstairs', 'backward'}
        print(f'Your directions are:{directions}')
        direction = input("Enter direction:")
        while True:
            if direction in directions:
                if direction == 'upstairs':
                    if self.player.backpack.check_item('Mystery stone'):
                        return self.locker_room()
                    else:
                        return self.main_deity_room()
                else:
                    return self.main_deity_room()

            else:
                print("Invalid direction!")
                direction = input("Enter direction:")

    def stairs_demon(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print("These stairs lead you to the demon room.!")
        directions = {"upstairs", 'backward'}
        print(f'Your directions are:{directions}')
        direction = input("Enter direction:")
        while True:
            if direction in directions:
                if direction == 'upstairs':
                    return self.demon_room()
                else:
                    return self.temple_mandapa()

            else:
                print("Invalid direction!")
                direction = input("Enter direction:")

    def stairs_dark(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print('These stairs lead to the scariest dark room')
        directions = {'upstairs', 'backward'}
        print(f'Your directions are:{directions}')
        direction = input("Enter direction:")
        while True:
            if direction in directions:
                if direction == 'upstairs':
                    return self.dark_room()
                else:
                    return self.temple_mandapa()

            else:
                print("Invalid direction!")
                direction = input("Enter direction:")

    def dark_room(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print("Welcome to the scariest dark room!This is a residence of Spirits.Don't stay for a long period without illuminator")
        print("This pitch dark room can only be lit by illuminator which haunts the darkness and reveals the path to glory")
        print("Without illuminator you can be dead in the dark room if you stay for long time!As the spirits feed on your energy")
        directions = {'forward', 'right'}
        print(f'Your directions are:{directions}')

        if not self.player.backpack.check_item('Illuminator'):
            start_time = time.time()
            while True:
                elapsed_time = time.time() - start_time
                mins, secs = divmod(elapsed_time, 60)
                hours, mins = divmod(mins, 60)
                timer = '{:02}:{:02}:{:02}'.format(int(hours), int(mins), int(secs))
                print('Time elapsed:', timer)

                if elapsed_time >= 5:
                    print('You are killed by the scary creatures')
                    return self.quit()
                direction = input("Enter direction:")
                if direction == "right":
                    return self.temple_mandapa()
                time.sleep(1)
        else:
            print("You illuminate the whole dark room with the Illuminator and delivered the spirit.With gratitude it reveals the location of the Key for god's room in the locker room")
            print("Key for guardian's room:To unlock the guardian's room")
            direction = input("Enter direction:")
            while True:
                if direction in directions:
                    if direction == 'forward':
                        return self.locker_room()
                    else:
                        return self.stairs_dark()
                else:
                    print("Invalid direction!")
                    direction = input("Enter direction:")

    def locker_room(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print("This is the locker room where the key for guardian's room is hidden")
        directions = {'left', 'right', 'backward'}
        thing = ("Key for guardian's room",2)

        if not self.player.item_visibility[thing[0]]:

            while True:
                print(f"Do you wanna pick this up?: {thing[0]}")
                response = input("Say Y or N: ")
                if response.lower() == "y":

                    item_picked = self.player.pickup(thing)
                    if item_picked:
                        print("Congratulations! You picked up the illuminator as a symbol of your courage.")
                        self.player.item_visibility[thing[0]] = True
                        break
                    else:
                        print('Ouch! Your bag is full.')
                        while True:
                            response = input("Wanna drop an item? (Y/N): ")
                            if response.lower() == 'y':
                                print('Choose an item to drop:', list(self.player.backpack.contents.keys()))
                                item_to_drop = input("Enter the item to drop: ")
                                item_dropped = self.player.drop(self.player.backpack.contents[item_to_drop])
                                if item_dropped:
                                    print('You successfully dropped the {}.'.format(item_to_drop))
                                    break  
                                else:
                                    print('Invalid item or unable to drop. Please try again.')
                            elif response.lower() == 'n':
                                print('You decided not to drop any item.')
                                break
                            else:
                                print('Invalid input. Please enter Y or N.')
                elif response.lower() == "n":
                    print("You decided not to pick the Key for guardian's room")
                    break
                else:
                    print("Invalid response! Enter Y/N")


        print(f'Your directions are:{directions}')
        direction = input("Enter input:")
        while True:
            if direction in directions:
                if direction == 'right':
                    return self.stairs_locker()

                elif direction == 'backward':
                    return self.dark_room()
                else:
                    print('You are at the dead end facing a wall')
                    print(f'Your directions are:{directions}')
                    direction = input("Enter directions:")
            else:
                print("Invalid direction!")
                direction = input("Enter direction:")

    def guardians_room(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print("Welcome to the guardian room warrior!From the time immemorial the guardians are guarding the mystery stone.")
        print("Waiting for the perfect warrior who is fit to get the mystery stone and handle it to him.")
        print("Mystery stone: Invaluable stone with immense power and capability to control time and make time travel a reality which weighs 2kg")
        directions = {'left', 'right', 'backward'}
        thing = ("Mystery stone",2)

        if not self.player.item_visibility[thing[0]]:
            while True:
                print(f"Do you wanna pick this up?: {thing[0]}")
                response = input("Say Y or N: ")
                if response.lower() == "y":
                    item_picked = self.player.pickup(thing)
                    if item_picked:
                        print("Congratulations! You picked up the Mystery stone as a symbol of your courage.")
                        self.player.item_visibility['Mystery stone'] = True
                        break
                    else:
                        print('Ouch! Your bag is full.')
                        while True:
                            response = input("Wanna drop an item? (Y/N): ")
                            if response.lower() == 'y':
                                print('Choose an item to drop:', list(self.player.backpack.contents.keys()))
                                item_to_drop = input("Enter the item to drop: ")
                                item_dropped = self.player.drop(item_to_drop)
                                if item_dropped:
                                    print('You successfully dropped the {}.'.format(item_to_drop))
                                    break
                                else:
                                    print('Invalid item or unable to drop. Please try again.')
                            elif response.lower() == 'n':
                                print('You decided not to drop any item.')
                                break
                            else:
                                print('Invalid input. Please enter Y or N.')
                elif response.lower() == 'n':
                    print('You decided not to pick up the Mystery stone.')
                    break
                else:
                    print('Invalid response! Enter Y or N')

        print(f'Your directions are:{directions}')
        direction = input("Enter directions:")
        while True:
            if direction in directions:
                if direction == 'left':
                    return self.stairs_guardian()

                elif direction == 'backward':
                    return self.demon_room()

                else:
                    print('You are at the dead end facing a wall')
                    print(f'Your directions are:{directions}')
                    direction = input("Enter directions:")

            else:
                print("Invalid direction!")
                direction = input("Enter direction:")

    def demon_room(self):
        """
            Process the directions and progress the game accordingly
        :return:method
        """
        print("This room is a habitat for a great demon king! He stole the illuminator from the gods and has been guarding it for a long time.")
        print('Defeat him in battle to get the illuminator.')
        print('Illuminator: To illuminate the dark room and lives of people, and it weighs 2kg')

        if not self.player.defeated_demon:
            fight_res = self.fight_scene()

            if fight_res == 'victory':
                self.player.defeated_demon = True
                thing = ('Illuminator', 2)
                if self.player.defeated_demon:
                    while True:
                        print(f"Do you want to pick this up?:{thing[0]}")
                        response = input("Say Y or N: ")
                        if response == "Y":
                            item_picked = self.player.pickup(thing)
                            if item_picked:
                                print("Congratulations! You picked up the illuminator as a symbol of your courage.")
                                break
                            else:
                                print('Ouch! Your bag is full.')
                                while True:
                                    response = input("Wanna drop an item? (Y/N): ")
                                    if response == 'Y':
                                        print('Choose an item to drop:', list(self.player.backpack.contents.keys()))
                                        item_to_drop = input("Enter the item to drop: ")
                                        item_dropped = self.player.drop(self.player.backpack.contents[item_to_drop])
                                        if item_dropped:
                                            print('You successfully dropped the {}.'.format(item_to_drop))
                                            break  # Exit the while loop if the item is successfully dropped
                                        else:
                                            print('Invalid item or unable to drop. Please try again.')
                                    elif response == 'N':
                                        print('You decided not to drop any item.')
                                        break  # Exit the while loop if the player decides not to drop any item
                                    else:
                                        print('Invalid input. Please enter Y or N.')
                        elif response == 'N':
                            print('You decided not to pick up the illuminator.')
                            break
                        else:
                            print('Invalid input. Please enter Y or N.')

            elif fight_res == 'defeated':
                return self.quit()

        directions = {'forward', 'left'}
        print(f'Your directions are: {directions}')
        direction = input("Enter directions:")

        while True:
            if direction in directions:

                if direction == 'forward':
                    if self.player.backpack.check_item("Key for guardian's room"):
                        return self.guardians_room()
                    else:
                        print("You do not have the key to unlock this guardian's room")
                        print(f'Your directions are: {directions}')
                        direction = input("Enter directions:")
                else:
                    return self.stairs_demon()

            else:
                print("Invalid direction!")
                direction = input("Enter direction:")

    def fight_scene(self):
        """
            Dynamic fight scene with demon
        :return:str
        """
        player_health = 100
        demon_health = 100

        print("The demon king appears!")
        while player_health > 0 and demon_health > 0:
            print("Player Health:", player_health)
            print("Demon Health:", demon_health)
            action = input("Enter 'attack' to attack the demon or 'run' to escape: ")

            if action == "attack":
                player_damage = random.randint(10, 20)
                demon_damage = random.randint(5, 15)
                demon_health -= player_damage
                player_health -= demon_damage
                print("You attack the demon and deal", player_damage, "damage.")
                print("The demon attacks you and deals", demon_damage, "damage.")

            elif action == "run":
                print("You attempt to run away...")
                if random.random() < 0.5:
                    print("You successfully escape from the demon!")
                    return "escaped"
                else:
                    print("You failed to escape! The demon catches up to you.")
                    player_health -= 20

            else:
                print("Invalid action! Please enter 'attack' or 'run'.")

        if player_health <= 0:
            print("You have been defeated by the demon!")
            return "defeated"
        else:
            print("You have defeated the demon!")
            return "victory"


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
