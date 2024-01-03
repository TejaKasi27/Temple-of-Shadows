"""
This class creates player object and allows him to pick and drop items
"""


from backpack import Backpack
class Player:
    def __init__(self):
        print('Please tell us how you like to be referred:')
        self.screen_name = input("Enter your screen name:")
        print(f"Hi {self.screen_name}!")
        self.backpack = Backpack(4)
        self.defeated_demon = False
        self.item_visibility = {"Mystery stone":False,"Key for guardian's room":False}

    def pickup(self,item):
        """
           Allows Player to pick an item found in the room
        :param:str
        :return:bool
        """
        item_added = self.backpack.add_item(item)
        if item_added:
            print('You have this in your bag')
        return item_added

    def inventory(self):
        """
            Displays the items in the backpack
        :return:None
        """
        print(f"Your backpack contains:{self.backpack.contents}")

    def drop(self, item):
        """
            Allows player to drop items
        :param:a string
        :return:bool
        """
        if item in self.backpack.contents:
            if self.backpack.remove_item(item):
                print("Uday 1")
                return True
        return False









