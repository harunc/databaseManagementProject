from flask import Flask, render_template, request, redirect, url_for

import views
from database import Db
from teams import Teams
from referees import Referees

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')

    app.add_url_rule("/", view_func=views.home_page)

    app.add_url_rule("/teams", view_func=views.teams_page, methods = ["GET", "POST"])
    app.add_url_rule("/teams/<int:team_key>", view_func=views.team_page)
    app.add_url_rule("/teams/<string:team_id>", view_func=views.team_page_foreign) 
    app.add_url_rule("/new_team", view_func=views.team_add_page, methods=["GET", "POST"])
    app.add_url_rule("/update_team", view_func=views.team_update_page, methods=["GET", "POST"])

    app.add_url_rule("/bookings", view_func=views.bookings_page, methods = ["GET", "POST"])
    app.add_url_rule("/new_booking", view_func=views.booking_add_page, methods=["GET", "POST"])
    app.add_url_rule("/update_booking", view_func=views.booking_update_page, methods=["GET", "POST"])

    app.add_url_rule("/referees", view_func=views.referees_page, methods = ["GET", "POST"])
    app.add_url_rule("/referees/<int:referee_key>", view_func=views.referee_page) 
    app.add_url_rule("/referees/<string:referee_id>", view_func=views.referee_page_foreign) 
    app.add_url_rule("/new-referee", view_func=views.referee_add_page, methods=["GET", "POST"])
    app.add_url_rule("/refereesap", view_func=views.refereesap_page, methods = ["GET", "POST"])
    app.add_url_rule("/new-refereeap", view_func=views.refereeap_add_page, methods=["GET", "POST"])
    app.add_url_rule("/refereesap/<int:refereeap_key>", view_func=views.refereeap_page)
    app.add_url_rule("/update-referee",view_func=views.referee_update_page, methods=["GET", "POST"])


    app.add_url_rule("/players", view_func=views.players_page, methods = ["GET", "POST"])
    app.add_url_rule("/new-player", view_func=views.players_add_page, methods=["GET", "POST"])
    app.add_url_rule("/update-player", view_func=views.players_update_page, methods=["GET", "POST"])
    app.add_url_rule("/players/<string:player_id>", view_func=views.player_page_foreign)
    app.add_url_rule("/players/<int:player_key>", view_func=views.player_page)
    app.add_url_rule("/new-awardwinner", view_func=views.awardwinners_add_page, methods=["GET", "POST"])
    app.add_url_rule("/awardwinners", view_func=views.awardwinners_page, methods = ["GET", "POST"])
    app.add_url_rule("/update-awardwinner", view_func=views.awardwinners_update_page, methods=["GET", "POST"])



    db = Db("lastDB.db")
    app.config["db"] = db

    return app

def main():
    app = create_app()
    debug = app.config['DEBUG']
    port = app.config.get('PORT', 5000)
    app.run(host = '0.0.0.0', port = port, debug = debug)

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
