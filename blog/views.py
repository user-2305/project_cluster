from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView #старый проект
from .models import Post, Edu, Agr, Empl
from .forms import RegionFilterForm, EmploymentFilterForm, АgricultureFilterForm

# Create your views here.
class BlogDetailView(DetailView): #старый проект
    model = Post
    template = 'post_detail.html'

class Bloglist(ListView): #старый проект
    model = Post
    template_name = 'home.html'

class About(TemplateView): #старый проект
    template_name = 'about.html'

'''
def edu_list(request):
    edus = Edu.objects.all()
    return render(request, 'edu_list.html', {'edus': edus})
'''

def edu_list(request):
    form = RegionFilterForm(request.GET)
    if form.is_valid():
        region = form.cleaned_data['region']
        district = form.cleaned_data['district']
        indicator = form.cleaned_data['indicator']
        amount = form.cleaned_data['amount']
        year = form.cleaned_data['year']
        edus = Edu.objects.all()
        if region:
            edus = edus.filter(region__icontains=region)
        if district:
            edus = edus.filter(district__icontains=district)
        if indicator:
            edus = edus.filter(indicator__icontains=indicator)
        if amount:
            edus = edus.filter(amount=amount)
        if year:
            edus = edus.filter(year=year)
    else:
        edus = Edu.objects.all()
    return render(request, 'edu_list.html', {'edus': edus, 'form': form})

def agr_list(request):
    form = АgricultureFilterForm(request.GET)
    if form.is_valid():
        region = form.cleaned_data.get('region')
        district = form.cleaned_data.get('district')
        indicator = form.cleaned_data.get('indicator')
        year = form.cleaned_data.get('year')
        min_percentage = form.cleaned_data.get('min_percentage')
        max_percentage = form.cleaned_data.get('max_percentage')
        agrs = Agr.objects.all()
        if region:
            agrs = agrs.filter(region__icontains=region)
        if district:
            agrs = agrs.filter(district__icontains=district)
        if indicator:
            agrs = agrs.filter(indicator__icontains=indicator)
        if year:
            agrs = agrs.filter(year=year)
        if min_percentage:
            agrs = agrs.filter(percentage__gte=min_percentage)
        if max_percentage:
            agrs = agrs.filter(percentage__lte=max_percentage)
    else:
        agrs = Agr.objects.all()

    return render(request, 'agr_list.html', {'form': form, 'agrs': agrs})

def empl_list(request):
    form = EmploymentFilterForm(request.GET)
    if form.is_valid():
        region = form.cleaned_data.get('region')
        district = form.cleaned_data.get('district')
        indicator = form.cleaned_data.get('indicator')
        year = form.cleaned_data.get('year')
        min_percentage = form.cleaned_data.get('min_percentage')
        max_percentage = form.cleaned_data.get('max_percentage')

        employments = Empl.objects.all()
        if region:
            employments = employments.filter(region__icontains=region)
        if district:
            employments = employments.filter(district__icontains=district)
        if indicator:
            employments = employments.filter(indicator__icontains=indicator)
        if year:
            employments = employments.filter(year=year)
        if min_percentage:
            employments = employments.filter(percentage__gte=min_percentage)
        if max_percentage:
            employments = employments.filter(percentage__lte=max_percentage)
    else:
        employments = Empl.objects.all()

    return render(request, 'empl_list.html', {'form': form, 'employments': employments})