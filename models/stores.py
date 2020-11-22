from db import db
#from models.item import ItemsModel
class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    items = db.relationship('ItemsModel',lazy='dynamic')

    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name':self.name,'items':[x.json() for x in self.items.all()]}
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def query_all_in_table(cls):
        return cls.query.all()