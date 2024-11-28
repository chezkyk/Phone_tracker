from flask import Flask

from app.routs.phone_blueprint import phone_bp

app = Flask(__name__)

app.register_blueprint(phone_bp)

if __name__ == '__main__':
    app.run(port=5000)