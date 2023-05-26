from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///\\flask\\flaskApp2\\app\\sqlite\\ShamieJobPortal.db')


def load_jobs():
    with engine.connect() as conn:
        jobs = conn.execute('SELECT * FROM jobs')
        job_dicts = []
        for job in jobs.all():
            job_dicts.append(dict(job))
        return job_dicts

def load_job(id):
    with engine.connect() as conn:
        job = conn.execute('SELECT * FROM jobs WHERE id = :val', val=id)
        rows = job.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])

def submit_application(job_id, data):
    with engine.connect() as conn:
        application = conn.execute('INSERT INTO application (job_id, name, email, linkedin, education, work, resume) VALUES (:job_id, :name, :email, :education, :linkedin, :work, :resume)', job_id=job_id, name=data['name'], email=data['email'], linkedin=data['linkedin'], education=data['education'], work=data['work'], resume=data['resume'])


# JOBS = [
#     {
#     'id': 1,
#     'post': 'Fitness Trainer',
#     'location': 'Karachi',
#     'salary': 'Rs. 100000'
#     },
#     {
#     'id': 2,
#     'post': 'Phsychologist',
#     'location': 'Karachi',
#     'salary': 'Rs. 60000'
#     },
#     {
#     'id': 3,
#     'post': 'Head Coach',
#     'location': 'Lahore'
#     # 'salary': 300000
#     },
#     {
#     'id': 4,
#     'post': 'Assistant to Head Coach',
#     'location': 'Rawalpindi',
#     'salary': 'Rs. 50000'
#     },
#     {
#     'id': 5,
#     'post': 'Data Analyst',
#     'location': 'Karachi',
#     'salary': 'Rs. 70000'
#     }
# ]
