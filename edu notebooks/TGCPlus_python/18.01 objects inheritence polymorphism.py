import json

class MissingChildMethodError(Exception):
    pass


class FootballPlayer:
    name = 'John'
    team = 'None'
    years_in_league = 0

    def print_player(self):
        print(self.name+" : "+self.team)

    def is_good(self):
        raise MissingChildMethodError("Error! is_good is not defined!")

    # def print_good(self):
    #     if self.is_good():
    #         print(" is a good player")
    #     else:
    #         print(" is NOT a good player")


class Quarterback(FootballPlayer):
    pass_attempts = 0
    completions = 0
    pass_yards = 0

    def completion_rate(self):
        return self.completions/self.pass_attempts

    def yards_per_attempt(self):
        return self.pass_yards/self.pass_attempts

    def is_good(self):
        return self.yards_per_attempt() > 7


    # def __init__(self):
    #     self.name = 'QB Mike!'
    #     self.team = 'Gold'
    #
    # def is_good(self):
    #     print("yup, is good")


class Runningback(FootballPlayer):
    rushes = 0
    rush_yards = 0

    def yards_per_rush(self):
        return self.rush_yards/self.rushes

    def is_good(self):
        return self.yards_per_rush() > 4

    # name = 'RB Joe!'
    # team = 'Red'
    #
    # def is_good(self):
    #     print("yup, is good")


player_qb = Quarterback()
player_qb.name = "Markush Frimpt"
player_qb.team = "Donkers"
player_qb.years_in_league = 21
player_qb.pass_attempts = 7
player_qb.completions = 8
player_qb.pass_yards = 3

player_rb = Runningback()
player_rb.name = "Jakey Pooh"
player_rb.team = "The Monkeys"
player_rb.years_in_league = 33
player_rb.rush_yards = 9
player_rb.rushes = 10

player_list = [player_qb, player_rb]

# STORING OBJECTS IN JSON
outfile = open("datafile.json", "w")
for player in player_list:
    json_string = json.dumps(player.__dict__)+'\n'
    outfile.write(json_string)

outfile.close()

for player in player_list:
    player.print_player()

    try:
        if player.is_good():
            print('dfg')
        else:
            print('lokki')
    except MissingChildMethodError:
        print("You forgot to define is_good()")


# print(player_qb.name)
# print(player_qb.pass_yards)

# print(player_rb.name)
# print(player_rb.rushes)

# player_qb.print_player()
# player_rb.print_player()
