#!/usr/bin/python3
"""Defines the BaseModel Class"""
from datetime import datetime
import models
from uuid import uuid4

class BaseModel:
	"""The BaseModel of the HBNB project"""

	def __init__(self, *args, **kwargs):
		"""Initialize a new BaseModel
		Arguments:
				*args: Unused
				**kwargs: key/value pairs of attributes
		"""
		tFormat = "%Y-%m-%dT%H:%M:%S.%f"
		self.id = str(uuid4())
		self.created = datetime.today()
		self.updated = datetime.today()
		if len(kwargs) != 0:
			for key, value in kwargs.items():



