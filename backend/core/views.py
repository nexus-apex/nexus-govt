import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import GovService, GovApplication, Citizen


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['govservice_count'] = GovService.objects.count()
    ctx['govservice_license'] = GovService.objects.filter(category='license').count()
    ctx['govservice_permit'] = GovService.objects.filter(category='permit').count()
    ctx['govservice_certificate'] = GovService.objects.filter(category='certificate').count()
    ctx['govservice_total_fee'] = GovService.objects.aggregate(t=Sum('fee'))['t'] or 0
    ctx['govapplication_count'] = GovApplication.objects.count()
    ctx['govapplication_submitted'] = GovApplication.objects.filter(status='submitted').count()
    ctx['govapplication_under_review'] = GovApplication.objects.filter(status='under_review').count()
    ctx['govapplication_approved'] = GovApplication.objects.filter(status='approved').count()
    ctx['citizen_count'] = Citizen.objects.count()
    ctx['citizen_verified'] = Citizen.objects.filter(status='verified').count()
    ctx['citizen_unverified'] = Citizen.objects.filter(status='unverified').count()
    ctx['recent'] = GovService.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def govservice_list(request):
    qs = GovService.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(category=status_filter)
    return render(request, 'govservice_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def govservice_create(request):
    if request.method == 'POST':
        obj = GovService()
        obj.name = request.POST.get('name', '')
        obj.department = request.POST.get('department', '')
        obj.category = request.POST.get('category', '')
        obj.fee = request.POST.get('fee') or 0
        obj.processing_days = request.POST.get('processing_days') or 0
        obj.status = request.POST.get('status', '')
        obj.documents_required = request.POST.get('documents_required', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/govservices/')
    return render(request, 'govservice_form.html', {'editing': False})


@login_required
def govservice_edit(request, pk):
    obj = get_object_or_404(GovService, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.department = request.POST.get('department', '')
        obj.category = request.POST.get('category', '')
        obj.fee = request.POST.get('fee') or 0
        obj.processing_days = request.POST.get('processing_days') or 0
        obj.status = request.POST.get('status', '')
        obj.documents_required = request.POST.get('documents_required', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/govservices/')
    return render(request, 'govservice_form.html', {'record': obj, 'editing': True})


@login_required
def govservice_delete(request, pk):
    obj = get_object_or_404(GovService, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/govservices/')


@login_required
def govapplication_list(request):
    qs = GovApplication.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(application_id__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'govapplication_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def govapplication_create(request):
    if request.method == 'POST':
        obj = GovApplication()
        obj.application_id = request.POST.get('application_id', '')
        obj.citizen_name = request.POST.get('citizen_name', '')
        obj.service_name = request.POST.get('service_name', '')
        obj.status = request.POST.get('status', '')
        obj.submitted_date = request.POST.get('submitted_date') or None
        obj.processed_date = request.POST.get('processed_date') or None
        obj.remarks = request.POST.get('remarks', '')
        obj.save()
        return redirect('/govapplications/')
    return render(request, 'govapplication_form.html', {'editing': False})


@login_required
def govapplication_edit(request, pk):
    obj = get_object_or_404(GovApplication, pk=pk)
    if request.method == 'POST':
        obj.application_id = request.POST.get('application_id', '')
        obj.citizen_name = request.POST.get('citizen_name', '')
        obj.service_name = request.POST.get('service_name', '')
        obj.status = request.POST.get('status', '')
        obj.submitted_date = request.POST.get('submitted_date') or None
        obj.processed_date = request.POST.get('processed_date') or None
        obj.remarks = request.POST.get('remarks', '')
        obj.save()
        return redirect('/govapplications/')
    return render(request, 'govapplication_form.html', {'record': obj, 'editing': True})


@login_required
def govapplication_delete(request, pk):
    obj = get_object_or_404(GovApplication, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/govapplications/')


@login_required
def citizen_list(request):
    qs = Citizen.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'citizen_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def citizen_create(request):
    if request.method == 'POST':
        obj = Citizen()
        obj.name = request.POST.get('name', '')
        obj.citizen_id = request.POST.get('citizen_id', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.address = request.POST.get('address', '')
        obj.applications_count = request.POST.get('applications_count') or 0
        obj.status = request.POST.get('status', '')
        obj.registered_date = request.POST.get('registered_date') or None
        obj.save()
        return redirect('/citizens/')
    return render(request, 'citizen_form.html', {'editing': False})


@login_required
def citizen_edit(request, pk):
    obj = get_object_or_404(Citizen, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.citizen_id = request.POST.get('citizen_id', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.address = request.POST.get('address', '')
        obj.applications_count = request.POST.get('applications_count') or 0
        obj.status = request.POST.get('status', '')
        obj.registered_date = request.POST.get('registered_date') or None
        obj.save()
        return redirect('/citizens/')
    return render(request, 'citizen_form.html', {'record': obj, 'editing': True})


@login_required
def citizen_delete(request, pk):
    obj = get_object_or_404(Citizen, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/citizens/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['govservice_count'] = GovService.objects.count()
    data['govapplication_count'] = GovApplication.objects.count()
    data['citizen_count'] = Citizen.objects.count()
    return JsonResponse(data)
