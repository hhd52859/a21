from flask import Blueprint
from apps.ext import db
from models import *

device_bp = Blueprint('device',__name__)
