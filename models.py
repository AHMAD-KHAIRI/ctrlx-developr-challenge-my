from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin

# create the extension
db = SQLAlchemy()


#   Create a User table for all your registered users. 
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(250))
    plcScores = relationship("PLC", back_populates = "user")
    plc_button_pressed = db.Column(db.Boolean, default=False)
    plc_start_time = db.Column(db.DateTime)
    plc_end_time = db.Column(db.DateTime)
    opcuaScores = relationship("Opcua", back_populates = "user")
    opcua_button_pressed = db.Column(db.Boolean, default=False)
    opcua_start_time = db.Column(db.DateTime)
    opcua_end_time = db.Column(db.DateTime)
    noderedScores = relationship("Nodered", back_populates = "user")
    nodered_button_pressed = db.Column(db.Boolean, default=False)
    nodered_start_time = db.Column(db.DateTime)
    nodered_end_time = db.Column(db.DateTime)
    motionScores = relationship("Motion", back_populates = "user")
    motion_button_pressed = db.Column(db.Boolean, default=False)
    motion_start_time = db.Column(db.DateTime)
    motion_end_time = db.Column(db.DateTime)
    webiqScores = relationship("Webiq", back_populates = "user")
    webiq_button_pressed = db.Column(db.Boolean, default=False)
    webiq_start_time = db.Column(db.DateTime)
    webiq_end_time = db.Column(db.DateTime)
    ideScores = relationship("IDE", back_populates = "user")
    ide_button_pressed = db.Column(db.Boolean, default=False)
    ide_start_time = db.Column(db.DateTime)
    ide_end_time = db.Column(db.DateTime)
    results = relationship("Result", back_populates = "user")


# Create a Result table for all groups
class Result(db.Model):
    __tablename__ = "results"
    id = db.Column(db.Integer, primary_key=True)    
    group_name = db.Column(db.String(50), nullable=False)
    total_time = db.Column(db.String(50), nullable=False)
    total_score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates = "results")

# Create a table to store the scores for PLC Challenge
class PLC(db.Model):
    __tablename__ = "plcScores"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates = "plcScores")

# Create a table to store the scores for OPCUA Challenge
class Opcua(db.Model):
    __tablename__ = "opcuaScores"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates = "opcuaScores")

# Create a table to store the scores for Node-RED Challenge
class Nodered(db.Model):
    __tablename__ = "noderedScores"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates = "noderedScores")

# Create a table to store the scores for Motion Challenge
class Motion(db.Model):
    __tablename__ = "motionScores"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates = "motionScores")

# Create a table to store the scores for WebIQ Challenge
class Webiq(db.Model):
    __tablename__ = "webiqScores"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates = "webiqScores")

# Create a table to store the scores for IDE Challenge
class IDE(db.Model):
    __tablename__ = "ideScores"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates = "ideScores")

# Create a Registration table for users.
# class Registration(db.Model):
#     __tablename__ = "registration"
#     id = db.Column(db.Integer, primary_key=True)
#     group_name = db.Column(db.String(250), nullable=False)
    # group_member_one = db.Column(db.String(250), nullable=False)
    # group_member_two = db.Column(db.String(250), nullable=False)
    # group_member_three = db.Column(db.String(250), nullable=False)
    # group_member_four = db.Column(db.String(250), nullable=False)
    # sector_categories = db.Column(db.String(250), nullable=False)
    # occupation = db.Column(db.String(250), nullable=False)
    # education = db.Column(db.String(250), nullable=False)
    # handphone = db.Column(db.String(100), nullable=False)
    # email = db.Column(db.String(100), nullable=False, unique=True)
    # password = db.Column(db.String(100), nullable=False)
    # interest_categories = db.Column(db.String(250), nullable=False)