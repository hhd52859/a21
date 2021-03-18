from flask import Blueprint
from apps.ext import db
from models import *

user_bp = Blueprint('user',__name__)

