from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "This is Home!!!"
    
    return app