from django.shortcuts import render
from .forms import ProductForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'product_creation_success.html')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})