from django.views.generic.base import View
# Create your views here.
from django.http import HttpResponse


class AboutUs(View):
    def get(self, request, *args, **kwargs):
        context = {
        "data":"hello world",
        "list": [1,2,3,4,5,6]
            }
        return render(request, 'aboutus.html', context)

    def post(self, request, *args, **kwargs):
        context = {
        "data":"hello world",
        "list": [1,2,3,4,5,6]
            }
        return render(request, 'post.html', context)

    def put(self, request, *args, **kwargs):
        context = {
        "data":"hello world",
        "list": [1,2,3,4,5,6]
            }
        return render(request, 'aboutus.html', context)


#form handing
#form logic
#form validation
#form rendering
def add_product(request):
    if request.method == 'POST':
        id_col_data = request.POST.getlist('services')
        onedata = request.POST.get('onedata')
        print('id_col_data------>', id_col_data)
        print('onedata------>', type(onedata))
        amz_columns_dict = {'id_col': id_col_data,
                            'target_col': onedata,
                            # 'time_index_col': 'G_WEEK',
                            # 'static_num_col_list': [],
                            # 'static_cat_col_list': ['BrandCode'],
                            # 'temporal_known_num_col_list':  ['Product_discount'],
                            # 'temporal_unknown_num_col_list': [],
                            # 'temporal_known_cat_col_list': ['M'],
                            # 'temporal_unknown_cat_col_list': [],
                            # 'strata_col_list': [],
                            # 'sort_col_list': ['cpf'],
                            'wt_col': None}
        print('amz_columns_dict---->', amz_columns_dict)
        return HttpResponse('product added successfully')
    return render(request, 'add_product.html')

from django.shortcuts import get_object_or_404
def update_view(request, id):
    context = {}
    obj = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponse('success')
    # context['form'] = form
    return render(request, 'update_ctegory.html', {'form':form})


def category_list(request):
    obj = Category.objects.all()
    return render(request, 'aboutus.html', {'data':obj})
