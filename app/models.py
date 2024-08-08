from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(100), nullable=False)
    part_number = db.Column(db.String(100), nullable=False)
    rev_number = db.Column(db.String(100), nullable=False)
    material = db.Column(db.String(100), nullable=False)
    part_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    steps = db.relationship('Step', backref='job', lazy=True)

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    shape = db.Column(db.String(100), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(100), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    step_number = db.Column(db.Integer, nullable=False)
    step_name = db.Column(db.String(100), nullable=False)
    step_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

class InspectionReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_data = db.Column(db.Text, nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

class FinalCheck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_check = db.Column(db.String(100), nullable=False)
    part_status = db.Column(db.String(100), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)