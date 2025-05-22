import environ
import os

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
