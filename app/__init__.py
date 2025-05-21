from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/healthcheck')
    def healthcheck():
        return jsonify({'status': 'ok'})

    # Тут інші ініціалізації, наприклад, бази даних, маршрути

    return app
