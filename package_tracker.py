from flask import Flask, render_template
from app.config import Config
from app.routes import root, new_package

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(root.bp)
app.register_blueprint(new_package.bp)
