from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), unique=True)
    last_name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    is_active = db.Column(db.Boolean(), default=True)
    profile = db.relationship("Profile", backref="user", uselist=False)

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'is active': self.is_active,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default="unknown")
    lastname = db.Column(db.String(100), default="unknown")
    fav_char = db.relationship('People', secondary="favorite_characters")
    fav_plan = db.relationship("Planet", secondary="favorite_planets")
    fav_vehic = db.relationship("Vehicle", secondary="favorite_vehicles")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def get_fav_chars(self):
        return (list(map(lambda char: char.name, self.fav_char)))

    def get_fav_plans(self):
        return (list(map(lambda plan: plan.name, self.fav_plan)))

    def get_fav_vehics(self):
        return (list(map(lambda plan: plan.name, self.fav_vehic)))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "user id": self.user_id,
            "username": self.user.username,
            "active": self.user.is_active,
            "liked characters": self.get_fav_chars(),
            "liked planets": self.get_fav_plans(),
            "liked vehicles": self.get_fav_vehics(),
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    picture = db.Column(db.String(100), default="https://dummyimage.com/300X200/dbdbdb/000")
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(100))
    skin_color = db.Column(db.String(100))
    eye_color = db.Column(db.String(100))
    birth_year = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture":self.picture,
            "height": self.height,
            "mass": self.mass,
            "hair color": self.hair_color,
            "skin color": self.skin_color,
            "eye color": self.eye_color,
            "birth year": self.birth_year,
            "gender": self.gender,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique = True, default="unknown")
    picture = db.Column(db.String(100), default="https://dummyimage.com/300X200/dbdbdb/000")
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(100), default="unknown")
    gravity = db.Column(db.String(100), default="unknown")
    terrain = db.Column(db.String(100), default="unknown")
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture":self.picture,
            "rotation period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface water": self.surface_water,
            "population": self.population,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    picture = db.Column(db.String(250), default="https://dummyimage.com/300X200/dbdbdb/000")
    model = db.Column(db.String(100), unique=True)
    manufacturer = db.Column(db.String(100))
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    max_atmosphering_speed = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    consumables = db.Column(db.String(100))
    vehicle_class = db.Column(db.String(100))
   
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "picture":self.picture,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost in credits": self.cost_in_credits,
            "length": self.length,
            "max atmosphering speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "vehicle class": self.vehicle_class
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Favorite_characters(db.Model):
    __tablename__ = 'favorite_characters'
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), primary_key=True) 
    character_id = db.Column(db.Integer, db.ForeignKey('people.id'), primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Favorite_planets(db.Model):
    __tablename__ = 'favorite_planets'
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), primary_key=True) 
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Favorite_vehicles(db.Model):
    __tablename__ = 'favorite_vehicles'
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'), primary_key=True) 
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()