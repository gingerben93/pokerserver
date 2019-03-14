import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    user_password = db.Column(db.String(50))

class Game(db.Model):
    __tablename__ = 'Game'
    game_id = db.Column(db.Integer, primary_key=True)
    round_current = db.Column(db.Integer)
    round_max = db.Column(db.Integer)
    #string 13 long?
    community_cards_values = db.Column(db.String(20))
    community_cards_suits = db.Column(db.String(20))

class Participant(db.Model):
    __tablename__ = 'Participant'
    participant_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    game_id = db.Column(db.Integer, db.ForeignKey('Game.game_id'))
    #need to save for plalyers that server can't contact right away
    #hand_values = db.Column(db.String(20))
    #hand_suits = db.Column(db.String(20))
    score = db.Column(db.Integer)

class Hand(db.Model):
    __tablename__ = 'Hand'
    hand_id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('Participant.participant_id'))
    #string 13 long?
    hand_values = db.Column(db.String(20))
    hand_suits = db.Column(db.String(20))
    round_number = db.Column(db.Integer)

class Super_hand(db.Model):
    __tablename__ = 'Super_hand'
    super_hand_id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('Hand.hand_id'))
    #string 13 long?
    hand_values = db.Column(db.String(20))
    hand_suits = db.Column(db.String(20))
