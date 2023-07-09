class Player:
    def __init__(self, name):
        self._name = name
        self.score = 0
        self.inputs = []

    @property
    def name(self):
        return self._name

    def do_work(self, letter):
        # name = input(f"Enter a name for {self.name}: ")
        # city = input(f"Enter a city for {self.name}: ")
        # food = input(f"Enter a food for {self.name}: ")
        # color = input(f"Enter a color for {self.name}: ")

        new_inputs = []
        for category in ["name", "city", "food", "color"]:
            input_value = input(f">> Enter a {category} for {self.name}: ").lower()
            if input_value.startswith(letter):
                new_inputs.append(input_value)

        self.calculate_score(letter, new_inputs)

    def calculate_score(self, letter, new_inputs):
        score = 0
        for item in new_inputs:
            if item in self.inputs:
                score += 5
            elif item != '':
                score += 10 
        self.score = score
        self.inputs.extend(new_inputs)


class Game:
    def __init__(self):
        self.players = []
        self.letter = ''

    def add_player(self, player):
        self.players.append(player)

    def set_letter(self):
        self.letter = input("Enter a letter: ")

    def start_game(self):
        # self.letter = input("Enter a letter: ")
        self.set_letter()

        for player in self.players:
            player.do_work(self.letter)

        self.print_scores()

    def print_scores(self):
        for player in self.players:
            print(f"{player.name}: {player.score} points")


