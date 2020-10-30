from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

from app import app, db

# Migration initieren und durchführen(init, migrate, upgrade)
app.config.from_object('config.DevelopmentConfig')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()