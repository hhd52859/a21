from flask import Blueprint
from apps.ext import db
from models import *
import json

overview_bp = Blueprint('overview',__name__)


@overview_bp.route('/')
def Overview():
    bridgeNum = Bridge.query.count()
    deviceNum = Sensor.query.count()
    alarmNum = ErrorData.query.count()
    data = {
        'bridgeNum':bridgeNum,
        'deviceNum':deviceNum,
        'alarmNum':alarmNum
    }
    return json.dumps(data)


@overview_bp.route('/notice')
def Notice():
    notice = "中小型桥梁监测数据管理后台正式上线，欢迎业界朋友和政府领导莅临指导工作。"
    return json.dumps(notice)


@overview_bp.route('/log')
def Log():
    log = "系统升级优化<br>大数据可视化图表优化<br>新增微信公众号通知<br>新增设置数据导出功能"
    return json.dumps(log)


@overview_bp.route('/chart')
def Chart():

    return json.dumps({})