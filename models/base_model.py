#!/usr/bin/env python3

from uuid import uuid4
from datetime import datetime

class BaseModel:
	"""
	BaseModel for tasks
	"""
	
	def __init__(self, description, status):
		self.id = uuid4()
		self.description = description
		self.status = status
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
	
	def __str__(self):
		return f"id: {self.id} — description: {self.description} — status: {self.status}"

	def to_dict(self):
		return self.__dict__
