from flask import request, jsonify
from .models import Task
from .database import db

def register_routes(app):
    @app.route('/')
    def index():
        return 'Todo Service API'

    @app.route('/healthcheck')
    def healthcheck():
        return 'OK', 200

    @app.route('/tasks', methods=['POST'])
    def create_task():
        data = request.json
        task = Task(title=data['title'])
        db.session.add(task)
        db.session.commit()
        return jsonify({"id": task.id, "title": task.title, "done": task.done}), 201

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([{"id": t.id, "title": t.title, "done": t.done} for t in tasks])
