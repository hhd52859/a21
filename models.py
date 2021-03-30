# 此文件存放数据库的类模型
from apps.ext import db


# 用户
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(10), primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    inspect_list = db.relationship('inspect_data', backref='user', cascade='all, delete-orphan', passive_deletes=True)
    record_list = db.relationship('record', backref='user', cascade='all, delete-orphan', passive_deletes=True)


# 桥
class Bridge(db.Model):
    __tablename__ = 'bridge'
    id = db.Column(db.String(10), primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(50),nullable = False)
    state = db.Column(db.Boolean,nullable = False)
    sensor_list = db.relationship('sensor', backref='bridge', cascade='all, delete-orphan', passive_deletes=True)


# 传感器
class Sensor(db.Model):
    __tablename__ = 'sensor'
    id = db.Column(db.String(10), primary_key=True, autoincrement=True)
    type = db.Column(db.String(10),nullable=False) # 传感器类型
    name = db.Column(db.String(10),nullable=False) # 传感器名
    long = db.Column(db.Boolean,nullable=False) # 是否是长时传感器
    bridge_id = db.Column(db.String(10), db.ForeignKey('bridge.id', ondelete='CASCADE'), nullable=False) # 所属桥梁id
    error_data_list = db.relationship('error_data', backref='sensor', cascade='all, delete-orphan', passive_deletes=True)
    raw_data_list = db.relationship('raw_data', backref='bridge', cascade='all, delete-orphan', passive_deletes=True)


# 原始数据
class RawData(db.Model):
    __tablename__ = 'raw_data'
    id = db.Column(db.String(10), primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullable=False)
    state = db.Column(db.Boolean, nullable=False)
    sensor_id = db.Column(db.String(10), db.ForeignKey('bridge.id', ondelete='CASCADE'), nullable=False)


# 长时预测
class PredictLong(db.Model):
    __tablename__ = 'predict_long'
    id = db.Column(db.String(10), primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=True)
    # 其余数据待定


# 短时预测
class PredictShort(db.Model):
    __tablename__ = 'predict_short'
    id = db.Column(db.String(10), primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=True)
    # 其余数据待定


# 异常数据
class ErrorData(db.Model):
    __tablename__ = 'error_data'
    id = db.Column(db.String(10), primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=True)
    value = db.Column(db.Float,nullable=False)
    sensor_id = db.Column(db.String(10),db.ForeignKey('bridge.id',ondelete='CASCADE'),nullable=False)


# 巡检数据
class InspectData(db.Model):
    __tablename__ = 'inspect_data'
    id = db.Column(db.String(10), primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=True)
    sensor_id = db.Column(db.String(10),nullable=True)
    sensor_state = db.Column(db.Boolean,nullable=True)
    bridge_id = db.Column(db.String(10),nullable=True)
    bridge_state = db.Column(db.Boolean,nullable=True)
    picture_route = db.Column(db.String(50),nullable=True) # 图片文件路径
    remark = db.Column(db.String(200),nullable=True)
    user_id = db.Column(db.String(10), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)


# 用户操作日志
class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.String(10), primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=False)
    operation = db.Column(db.String(20),nullable = False)
    user_id = db.Column(db.String(10), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)