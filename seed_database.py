"""Utility file to seed gorillas database with dummy data from seed_data file"""

from model import Student, Coach, ClassInstance, ClassSchedule, ClassScheduleCoach
from model import StudentClassInstance, AttendanceType, StudentClassSchedule, RankType, Program
from model import StudentLifeSkill, LifeSkillInstance, LifeSkillMaster
from model import connect_to_db, db
from server import app
from datetime import datetime, time
import json

import os
import binascii

def load_coach():
    """Load coach from seed_data into database."""
    tablename = 'coach'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = Coach(
            name_first=item['name_first'],
            name_last=item['name_last'],
            email=item['email']
            )
        db.session.add(new_item)
    db.session.commit()

def load_rank_type():
    """Load rank type from seed_data into database."""
    tablename = 'rank_type'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = RankType(
            name=item['name'],
            abbr=item['abbr'],
            order=item['order']
            )
        db.session.add(new_item)
    db.session.commit()

def load_program():
    """Load program from seed_data into database."""
    tablename = 'program'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = Program(
            name=item['name'],
            order=item['order']
            )
        db.session.add(new_item)
    db.session.commit()

def load_student():
    """Load student from seed_data into database."""
    tablename = 'student'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = Student(
            name_first=item['name_first'],
            name_last=item['name_last'],
            rank_stripes=item['rank_stripes'],
            rank_type_id=item['rank_type_id'],
            program_id=item['program_id']
            )
        db.session.add(new_item)
    db.session.commit()

def load_class_schedule():
    """Load class schedule from seed_data into database."""
    tablename = 'class_schedule'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = ClassSchedule(
            name=item['name'],
            day_of_week=item['day_of_week'],
            time=item['time']
            )
        db.session.add(new_item)
    db.session.commit()

def load_class_instance():
    """Load class instance from seed_data into database."""
    tablename = 'class_instance'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = ClassInstance(
            class_schedule_id=item['class_schedule_id'],
            date=item['date']
            )
        db.session.add(new_item)
    db.session.commit()

def load_class_schedule_coach():
    """Load class schedule coach from seed_data into database."""
    tablename = 'class_schedule_coach'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = ClassScheduleCoach(
            class_schedule_id=item['class_schedule_id'],
            coach_id=item['coach_id']
            )
        db.session.add(new_item)
    db.session.commit()

def load_attendance_type():
    """Load attendance type from seed_data into database."""
    tablename = 'attendance_type'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = AttendanceType(
            name=item['name'],
            abbr=item['abbr']
            )
        db.session.add(new_item)
    db.session.commit()

def load_student_class_instance():
    """Load student class instance type from seed_data into database."""
    tablename = 'student_class_instance'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = StudentClassInstance(
            student_id=item['student_id'],
            class_instance_id=item['class_instance_id'],
            attendance_id=item['attendance_id']
            )
        db.session.add(new_item)
    db.session.commit()

def load_student_class_schedule():
    """Load student class schedule type from seed_data into database."""
    tablename = 'student_class_schedule'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = StudentClassSchedule(
            student_id=item['student_id'],
            class_schedule_id=item['class_schedule_id']
            )
        db.session.add(new_item)
    db.session.commit()

def load_life_skill_master():
    """Load life skill master class schedule type from seed_data into database."""
    tablename = 'life_skill_master'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = LifeSkillMaster(
            name=item['name'],
            order=item['order'],
            version=item['version']
            )
        db.session.add(new_item)
    db.session.commit()

def load_life_skill_instance():
    """Load life skill instance class schedule type from seed_data into database."""
    tablename = 'life_skill_instance'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = LifeSkillInstance(
            life_skill_master_id=item['life_skill_master_id'],
            start_date=item['start_date']
            )
        db.session.add(new_item)
    db.session.commit()

def load_student_life_skill():
    """Load student life skill class schedule type from seed_data into database."""
    tablename = 'student_life_skill'
    data = jsonify_seed_data(tablename)

    for item in data[tablename]:
        new_item = StudentLifeSkill(
            student_id=item['student_id'],
            life_skill_instance_id=item['life_skill_instance_id']
            )
        db.session.add(new_item)
    db.session.commit()

def jsonify_seed_data(tablename):
    """tbd"""
    with open("seed_data/{}.json".format(tablename)) as data_file:
        data = json.load(data_file)

    return data


if __name__ == "__main__":
    connect_to_db(app)
    db.drop_all()
    db.create_all()

    # import pdb; pdb.set_trace()

    load_coach()
    load_rank_type()
    load_program()
    load_student()
    load_class_schedule()
    load_class_instance()
    load_class_schedule_coach()
    load_attendance_type()
    load_student_class_instance()
    load_student_class_schedule()
    load_life_skill_master()
    load_life_skill_instance()
    load_student_life_skill()
