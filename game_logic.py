class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def to_dict(self):
        return {
            "name": self.name,
            "inventory": self.inventory
        }

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.map = self.create_map()
        self.current_location = "Beach"

    def create_map(self):
        return {
            "Beach": {
                "description": "You are standing on a sandy beach with waves crashing nearby.",
                "items": ["Shell"],
                "directions": {"North": "Jungle", "East": "Cave"}
            },
            "Jungle": {
                "description": "A dense jungle filled with tall trees and exotic sounds.",
                "items": ["Map"],
                "directions": {"South": "Beach", "West": "Waterfall"}
            },
            "Cave": {
                "description": "A dark and eerie cave. You hear echoes all around.",
                "items": ["Torch"],
                "directions": {"West": "Beach"}
            },
            "Waterfall": {
                "description": "A beautiful waterfall with a hidden passage behind it.",
                "items": ["Key"],
                "directions": {"East": "Jungle"}
            }
        }

    def display_location(self):
        location = self.map[self.current_location]
        self.location_description = location["description"]
        self.items = ", ".join(location["items"]) if location["items"] else "No items."
        self.directions = ", ".join(location["directions"].keys())

    def move(self, direction):
        if direction in self.map[self.current_location]["directions"]:
            self.current_location = self.map[self.current_location]["directions"][direction]
            self.display_location()

    def to_dict(self):
        return {
            "player": self.player.to_dict(),
            "map": self.map,
            "current_location": self.current_location
        }

    @classmethod
    def from_dict(cls, data):
        game = cls(data["player"]["name"])
        game.player.inventory = data["player"]["inventory"]
        game.map = data["map"]
        game.current_location = data["current_location"]
        return game
