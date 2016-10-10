# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.fields import FieldDoesNotExist
from django.core.validators import *
from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.conf import settings
import traceback


# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=20, primary_key=True)
	password = models.CharField(max_length=32)
	student_id = models.CharField(max_length=20)
	real_name = models.CharField(max_length=20)
	dept = models.CharField(max_length=40)
	tel = models.CharField(
		max_length=20,
		validators=[
			RegexValidator(
			regex=r'^\d{11}$',
				message='请输入一个合法的电话号码'
			)
		]
	)
	email = models.CharField(
		max_length=254,
		validators=[
		EmailValidator(
			message='请输入一个合法的邮件地址'
			)
		]
	)

	def information_filled(self):
		try:
			self.full_clean()
			return True
		except ValidationError:
			return False

	def __unicode__(self):
		return u'%s(%s)' % (self.student_id, self.real_name)
