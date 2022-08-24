import os
from app import create_app

CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='app.configs.config.DevelopmentConfig')
app = create_app(CONFIG_TYPE)

if __name__ == "__main__":
    app.run()