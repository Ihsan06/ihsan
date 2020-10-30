from app import db, ma
from flask_marshmallow import Marshmallow

# Sales Klasse erstellen
class Sales(db.Model):

    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True, nullable=True)
    filnr = db.Column(db.Integer, nullable=False)
    artnr = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=True)
    date = db.Column(db.Text)
    amount = db.Column(db.Integer, nullable=True)

    def __init__(self, id, filnr, artnr, discount, date, amount):
        self.id = id
        self.filnr = filnr
        self.artnr = artnr
        self.discount = discount
        self.date = date
        self.amount = amount

    #def __repr__(self):
     #   return '<id {}>'.format(self.id)


class SalesSchema(ma.Schema):
    class Meta:
        fields = ('id','filnr', 'artnr', 'discount', 'date', 'amount')

sale_schema = SalesSchema()
sales_schema = SalesSchema(many=True)