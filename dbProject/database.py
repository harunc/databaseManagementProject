import sqlite3 as dbapi2
from teams import Teams
from bookings import Bookings
from referees import Referees
from refereesap import Refereesap

from players import Players
from award_winners import AwardWinners


class Db:
    def __init__(self, database_File):
        self.database_File = database_File
    
    def add_teams(self, team):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO TEAMS (team_id, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, ( team.team_id,team.team_name, team.federation_name, team.region_name, team.confederation_id, team.confederation_name, team.team_wikipedia_link))
            connection.commit()
            team_key = cursor.lastrowid
        return team_key
    
    def update_team(self, team):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "UPDATE TEAMS SET TEAM_ID = ?, TEAM_name = ?, FEDERATION_NAME = ?, REGION_NAME = ?, CONFEDERATION_ID = ?, CONFEDERATION_name = ?, TEAM_WIKIPEDIA_LINK = ? WHERE (KEY_ID = ?)"
            cursor.execute(query, (team.team_id,team.team_name, team.federation_name, team.region_name, team.confederation_id, team.confederation_name, team.team_wikipedia_link, team.key_id))
            connection.commit()

    def find_team_id(self, team_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM TEAMS WHERE (KEY_ID = ?)"
            cursor.execute(query, (team_key,))
            team_keyy, team_id, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link = cursor.fetchone()
        team_ = Teams(team_keyy, team_id, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link)
        team_idd = '%' + team_.team_id + '%'
        return team_idd

    def delete_foreign(self, team_idd):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM BOOKINGS WHERE (team_id like (?))"
            cursor.execute(query, (team_idd,))
            connection.commit()

    def delete_team(self, team_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM TEAMS WHERE (key_id = ?)"
            cursor.execute(query, (team_key,))
            connection.commit()

    def get_team(self, team_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM TEAMS WHERE (KEY_ID = ?)"
            cursor.execute(query, (team_key,))
            team_keyy, team_id, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link = cursor.fetchone()
        team_ = Teams(team_keyy, team_id, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link)
        return team_

    def get_team_foreign(self, team_id):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM TEAMS WHERE (team_id like (?))"
            print(team_id)
            cursor.execute(query, (team_id,))
            team_key, team_iddd, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link = cursor.fetchone()
        team_ = Teams(team_key, team_iddd, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link)
        return team_

    def get_teams(self):
        teams = []
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM TEAMS ORDER BY KEY_ID"
            cursor.execute(query)
            for team_key, team_id,team_name,federation_name,region_name,confederation_id,confederation_name,team_wikipedia_link in cursor:
                teams.append((team_key, Teams( team_key, team_id, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link)))
        return teams

    def get_booking(self, booking_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM BOOKINGS WHERE (KEY_ID = ?)"
            cursor.execute(query, (booking_key, ))
            bookin_key, booking_id, tournament_id, tournament_name, match_id, match_name, match_date, stage_name, team_id = cursor.fetchone()
        booking = Bookings(bookin_key, booking_id, tournament_id, tournament_name, match_id, match_name, match_date, stage_name, team_id)
        return booking

    def get_bookings(self):
        bookings = []
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM BOOKINGS ORDER BY KEY_ID"
            cursor.execute(query)
            for bookings_key, booking_id,tournament_id,tournament_name,match_id,match_name,match_date,stage_name,team_id in cursor:
                bookings.append((bookings_key, Bookings(bookings_key, booking_id, tournament_id, tournament_name, match_id, match_name, match_date, stage_name, team_id)))
        return bookings
    
    def delete_booking(self, booking_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM BOOKINGS WHERE (key_id = ?)"
            cursor.execute(query, (booking_key,))
            connection.commit()

    def add_bookings(self, booking):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO BOOKINGS (booking_id, tournament_id, tournament_name, match_id, match_name, match_date, stage_name, team_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (booking.booking_id,booking.tournament_id, booking.tournament_name, booking.match_id, booking.match_name, booking.match_date, booking.stage_name, booking.team_id))
            connection.commit()
            booking_key = cursor.lastrowid
        return booking_key

    def update_booking(self, booking):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "UPDATE BOOKINGS SET BOOKING_ID = ?, TOURNAMENT_ID = ?, TOURNAMENT_NAME = ?, MATCH_ID = ?, MATCH_NAME = ?, MATCH_DATE = ?, STAGE_NAME = ?, TEAM_ID = ? WHERE (KEY_ID = ?)"
            cursor.execute(query, (booking.booking_id,booking.tournament_id, booking.tournament_name, booking.match_id, booking.match_name, booking.match_date, booking.stage_name, booking.team_id, booking.key_id))
            connection.commit()

    def add_referee(self, referee):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO REFEREES (referee_id, family_name, given_name, country_name, confederation_id, confederation_name, confederation_code, referee_wikipedia_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (referee.referee_id,referee.family_name,referee.given_name,referee.country_name,referee.confederation_id,referee.confederation_name,referee.confederation_code,referee.referee_wikipedia_link))
            connection.commit()
            referee_key = cursor.lastrowid
        return referee_key

    def update_referee(self, referee):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "UPDATE REFEREES SET REFEREE_ID = ?, FAMILY_NAME = ?, GIVEN_NAME = ?, COUNTRY_NAME = ?, CONFEDERATION_ID = ?, CONFEDERATION_NAME = ?, CONFEDERATION_CODE = ?, REFEREE_WIKIPEDIA_LINK = ? WHERE (KEY_ID = ?)"
            cursor.execute(query, (referee.referee_id,referee.family_name,referee.given_name,referee.country_name,referee.confederation_id,referee.confederation_name,referee.confederation_code,referee.referee_wikipedia_link, referee.key_id))
            connection.commit()

    def delete_referee(self, referee_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM REFEREES WHERE (key_id = ?)"
            cursor.execute(query, (referee_key,))
            connection.commit()

    def get_referee(self, referee_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM REFEREES WHERE (KEY_ID = ?)"
            cursor.execute(query, (referee_key,))
            rf_key, a,b,c,d,e,f,g,h = cursor.fetchone()
        referee_ = Referees(rf_key,a,b,c,d,e,f,g,h)
        return referee_

    def get_referees(self):
        referees = []
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM REFEREES ORDER BY KEY_ID"
            cursor.execute(query)
            for referee_key, a,b,c,d,e,f,g,h in cursor:
                referees.append((referee_key, Referees(referee_key,a, b, c, d, e, f, g,h)))
        return referees

    def get_refereesap(self):
        refereesap = []
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM REFEREEAP ORDER BY KEY_ID"
            cursor.execute(query)
            for refereesap_key, a,b,c,d,e,f,g,h,i,k,l,m,n,o in cursor:
                refereesap.append((refereesap_key, Refereesap(a, b, c, d, e, f, g, h, i, k, l, m, n, o)))
        return refereesap

    def add_refereeap(self, refereeap):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO REFEREEAP (tournament_id,tournament_name, match_id, match_name, match_date, stage_name, group_name, referee_id, family_name, given_name, country_name, confederation_id, confederation_name, confederation_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(query, (refereeap.tournament_id, refereeap.tournament_name, refereeap.match_id, refereeap.match_name, refereeap.match_date, refereeap.stage_name, refereeap.group_name, refereeap.referee_id,refereeap.family_name,refereeap.given_name,refereeap.country_name,refereeap.confederation_id,refereeap.confederation_name,refereeap.confederation_code))
            connection.commit()
            refereeap_key = cursor.lastrowid
        return refereeap_key

    def get_refereeap(self, refereeap_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT tournament_id, tournament_name, match_id, match_name, match_date, stage_name, group_name, referee_id, family_name, given_name, country_name, confederation_id, confederation_name, confederation_code FROM REFEREEAP WHERE (key_id = ?)"
            cursor.execute(query, (refereeap_key,))
            a,b,c,d,e,f,g,h,i,k,l,m,n,o = cursor.fetchone()
        refereeap_ = Refereesap(a,b,c,d,e,f,g,h,i,k,l,m,n,o)
        return refereeap_

    def update_refereeap(self, refereeap_key, refereeap):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "UPDATE REFEREEAP SET tournament_id = ?, tournament_name = ?, match_id = ?, match_name = ?, match_date = ?, stage_name = ?, group_name = ?,  referee_id = ?, family_name = ?, given_name = ?, country_name = ?, confederation_id = ?, confederation_name = ?, confederation_code = ? WHERE (key_id = ?)"
            cursor.execute(query, (refereeap.tournament_id, refereeap.tournament_name, refereeap.match_id, refereeap.match_name, refereeap.match_date, refereeap.stage_name, refereeap.group_name, refereeap.referee_id,refereeap.family_name,refereeap.given_name,refereeap.country_name,refereeap.confederation_id,refereeap.confederation_name,refereeap.confederation_code, refereeap_key))
            connection.commit()

    def delete_refereeap(self, refereeap_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM REFEREEAP WHERE (key_id = ?)"
            cursor.execute(query, (refereeap_key,))
            connection.commit()

    def add_player(self, player):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO PLAYERS (player_id, family_name, given_name, birth_date, goal_keeper, defender, midfielder,forward,count_tournaments,list_tournaments,player_wikipedia_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?,?,?)"
            cursor.execute(query, (player.player_id,player.family_name,player.given_name,player.birth_date,player.goal_keeper,player.defender,player.midfielder,player.forward,player.count_tournaments,player.list_tournaments,player.player_wikipedia_link))
            connection.commit()
            player_key = cursor.lastrowid
        return player_key

    def update_player(self, player):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "UPDATE PLAYERS SET PLAYER_ID = ?, FAMILY_NAME = ?, GIVEN_NAME = ?, BIRTH_DATE = ?, GOAL_KEEPER = ?, DEFENDER = ?, MIDFIELDER = ?, FORWARD = ?, COUNT_TOURNAMENTS = ?, LIST_TOURNAMENTS = ?, PLAYER_WIKIPEDIA_LINK = ? WHERE (KEY_ID = ?)"
            cursor.execute(query, (player.player_id,player.family_name,player.given_name,player.birth_date,player.goal_keeper,player.defender,player.midfielder,player.forward,player.count_tournaments,player.list_tournaments,player.player_wikipedia_link,player.key_id))
            connection.commit()

    def delete_player(self, player_id):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM PLAYERS WHERE (key_id = ?)"
            cursor.execute(query, (player_id,))
            connection.commit()

    def get_player(self, player_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PLAYERS WHERE (KEY_ID = ?)"
            cursor.execute(query, (player_key,))
            player_key, a,b,c,d,e,f,g,h,i,j,k = cursor.fetchone()
        player = Players(player_key,a, b, c, d, e, f, g,h,i,j,k)
        return player

    def get_players(self):
        players = []
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PLAYERS ORDER BY KEY_ID"
            cursor.execute(query)
            for referee_key, a,b,c,d,e,f,g,h,i,j,k in cursor:
                players.append((referee_key, Players(referee_key,a, b, c, d, e, f, g,h,i,j,k)))
        return players

    def find_player_id(self, player_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PLAYERS WHERE (KEY_ID = ?)"
            cursor.execute(query, (player_key,))
            player_key, a,b,c,d,e,f,g,h,i,j,k = cursor.fetchone()
        player = Players(player_key,a, b, c, d, e, f, g,h,i,j,k)
        player_id2 = '%' + player.player_id + '%'
        return player_id2

    def delete_foreign3(self, player_id2):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM AWARD_WINNERS WHERE (player_id like (?))"
            cursor.execute(query, (player_id2,))
            connection.commit()

    def get_player_foreign(self,player_id):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PLAYERS WHERE (KEY_ID = ?)"
            cursor.execute(query, (player_id,))
            player_key, a,b,c,d,e,f,g,h,i,j,k = cursor.fetchone()
        player = Players(player_key,a, b, c, d, e, f, g,h,i,j,k)
        return player

    def get_awardwinner(self, award_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM AWARD_WINNERS WHERE (KEY_ID = ?)"
            cursor.execute(query, (award_key,))
            aw_key, a,b,c,d,e,f,g,h,i,k,l = cursor.fetchone()
        awardwinner = AwardWinners(aw_key,a, b, c, d, e, f, g, h, i, k, l)
        return awardwinner

    def get_awardwinners(self):
        awardwinners = []
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM AWARD_WINNERS ORDER BY KEY_ID"
            cursor.execute(query)
            for refereesap_key, a,b,c,d,e,f,g,h,i,k,l in cursor:
                awardwinners.append((refereesap_key, AwardWinners(refereesap_key,a, b, c, d, e, f, g, h, i, k, l)))
        return awardwinners
    def delete_awardwinner(self, award_id):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM AWARD_WINNERS WHERE (key_id = ?)"
            cursor.execute(query, (award_id,))
            connection.commit()

    def add_awardwinner(self, award):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO AWARD_WINNERS (tournament_id, tournament_name, award_id, award_name, shared, player_id, family_name,given_name,team_id,team_name,team_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?,?,?)"
            cursor.execute(query, (award.tournament_id,award.tournament_name,award.award_id,award.award_name,award.shared,award.player_id,award.family_name,award.given_name,award.team_id,award.team_name,award.team_code))
            connection.commit()
            awardwinner_key = cursor.lastrowid
        return awardwinner_key

    def update_awardwinner(self, award):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "UPDATE AWARD_WINNERS SET TOURNAMENT_ID = ?, TOURNAMENT_NAME = ?, AWARD_ID = ?, AWARD_NAME = ?, SHARED = ?, PLAYER_ID = ?, FAMILY_NAME = ?, GIVEN_NAME = ?, TEAM_ID = ?, TEAM_NAME = ?, TEAM_CODE = ? WHERE (KEY_ID = ?)"
            cursor.execute(query, (award.tournament_id,award.tournament_name,award.award_id,award.award_name,award.shared,award.player_id,award.family_name,award.given_name,award.team_id,award.team_name,award.team_code,award.key_id))
            connection.commit()

    def get_referee_foreign(self, referee_id):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM REFEREES WHERE (referee_id like (?))"
            print(referee_id)
            cursor.execute(query, (referee_id,))
            a,b,c,d,e,f,g,h,i = cursor.fetchone()
        team_ = Referees(a,b,c,d,e,f,g,h,i)
        return team_

    def delete_foreign2(self, referee_id):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM REFEREEAP WHERE (referee_id like (?))"
            cursor.execute(query, (referee_id,))
            connection.commit()

    def find_referee_id(self, referee_key):
        with dbapi2.connect(self.database_File) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM REFEREES WHERE (KEY_ID = ?)"
            cursor.execute(query, (referee_key,))
            a,b,c,d,e,f,g,h,i = cursor.fetchone()
        referee_ = Referees(a,b,c,d,e,f,g,h,i)
        referee_idd = '%' + referee_.referee_id + '%'
        return referee_idd
