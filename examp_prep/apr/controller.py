class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        name_added = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                name_added.append(player.name)
        return f"Successfully added: {', '.join(name_added)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name, sustenance_type: str):
        player = self.__find_player(player_name)

        if player is None:
            return

        if sustenance_type != "Food" and sustenance_type != "Drink":
            return

        idx, supply = self.__find_sustenance(sustenance_type)

        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        player.stamina = min(player.stamina + supply.energy, 100)

        self.supplies.pop(idx)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina.\n" \
                   f"Player {second_player.name} does not have enough stamina."

        if first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."

        if second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        first_player_damage = first_player.stamina / 2
        second_player.stamina = max(second_player.stamina - first_player_damage, 0)
        if second_player.stamina == 0:
            return f"Winner: {first_player.name}"

        second_player_damage = second_player.stamina / 2
        first_player.stamina = max(first_player.stamina - second_player_damage, 0)
        if first_player.stamina == 0:
            return f"Winner: {second_player.name}"

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += f"{str(player)}\n"
        for supply in self.supplies:
            result += f"{supply.details()}\n"
        return result.strip()

    def __find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_sustenance(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return idx, supply
        return -1, None

