from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, time

db = SQLAlchemy()

##############################################################################

class Student(db.Model):
    """Student from mind body app"""

    __tablename__ = "student"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_first = db.Column(db.String(64), nullable=True)
    name_last = db.Column(db.String(64), nullable=True)
    rank_stripes = db.Column(db.Integer, nullable=True)
    rank_id = db.Column(db.Integer, db.ForeignKey('rank.id'), nullable=True)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=True)

    # define a relationship to Rank
    rank = db.relationship("RankType",
                           backref=db.backref("students", order_by=id))
    # define a relationship to Program
    program = db.relationship("Program",
                           backref=db.backref("students", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Student id={1} name={2}>".format(self.id, self.name_first + ' ' + name_last)

class Coach(db.Model):
    """Coach user created in gorillas app"""

    __tablename__ = "coach"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(124), nullable=False, unique=True)
    name_first = db.Column(db.String(64), nullable=True, unique=True)
    name_last = db.Column(db.String(64), nullable=True, unique=True)
    password_salt = db.Column(db.String(20), nullable=True)
    password_hash = db.Column(db.String(64), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)


    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Coach id={} email{}>".format(self.id, self.email)

class ClassInstance(db.Model):
    """tbd"""

    __tablename__ = "class_instance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_schedule_id = db.Column(db.Integer, db.ForeignKey('class_schedule.id'), nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.String(500), nullable=True)
    substitute_coach_id = db.Column(db.Integer, db.ForeignKey('coach.id'), nullable=True)

    # define a relationship to Coach
    substitute_coach = db.relationship("Coach",
                           backref=db.backref("substituted_classes", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<ClassInstance id={} date={}>" % (self.id, self.date)

class ClassSchedule(db.Model):
    """tbd"""

    __tablename__ = "class_schedule"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=True)
    day_of_week = db.Column(db.String(9), nullable=False)
    time = db.Column(db.Time, nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<ClassSchedule id={} day_of_week={} time={}>" % (self.id, self.day_of_week, self.time)

class ClassScheduleCoach(db.Model):
    """tbd"""

    __tablename__ = "class_schedule_coach"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_schedule_id = db.Column(db.Integer, db.ForeignKey('class_schedule.id'), nullable=True)
    coach_id = db.Column(db.Integer, db.ForeignKey('coach.id'), nullable=True)

    # define a relationship to Class Schedule
    class_schedule = db.relationship("ClassSchedule",
                           backref=db.backref("class_schedule_coach", order_by=id))

    # define a relationship to Coach
    coach = db.relationship("Coach",
                           backref=db.backref("class_schedule_coach", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<ClassScheduleCoach id={} class_schedule_id={} coach_id={}>" % (self.id, self.class_schedule_id, self.coach_id)

class StudentVisit(db.Model):
    """tbd"""

    __tablename__ = "student_visit"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    class_instance_id = db.Column(db.Integer, db.ForeignKey('class_instance.id'), nullable=False)
    attendance_id = db.Column(db.Integer, db.ForeignKey('attendance.id'), nullable=False)
    notes = db.Column(db.String(500), nullable=True)

    # define a relationship to Student
    student = db.relationship("Student",
                           backref=db.backref("student_visits", order_by=id))

    # define a relationship to ClassInstance
    class_instance = db.relationship("ClassInstance",
                           backref=db.backref("student_visits", order_by=id))

    # define a relationship to AttendanceType
    attendance = db.relationship("AttendanceType",
                           backref=db.backref("student_visits", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<StudentVisit id={} student_id = {} class_instance_id={} attendance_id={}>" % (self.id, self.student_id, self.class_instance_id, self.attendance_id)

class AttendanceType(db.Model):
    """tbd"""

    __tablename__ = "attendance_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    abbr = db.Column(db.String(1), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<AttendanceType id={} name={}>" % (self.id, self.name)

class Enrollment(db.Model):
    """tbd"""

    __tablename__ = "enrollment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    class_schedule_id = db.Column(db.Integer, db.ForeignKey('class_schedule.id'), nullable=False)

    # define a relationship to Student
    student = db.relationship("Student",
                           backref=db.backref("enrollment", order_by=id))

    # define a relationship to Class Schedule
    class_schedule = db.relationship("class_schedule",
                           backref=db.backref("enrollment", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<AttendanceType id={} name={}>" % (self.id, self.name)

class RankType(db.Model):
    """tbd"""

    __tablename__ = "rank_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    abbr = db.Column(db.String(5), nullable=True)
    order = db.Column(db.Integer, nullable=False, unique=True)

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<RankType id={} name={}>" % (self.id, self.name)

class Program(db.Model):
    """tbd"""

    __tablename__ = "program"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    order = db.Column(db.Integer, nullable=False, unique=True)

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<Program id={} name={}>" % (self.id, self.name)

class StudentLifeSkill(db.Model):
    """tbd"""

    __tablename__ = "student_life_skill"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    life_skill_instance_id = db.Column(db.Integer, db.ForeignKey('life_skill_instance.id'), nullable=False)
    complete_date = db.Column(db.DateTime, nullable=True)
    stripe_given_date = db.Column(db.DateTime, nullable=True)

    # define a relationship to Student
    student = db.relationship("Student",
                           backref=db.backref("student_life_skill", order_by=id))

    # define a relationship to LifeSkillInstance
    life_skill_instance = db.relationship("LifeSkillInstance",
                           backref=db.backref("student_life_skills", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<StudentLifeSkill id={} student_id={} life_skill_instance_id={}>" % (self.id, self.student_id, self.life_skill_instance_id)

class LifeSkillInstance(db.Model):
    """tbd"""

    __tablename__ = "life_skill_instance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    life_skill_master_id = db.Column(db.Integer, db.ForeignKey('life_skill_master.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=True)

    # define a relationship to LifeSKillMaster
    life_skill_master = db.relationship("LifeSKillMaster",
                           backref=db.backref("life_skill_instance", order_by=id))

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<LifeSkillInstance id={} life_skill_master_id={} start_date={}>" % (self.id, self.life_skill_master_id, self.start_date)

class LifeSkillMaster(db.Model):
    """tbd"""

    __tablename__ = "life_skill_master"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    order = db.Column(db.Integer, nullable=False, unique=True)
    version = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""
        return "<LifeSkillMaster id={} name={}>" % (self.id, self.name)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/gorillas'
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    # app.config['SQLALCHEMY_RECORD_QUERIES'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."