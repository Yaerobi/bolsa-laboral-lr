from flask_restplus import Api
from flask import Blueprint

from app.main.controller.user_controller import api as user_ns
from app.main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='IT Jobs La Rioja',
          version='1.0',
          description='IT jobs La Rioja'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)

