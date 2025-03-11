from market import db, bcrypt, login_manager  #sadrzi modele koji su u stvari tabele u bazi podataka
from flask_login import UserMixin   # sadrzi modele koje flask zahteva od LoginManagera: is_auth, is_active,..

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): # za user authentication
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)  # kolona za enkriptovanu lozinku
    budget = db.Column(db.Integer(), nullable=False, default=10000) # default=1000 --> koliko tokena imaju kad se loguju prvi put
    items = db.relationship('Item', backref='owned_user', lazy=True) # backref nam omogucava da vidimo koji vlasnik poseduje koji proizvod

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]}$"
        else:
            return f"{self.budget}$"

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password) # vraca ili tacno ili netacno
    
    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

    def can_sell(self, item_obj):
        return item_obj in self.items
            
            

class Item(db.Model):      # ovako se pravi model koji posle prelazi u tabelu u nasoj db
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)  # ovako se prave kolone u toj tabeli Item
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id')) # da bi se ostvarila veza izmedju ove dve tabele

    def __repr__(self):
        return f"Item {self.name}"
    
    def buy(self, user):
        self.owner = user.id 
        user.budget -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner = None
        user.budget += self.price
        db.session.commit()