from game_obj.item import Item
from game_obj.player import Player
from selectabletext_lib.SelectableText_lib import SelectableText_lib

class Store():
    
    def __init__(self, Player : Player):
        self.ST_lib : SelectableText_lib = SelectableText_lib()
        self.item_count : int = 0
        self.Items : dict[int, Item] = {}
        self.player = Player
    
    def add_item(self, name: str, initial_cost: int, description : str):
        temp_item : Item = Item(name, initial_cost, description)
        self.Items[self.item_count] = temp_item
        self.ST_lib.addText(f"buy [{name}]", self.sell_item, self.item_count)
        self.item_count += 1
        
    
    def tick(self):
        for key in self.Items:
            current_item : Item = self.Items[key]
            current_item.tick(1)
            
    def sell_item(self, item_number : int):
        item : Item = self.Items[item_number]
        succes: bool = item.sell(1, self.player.cash)
        if (succes):
            self.player.Items.append(item)
            self.player.cash -= item.cost
            return True
        else:
            return False
        
    def enter(self):
        BuildText = list([])
        for ItemKey in self.Items:
            BuildText.append(ItemKey)
        self.ST_lib.setShownText(BuildText)
        self.ST_lib.displayText()