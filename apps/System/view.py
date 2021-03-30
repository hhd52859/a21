from flask import Blueprint
from apps.ext import db
from models import *

system_bp = Blueprint('system',__name__)
