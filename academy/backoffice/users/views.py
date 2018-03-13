from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from academy.apps.accounts.models import User
from academy.apps.students.models import Student
from .forms import BaseFilterForm


@staff_member_required
def index(request):
    user_ids = Student.objects.distinct('user_id').values_list('user_id', flat=True)
    users = User.objects.exclude(is_superuser=True).exclude(is_staff=True) \
        .exclude(is_superuser=True).filter(id__in=user_ids)
    user_count = users.count()

    download = request.GET.get('download', '')
    form = BaseFilterForm(request.GET or None)
    if form.is_valid():
        users = form.get_data()
        if download:
            csv_buffer = form.generate_to_csv()
            response = HttpResponse(csv_buffer.getvalue(), content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename=daftar-pengguna.csv'
            return response

    context = {
        'title': 'User',
        'page_active': 'user',
        'users': users,
        'form': form,
        'user_count': user_count,
        'filter_count': users.count()
    }
    return render(request, 'backoffice/users/index.html', context)


@staff_member_required
def details(request, id):
    user = get_object_or_404(User, id=id)

    context = {
        'user': user,
        'page_active': 'user',
        'title': 'User Detail',
        'student': user.get_student()
    }
    return render(request, 'backoffice/users/details.html', context)
