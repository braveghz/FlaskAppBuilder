# coding=utf-8
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

mindate = datetime.date(datetime.MINYEAR, 1, 1)
# datetime.MINYEAR:The smallest year number allowed in a date or datetime object. MINYEAR is 1.


class ContactGroup(Model):
    """
    联系人分组
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Gender(Model):
    """
    性别
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Contact(Model):
    """
    联系人详细信息 id/姓名/地址/生日/电话/联系人分组/性别
    """
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)
    address = Column(String(512))
    birthday = Column(Date, nullable=True)
    phone = Column(String(32))
    contact_group_id = Column(
        Integer,
        ForeignKey('contact_group.id'),
        nullable=False)
    contact_group = relationship("ContactGroup")
    gender_id = Column(Integer, ForeignKey('gender.id'), nullable=False)
    gender = relationship("Gender")

    def __repr__(self):
        return self.name

    def month_year(self):
        """
        :return: 生日的年月
        """
        date = self.birthday or mindate
        return datetime.datetime(date.year, date.month, 1) or mindate

    def year(self):
        """
        :return: 生日的年份 1月1日
        """
        date = self.birthday or mindate
        return datetime.datetime(date.year, 1, 1)
