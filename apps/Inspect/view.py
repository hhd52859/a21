from flask import Blueprint
from apps.ext import db
from models import *

inspect_bp = Blueprint('inspect',__name__)
