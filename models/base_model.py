#!/usr/bin/env python3

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
	"""
	BaseModel for tasks
	"""
	id = 0
	
	def __init__(self, description, status='todo'):
		BaseModel.id += 1
		self.id = BaseModel.id
		self.description = description
		self.status = status
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
	
	
	def __str__(self):
		return f"id: {self.id} — description: {self.description} — status: {self.status}"

	def to_dict(self):
		return_dict = self.__dict__.copy()
		for k, v in return_dict.items():
			if isinstance(v, datetime):
				return_dict[k] = v.isoformat()
		return return_dict
		
	def save(self):
		obj = self.to_dict()
		models.storage.new(obj)
		models.storage.save()


