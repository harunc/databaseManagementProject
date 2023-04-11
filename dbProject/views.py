from flask import current_app, render_template, request, redirect, url_for
from teams import Teams
from bookings import Bookings
from referees import Referees
from refereesap import Refereesap
from players import Players
from award_winners import AwardWinners

def home_page():
    return render_template("home.html")

def teams_page():
    db = current_app.config["db"]
    if request.method == "GET":
        teams = db.get_teams()
        return render_template("teams.html", teams=sorted(teams))
    elif request.method== "POST":
        deleteTeam = request.form.get("deleteTeam","")
        db.delete_foreign(db.find_team_id(int(deleteTeam)))
        db.delete_team(int(deleteTeam))
        return redirect(url_for("teams_page"))

def team_add_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("teams_edit.html")
    else:
        team_id = request.form["team_id"]
        team_name = request.form["team_name"]
        federation_name = request.form["federation_name"]
        region_name = request.form["region_name"]
        confederation_id = request.form["confederation_id"]
        confederation_name = request.form["confederation_name"]
        team_wikipedia_link = request.form["team_wikipedia_link"]
        team = Teams(0, team_id, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link)
        team_key = db.add_teams(team)
        return redirect(url_for("teams_page", team_key = team_key))

def team_page(team_key):
    db = current_app.config["db"]
    team = db.get_team(team_key)
    return render_template("team.html", team=team)

def team_page_foreign(team_id):
    db = current_app.config["db"]
    team_idd = '%' + team_id + '%'
    team = db.get_team_foreign(team_idd)
    return render_template("team.html", team = team)

def team_update_page():
    db = current_app.config["db"]
    a = request.args["updateTeam"]
    if request.method == "GET":
        team = db.get_team(int(a))
        return render_template("teams_edit.html", team = team)
    else:
        team_id = request.form["team_id"]
        team_name = request.form["team_name"]
        federation_name = request.form["federation_name"]
        region_name = request.form["region_name"]
        confederation_id = request.form["confederation_id"]
        confederation_name = request.form["confederation_name"]
        team_wikipedia_link = request.form["team_wikipedia_link"]
        team = Teams(a, team_id, team_name, federation_name, region_name, confederation_id, confederation_name, team_wikipedia_link)
        db.update_team(team)
        return redirect(url_for("teams_page"))


def bookings_page():
    db = current_app.config["db"]
    if request.method == "GET":
        bookings = db.get_bookings()
        return render_template("bookings.html", bookings = sorted(bookings))
    elif request.method== "POST":
        deleteBooking = request.form.get("deleteBooking","")
        db.delete_booking(int(deleteBooking))
        return redirect(url_for("bookings_page"))

def booking_add_page():
    db = current_app.config["db"]
    if request.method == "GET":
        return render_template("bookings_edit.html")
    else:
        booking_id = request.form["booking_id"]
        tournament_id = request.form["tournament_id"]
        tournament_name = request.form["tournament_name"]
        match_id = request.form["match_id"]
        match_name = request.form["match_name"]
        match_date = request.form["match_date"]
        stage_name = request.form["stage_name"]
        team_id = request.form["team_id"]
        booking = Bookings(0, booking_id, tournament_id, tournament_name, match_id, match_name, match_date, stage_name, team_id)
        booking_key = db.add_bookings(booking)
        return redirect(url_for("bookings_page", booking_key = booking_key))

def booking_update_page():
    db = current_app.config["db"]
    a = request.args["updateBooking"]
    if request.method == "GET":
        booking = db.get_booking(int(a))
        return render_template("bookings_edit.html", booking = booking)
    else:
        booking_id = request.form["booking_id"]
        tournament_id = request.form["tournament_id"]
        tournament_name = request.form["tournament_name"]
        match_id = request.form["match_id"]
        match_name = request.form["match_name"]
        match_date = request.form["match_date"]
        stage_name = request.form["stage_name"]
        team_id = request.form["team_id"]
        booking = Bookings(a, booking_id, tournament_id, tournament_name, match_id, match_name, match_date, stage_name, team_id)
        db.update_booking(booking)
        return redirect(url_for("bookings_page"))

def referees_page():
    db = current_app.config["db"]
    if request.method == "GET":
        referees = db.get_referees()
        return render_template("referees.html", referees=sorted(referees))
    else:
        a = request.form["rfdelete"]
        db.delete_foreign2(db.find_referee_id(int(a)))
        db.delete_referee(int(a))
        return redirect(url_for("referees_page"))

def referee_page(referee_key):
    db = current_app.config["db"]
    referee = db.get_referee(referee_key)
    return render_template("referee.html", referee=referee)

def referee_page_foreign(referee_id):
    db = current_app.config["db"]
    referee_idd = '%' + referee_id + '%'
    referee = db.get_referee_foreign(referee_idd)
    return render_template("referee.html", referee = referee)

def referee_add_page():
    if request.method == "GET":
        return render_template("referee_edit.html")
    else:
        form_referee_id = request.form["referee_id"]
        form_family_name = request.form["family_name"]
        form_given_name = request.form["given_name"]
        form_country_name = request.form["country_name"]
        form_confederation_id = request.form["confederation_id"]
        form_confederation_name = request.form["confederation_name"]
        form_confederation_code = request.form["confederation_code"]
        form_referee_wikipedia_link = request.form["referee_wikipedia_link"]
        referee = Referees(0,form_referee_id, form_family_name, form_given_name, form_country_name, form_confederation_id, form_confederation_name, form_confederation_code, form_referee_wikipedia_link)
        db = current_app.config["db"]
        referee_key = db.add_referee(referee)
        return redirect(url_for("referees_page", referee_key=referee_key))

def refereeap_add_page():
    if request.method == "GET":
        return render_template("refereeap_edit.html")
    else:
        form_tournament_id = request.form["tournament_id"]
        form_tournament_name = request.form["tournament_name"]
        form_match_id = request.form["match_id"]
        form_match_name = request.form["match_name"]
        form_match_date = request.form["match_date"]
        form_stage_name = request.form["stage_name"]
        form_group_name = request.form["group_name"]
        form_referee_id = request.form["referee_id"]
        form_family_name = request.form["family_name"]
        form_given_name = request.form["given_name"]
        form_country_name = request.form["country_name"]
        form_confederation_id = request.form["confederation_id"]
        form_confederation_name = request.form["confederation_name"]
        form_confederation_code = request.form["confederation_code"]
        refereeap = Refereesap(form_tournament_id, form_tournament_name, form_match_id, form_match_name, form_match_date, form_stage_name, form_group_name, form_referee_id, form_family_name, form_given_name, form_country_name, form_confederation_id, form_confederation_name, form_confederation_code)
        db = current_app.config["db"]
        refereeap_key = db.add_refereeap(refereeap)
        return redirect(url_for("refereesap_page", refereeap_key=refereeap_key))

def refereeap_page(refereeap_key):
    db = current_app.config["db"]
    refereeap = db.get_refereeap(refereeap_key)
    return render_template("refereeap.html", refereeap=refereeap)

def referee_update_page():
    db = current_app.config["db"]
    a = request.args["rfupdate"]
    if request.method == "GET":
        referee = db.get_referee(int(a))
        return render_template("referee_edit.html",referee=referee)
    else:
        form_referee_id = request.form["referee_id"]
        form_family_name = request.form["family_name"]
        form_given_name = request.form["given_name"]
        form_country_name = request.form["country_name"]
        form_confederation_id = request.form["confederation_id"]
        form_confederation_name = request.form["confederation_name"]
        form_confederation_code = request.form["confederation_code"]
        form_referee_wikipedia_link = request.form["referee_wikipedia_link"]
        referee = Referees(a,form_referee_id, form_family_name, form_given_name, form_country_name, form_confederation_id, form_confederation_name, form_confederation_code, form_referee_wikipedia_link)
        referee_key = db.update_referee(referee)
        return redirect(url_for("referees_page", referee_key=referee_key))

def refereesap_page():
    db = current_app.config["db"]
    if request.method == "GET":
        refereesap = db.get_refereesap()
        return render_template("referees_ap.html", refereesap=sorted(refereesap))
    else:
        form_refereeap_keys = request.form.getlist("refereeap_keys")
        for form_refereeap_key in form_refereeap_keys:
            db.delete_refereeap(int(form_refereeap_key))
        return redirect(url_for("refereesap_page"))


def players_page():
    db = current_app.config["db"]
    if request.method == "GET":
        players = db.get_players()
        return render_template("players.html", players=players)
    elif request.method== "POST":
        a = request.form.get("delete","")
        b=db.delete_foreign3(db.find_player_id(int(a)))
        print(b)
        db.delete_player(int(a))
        return redirect(url_for("players_page"))

def players_add_page():
    if request.method == "GET":
        return render_template("players_edit.html")
    else:
        player_id = request.form["player_id"]
        family_name = request.form["family_name"]
        given_name = request.form["given_name"]
        birth_date = request.form["birth_date"]
        goal_keeper = request.form["goal_keeper"]
        defender = request.form["defender"]
        midfielder = request.form["midfielder"]
        forward = request.form["forward"]
        count_tournaments = request.form["count_tournaments"]
        list_tournaments = request.form["list_tournaments"]
        player_wikipedia_link = request.form["player_wikipedia_link"]
        player = Players(0,player_id, family_name, given_name, birth_date, goal_keeper, defender, midfielder,forward,count_tournaments,list_tournaments,player_wikipedia_link)
        db = current_app.config["db"]
        referee_key = db.add_player(player)
        return redirect(url_for("players_page", referee_key=referee_key))

def players_update_page():
    db = current_app.config["db"]
    a = request.args["player"]
    if request.method == "GET":
        player=db.get_player(int(a))
        return render_template("players_edit.html",player=player)
    elif request.method== "POST":
        player_id = request.form["player_id"]
        family_name = request.form["family_name"]
        given_name = request.form["given_name"]
        birth_date = request.form["birth_date"]
        goal_keeper = request.form["goal_keeper"]
        defender = request.form["defender"]
        midfielder = request.form["midfielder"]
        forward = request.form["forward"]
        count_tournaments = request.form["count_tournaments"]
        list_tournaments = request.form["list_tournaments"]
        player_wikipedia_link = request.form["player_wikipedia_link"]
        player = Players(a,player_id, family_name, given_name, birth_date, goal_keeper, defender, midfielder,forward,count_tournaments,list_tournaments,player_wikipedia_link)
        db = current_app.config["db"]
        db.update_player(player)
        return redirect(url_for("players_page"))

def player_page(player_key):
    db = current_app.config["db"]
    player = db.get_player(player_key)
    return render_template("player.html", player=player)
    
def player_page_foreign(player_id):
    db = current_app.config["db"]
    player_id2 = '%' + player_id + '%'
    player = db.get_player_foreign(player_id2)
    return render_template("player.html", player = player)        

def awardwinners_page():
    db = current_app.config["db"]
    if request.method == "GET":
        
        awardwinners = db.get_awardwinners()
        awardwinners.sort(key=lambda x: x[1].key_id)
        return render_template("awardWinners.html", awardwinners=sorted(awardwinners))
    elif request.method== "POST":
        a = request.form.get("delete","")
        print(int(a))
        db.delete_awardwinner(int(a))
        return redirect(url_for("awardwinners_page"))

def awardwinners_add_page():
    if request.method == "GET":
        return render_template("awardwinners_edit.html")
    else:
        tournament_id = request.form["deneme"]
        tournament_name = request.form["tournament_name"]
        award_id = request.form["award_id"]
        award_name = request.form["award_name"]
        shared = request.form["shared"]
        player_id = request.form["player_id"]
        family_name = request.form["family_name"]
        given_name = request.form["given_name"]
        team_id = request.form["team_id"]
        team_name = request.form["team_name"]
        team_code = request.form["team_code"]
        Awardwinner = AwardWinners(0,tournament_id, tournament_name, award_id, award_name, shared, player_id, family_name, given_name,team_id,team_name,team_code)
        db = current_app.config["db"]
        referee_key = db.add_awardwinner(Awardwinner)
        return redirect(url_for("awardwinners_page", referee_key=referee_key))

def awardwinners_update_page():
    db = current_app.config["db"]
    a = request.args["awardwinner"]
    if request.method == "GET":
        awardwinner=db.get_awardwinner(int(a))
        return render_template("awardwinners_edit.html",awardwinner=awardwinner)
    elif request.method== "POST":
        tournament_id = request.form["deneme"]
        tournament_name = request.form["tournament_name"]
        award_id = request.form["award_id"]
        award_name = request.form["award_name"]
        shared = request.form["shared"]
        player_id = request.form["player_id"]
        family_name = request.form["family_name"]
        given_name = request.form["given_name"]
        team_id = request.form["team_id"]
        team_name = request.form["team_name"]
        team_code = request.form["team_code"]
        awardwinner = AwardWinners(a,tournament_id, tournament_name, award_id, award_name, shared, player_id, family_name, given_name,team_id,team_name,team_code)
        db = current_app.config["db"]
        db.update_awardwinner(awardwinner)
        return redirect(url_for("awardwinners_page"))
