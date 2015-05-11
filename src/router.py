__author__ = 'chrisshroba'

from app import app

for module in modules:
    app.register_blueprint(module.blueprint, **module.rules)
