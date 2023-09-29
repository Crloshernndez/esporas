import os

from . import base

environment = os.environ.get('ENVIROMENT', 'development')

if environment == 'production':
    from .production import *
elif environment == 'testing':
    from .testing import *
else:
    from .development import *
