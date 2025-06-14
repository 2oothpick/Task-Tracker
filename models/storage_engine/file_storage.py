#!/usr/bin/env python3

import json

class FileStorage:
	
	__file_name = 'file.json'
	__objs = None
	
	def save(self):
		""" serializes self.__objs to self.__file_name """
		with open(self.__file_name, 'w') as file:
			json.dump(self.__objs,file)
	
	def new(self, obj):
		""" adds obj to self.__objs """
		self.__objs.append(obj)
	
	def reload(self):
		"""
		deserializes objects in self.__file_name
		and returns them to self.__objs
		"""
		with open(self.__file_name, 'r') as file:
			self.__objs = json.load(file)
	
	def all(self):
		""" returns all objects stored in the file """
		return self.__objs
	
	def delete(self, obj):
		pass
