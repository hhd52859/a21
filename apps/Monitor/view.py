from flask import Blueprint
from apps.ext import db
from models import *

monitor_bp = Blueprint('monitor',__name__)
