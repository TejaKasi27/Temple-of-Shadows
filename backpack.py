class Backpack:
    """
    A class to allow user to add and remove items...
    Backpack is limited to number of items set by capacity.
    This example incorporates a user defined exception.
    """
    def __init__(self, capacity):
        self.contents = {}
        self.capacity = capacity
    def contents_weight(self):
        """
            To calculate the weight of contents in backpack
        :return:int
        """
        weight = 0
        for value in self.contents.values():
            weight += value
        return weight
    def add_item(self, item):
        """
            Adds an item to our backpack
        :param:item
        :return:bool
        """
        if self.contents_weight() < self.capacity:
            self.contents[item[0]] = item[1]
            return True
        return False
    def remove_item(self, item):
        """
        Removes an item from our backpack
        :param:str
        :return:bool
        """
        try:
            if item not in self.contents:
                raise NotInBackpackError(item, 'is not in the backpack.')
            del self.contents[item]
            return True

        except NotInBackpackError as e:
            print(f'Error: {e.item} {e.message}')
        finally:
            print('Carrying on...')

    def check_item(self, item):
        """
            Returns True if item is in backpack, False otherwise.
        :param:str
        :return:None
        """
        return item in self.contents

"""
    This class hanldes exception if the player try to drop items not in backpack
    
"""
class NotInBackpackError(Exception):
    def __init__(self, item, message):
        self.item = item
        self.message = message
