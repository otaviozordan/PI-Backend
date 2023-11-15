import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '')##falta a chavezinha
    MONGO_URI = 'mongodb://localhost:--' ##perguntar para o zordan
    # Adicione outras configurações globais aqui

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    MONGO_URI = 'mongodb://localhost:27017/bancodetesteruanzin' #testes
    # Adicione configurações específicas de teste

class ProductionConfig(Config):
    DEBUG = False
    # Ative o modo de depuração apenas para desenvolvimento

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig  # Configuração padrão
}

def get_config(env):
    return config.get(env, config['default'])