from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class JobSelectionForm(FlaskForm):
    jobSelect = SelectField('Select Job', validators=[DataRequired()])
    submit = SubmitField('Select')

class MaterialPullForm(FlaskForm):
    materialID = StringField('Material ID', validators=[DataRequired()])
    materialLocation = StringField('Material Location', validators=[DataRequired()])
    materialSize = StringField('Material Size', validators=[DataRequired()])
    materialShape = StringField('Material Shape', validators=[DataRequired()])
    submit = SubmitField('Pull Material')

class ToolPullForm(FlaskForm):
    toolChecklist = TextAreaField('Tools Checklist', validators=[DataRequired()])
    submit = SubmitField('Pull Tools')

class MachineSetupForm(FlaskForm):
    setupTime = IntegerField('Setup Time', validators=[DataRequired()])
    submit = SubmitField('Setup Machine')

class InspectionReportForm(FlaskForm):
    inspectionReport = TextAreaField('Inspection Report', validators=[DataRequired()])
    submit = SubmitField('Submit Report')

class RunPartForm(FlaskForm):
    runTime = IntegerField('Run Time', validators=[DataRequired()])
    partStatus = SelectField('Part Status', choices=[('Good', 'Good'), ('Quarantine', 'Quarantine'), ('Scrap', 'Scrap')], validators=[DataRequired()])
    submit = SubmitField('Run Part')

class FinalCheckForm(FlaskForm):
    finalCheck = TextAreaField('Final Check', validators=[DataRequired()])
    remainingMaterial = StringField('Remaining Material', validators=[DataRequired()])
    submit = SubmitField('Final Check')

class JobSubmitForm(FlaskForm):
    submit = SubmitField('Submit Job')