#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Text

from .. import db

import json


class BaseModel:
    """
    Base DB Model
    
    Every table must have isDeleted, then can use the function of query with valid data !!!
    queryAll is the origin query function !!!
    """

    db = db

    def save(self):
        '''dave or update'''
        self.db.session.add(self)
        self.db.session.commit()

    def delete(self):
        '''delete by status'''
        self.isDeleted = 1
        self.save()

    def __str__(self):
        return json.dumps(self.__dict__)
        #return '<%s %s>' % (type(self).__name__ ,self.id)  

    def __repr__(self):
        return '<%s %s>' % (type(self).__name__ ,self.id)  

    @classmethod
    def deleteById(cls, id):
        res = cls.query.filter_by(id=id).first()
        if res:
            res.delete()

    @classmethod
    def query(cls):
        '''query of valid status'''
        return cls.query.filter(cls.isDeleted == 0)

    @classmethod
    def queryAll(cls):
        '''query with delete ones'''
        return cls.query

    @classmethod
    def queryById(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def queryByIds(cls, ids):
        return cls.query.filter(cls.id.in_(ids)).all()

