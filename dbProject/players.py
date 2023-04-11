class Players:
    def __init__(self, key_id,player_id, family_name, given_name, birth_date, goal_keeper, defender, midfielder,forward,count_tournaments,list_tournaments,player_wikipedia_link):
        self.key_id = key_id
        self.player_id = player_id
        self.family_name = family_name
        self.given_name = given_name
        self.birth_date = birth_date
        self.goal_keeper = goal_keeper
        self.defender = defender
        self.midfielder = midfielder
        self.forward = forward
        self.count_tournaments=count_tournaments
        self.list_tournaments=list_tournaments
        self.player_wikipedia_link=player_wikipedia_link
