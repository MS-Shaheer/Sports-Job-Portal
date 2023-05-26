from flask import Blueprint, jsonify, render_template
from ..database import load_jobs

apiView = Blueprint('apiView', __name__)

@apiView.route('/api/jobsData')
def jobsData():
    jobs = load_jobs()
    return jsonify(jobs)
