from flask import render_template, request, redirect, url_for
from app import app
from app.models import Job, Material, Tool, InspectionReport
from app.forms import MaterialForm, ToolForm, InspectionReportForm, FinalCheckForm

@app.route('/')
@app.route('/index')
def index():
    jobs = Job.query.all()
    return render_template('index.html', title='Home', jobs=jobs)

@app.route('/job/<int:job_id>', methods=['GET', 'POST'])
def job(job_id):
    job = Job.query.get(job_id)
    if request.method == 'POST':
        if 'materialForm' in request.form:
            form = MaterialForm(request.form)
            if form.validate():
                material = Material(form.data)
                job.materials.append(material)
        elif 'toolForm' in request.form:
            form = ToolForm(request.form)
            if form.validate():
                tool = Tool(form.data)
                job.tools.append(tool)
        elif 'inspectionForm' in request.form:
            form = InspectionReportForm(request.form)
            if form.validate():
                report = InspectionReport(form.data)
                job.inspection_reports.append(report)
        elif 'finalCheckForm' in request.form:
            form = FinalCheckForm(request.form)
            if form.validate():
                job.final_check = form.data
                job.status = 'Complete'
        job.save()
        return redirect(url_for('job', job_id=job.id))
    else:
        materialForm = MaterialForm()
        toolForm = ToolForm()
        inspectionForm = InspectionReportForm()
        finalCheckForm = FinalCheckForm()
        return render_template('job.html', title='Job', job=job, materialForm=materialForm, toolForm=toolForm, inspectionForm=inspectionForm, finalCheckForm=finalCheckForm)

@app.route('/error')
def error():
    return render_template('error.html', title='Error')