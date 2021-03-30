from flask import Blueprint
from apps.ext import db
from models import *

alarm_bp = Blueprint('alarm',__name__)
