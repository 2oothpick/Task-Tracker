#!/usr/bin/env python3

from uuid import uuid4
from datetime import datetime
import models
from random import randint


class BaseModel:
    """
    BaseModel for tasks
    """

    def __init__(self, description, status='todo'):
        self.id = self.set_id()
        self.description = description
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def set_id(self):
        ids_list = [obj['id'] for obj in models.storage.all()]
        max_id = max(ids_list)
        id = randint(0, max_id + 1)
        if id in ids_list:
            id = max_id + 1
        return id

    def to_dict(self):
        return_dict = self.__dict__.copy()
        for k, v in return_dict.items():
            if isinstance(v, datetime):
                return_dict[k] = v.isoformat()
        return return_dict

    def save(self):
        self.updated_at = datetime.now()
        obj = self.to_dict()
        models.storage.new(obj)
        models.storage.save()
