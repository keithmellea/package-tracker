from flask_sqlalchemy import SQLAlchemy
from map.map import advance_delivery, DELIVERED
from sqlalchemy.orm import relationship
from flask_login import UserMixin

db = SQLAlchemy()

class Package(db.Model):
    __tablename__ = 'packages'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(255))
    recipient = db.Column(db.String(255))
    origin = db.Column(db.String(255))
    destination = db.Column(db.String(255))
    location = db.Column(db.String(255))
    sender.id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    sender = relationship("User", back_populates = "packages")

    @staticmethod
    def advance_all_locations():
        packages = Package.query.all()
        for package in packages:
            if package.location is not DELIVERED:
                package.location = advance_delivery(package.location, package.destination)

        db.session.commit()


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Email(100), nullable=False)
    hashed_password = db.Column(db.String(200), nullable=False)

    packages = relationship("Package", back_populates= "sender")