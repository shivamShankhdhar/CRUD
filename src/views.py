from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Task

def home(request):
	task = Task.objects.all()
	task_count = Task.objects.all().count()
	template_name = 'home.html'
	context = {'task':task, 'task_count':task_count}
	return render(request, template_name, context)

def post_data(request):
	if request.method == 'POST':
		task = request.POST.get('task')
		# print(f'task is {task}')
		db_task = Task.objects.filter(name__icontains = task)
		print(f' dbtask {db_task}')
		if len(db_task) or task == '':
			# print("Task is there")
			messages.warning(request, 'Failure! Task already there or task cannot be empty')
		# elif task == '':
		# 	messages.warning(request, 'Failure! Please type some value ')
		else:
			task_save = Task(name = task)
			task_save.save()
			messages.success(request, f'Success! Task " {task } " added')
		# get = Task.objects.get_or_create(
		# 		name = task
		# 	)
		# print(get)
	
		# if not get[1] :
		# 	messages.info(request, "already there")
	return redirect('/')


def delete_task(request, id):
	task = Task.objects.get(id = id)   # get is useful when only single item reterieved 
	messages.success(request, f' Success! " {task } " Task  deleted')
	task.delete()
	return redirect('/')


def task_cross_off(request, id):
	task = Task.objects.filter(id = id)
	task.update(is_active = False)
	# print(task.is_active)
	messages.success(request, 'crossed off')
	return redirect('/')

def un_cross(request, id):
	task = Task.objects.filter(id = id)
	task.update(is_active = True)
	# print(task.is_active)
	messages.success(request, f'un crossed')
	return redirect('/')