from app import db

class User(db.Model):
	__tablename__ = "users"
	
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	name = db.Column(db.String)
	email = db.Column(db.String,unique=True)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.id)

	def __init__(self, username, password, name, email):
		self.username = username
		self.password = password
		self.name = name
		self.email = email
	
	def __repr__(self):
		return "<User %r>" % self.username

class Lead(db.Model):
	__tablename__ = "leads"
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	telnumber = db.Column(db.String)
	email = db.Column(db.String)
	#contact_date = db.Column(db.

	def __init__(self, name, telnumber, email):
		self.name = name
		self.telnumber = telnumber
		self.email = email

	def __repr__(self):
		return "<Lead %r>" % self.id

