from .db import db

class ProstheticTool(db.Model):
    __tablename__ = 'prosthetic_tools'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.Text)
    spirit_emblem_cost = db.Column(db.Integer)

