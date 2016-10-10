# coding=utf-8

from models import *
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

def set_user_information(dic):
    try:
    	print dic['username']
        user = User.objects.create(username = dic['username'])
    except IntegrityError:
        user = User.objects.get(pk = dic['username'])
    print dic['password']
    for attr in ['password', 'student_id', 'real_name', 'dept', 'tel', 'email']:
        # Again, __placeholder__ exists for the sake of database.tests
        setattr(user, attr, dic.get(attr, '__placeholder__'))
    user.full_clean()
    user.save()

def login(request):
    print "login"
    username, password = request.POST['account'], request.POST['password']
    try:
        user = User.objects.get(username=username)
        print password
        if user.password == password :
        	return JsonResponse({'status': 'ok'})
    	else :
    		return JsonResponse({
        		'status': 'error',
        		'error_message': u'用户名或密码错误！'
    		})		
    except ObjectDoesNotExist:
    	return JsonResponse({
        	'status': 'error',
        	'error_message': u'找不到这个用户！'
    	})