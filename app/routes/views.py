from flask import Blueprint, jsonify, render_template, request
from ..database import load_jobs, load_job, submit_application

views = Blueprint('views', __name__)


@views.route('/')
def home():
    jobs = load_jobs()
    return render_template('home.html', jobs=jobs)


@views.route('/job/<id>')
def show_job(id):
    job = load_job(id)
    if not job:
        return 'Not Found', 404
    else:
        return render_template('jobDisplay.html', job=job)
    # return jsonify(job)


@views.route('/job/<id>/apply', methods=['GET', 'POST'])
def application_submit(id):
    # if request.form == 'POST':
    job = load_job(id)
    data = request.form
    submit_application(id, data)
    return render_template('application_submitted.html', application=data, job=job)
    # else:
    # render_template('home.html')
