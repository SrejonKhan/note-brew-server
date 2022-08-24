from app import create_app
from app.configs.config import Config, DevelopmentConfig, TestingConfig, ProductionConfig

app = create_app(TestingConfig)

if __name__ == "__main__":
    app.run()