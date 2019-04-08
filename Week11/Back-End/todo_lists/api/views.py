from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
from .models import Task
from .models import TaskList

def show_lists(request):
    l = TaskList.objects.all()
    json_lists=[c.to_json() for c in l]
    return JsonResponse(json_lists, safe=False)


def task_list_detail(request,pk):
    try:
        li = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)},safe=False)
    j_li=li.to_json()
    return JsonResponse(j_li)


def task_list_detail_task(request, pk):
    try:
        li = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    tasks = li.task_set.all()
    json_task = [p.to_json() for p in tasks]
    return JsonResponse(json_task, safe=False)


