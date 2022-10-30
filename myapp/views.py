from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Student
from myapp.task import async_task
from myproject.settings import BASE_DIR

def home(request):
    obj = Student.objects.all()
    context = {
        'data': obj
    }
    return render(request, 'data/data.html', context)


class HomeView(View):
    def get(self, request, *args, **kwargs):
        obj = Student.objects.all()
        context = {'data': obj}
        
        return render(request, 'data/homeview.html', context)


def add_product(request):
    if request.method == 'POST':
        id_col_data = request.POST.getlist('services')
        target_col = request.POST.get('target_col')
        file_name = request.POST.get('file_name')
        amz_columns_dict = {'id_col': id_col_data,
                            'target_col': target_col,
                            'wt_col': None}
        import os.path
        save_path = r"{}".format(BASE_DIR)
        # save_path = '/home/satyajit/Desktop/'
        if os.path.exists(save_path):
            try:
                name_of_file = file_name
                status = async_task.delay(save_path, name_of_file)
                print('status---->', status)
            except Exception as e:
                print('task error is ------>', e)
                return render(request,'data/error.html', {'message': 'async task error'})
        else:
            print('error occured')
        return HttpResponse('product added successfully')
    return render(request, 'add_product.html')

