from .main import main

DEFAULT_BLUEPRINT = (
(main, ''),
)
def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)