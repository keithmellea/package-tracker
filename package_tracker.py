from flask import Flask, render_template
from flask_migrate import Migrate
from app.config import Config
from app.routes import root, new_package
from app.models import Package, db

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(root.bp)
app.register_blueprint(new_package.bp)

db.init_app(app)
migrate = Migrate(app, db)
