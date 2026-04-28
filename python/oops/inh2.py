class Football:
    def __init__(self, player_id, player_name, match_goals):
        self.player_id = player_id
        self.player_name = player_name
        self.match_goals = match_goals
        self.qualified = False  # default

    def findQualification(self):
        avg_goals = sum(self.match_goals) / len(self.match_goals)

        if avg_goals < 3:
            self.qualified = False
        else:
            self.qualified = True

        return self.qualified


# Creating objects
p1 = Football(101, "Messi", [2, 3, 4, 3, 5])
p2 = Football(102, "Ronaldo", [1, 2, 1, 2, 2])

# Checking qualification
print(p1.player_name, "QUALIFIED" if p1.findQualification() else "DISQUALIFIED")
print(p2.player_name, "QUALIFIED" if p2.findQualification() else "DISQUALIFIED")