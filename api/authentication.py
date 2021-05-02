from flask import request,Response,jsonify,current_app
from flask_resful import Resource

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)