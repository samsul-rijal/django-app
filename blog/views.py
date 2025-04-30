# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserForm
from .models import User, Task
# from .form import TaskForm

def dashboard(request):
    total_users = User.objects.count()
    return render(request, 'dashboard.html', {'total_users': total_users})

def user_list(request):
    users = User.objects.all()
    # users = User.objects.raw('delete * FROM users')
    # "select * from users"
    return render(request, 'user_list.html', {'users': users})


# def user_create(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'User berhasil ditambahkan!')
#             return redirect('users')
#     else:
#         form = UserForm()
#     return render(request, 'user_form.html', {'form': form})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            kategori = form.cleaned_data.get('kategori')
            material = form.cleaned_data.get('material')
            lokasi = form.cleaned_data.get('lokasi')

            # Ambil potongan kode
            kategori_code = kategori[:3].lower()  # 'geo' from "geoteknik"
            material_code = material[:2].lower()  # 'cl' from "clay"
            lokasi_code = lokasi[:3].lower()     # 'kal' from "kalimantan"

            base_code = f"{kategori_code}-{material_code}-{lokasi_code}"

            # Cari user terakhir dengan flag yang sama
            last_user = User.objects.filter(flag__startswith=base_code).order_by('-flag').first()

            if last_user:
                last_number = int(last_user.flag.split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1

            user.flag = f"{base_code}-{new_number:03d}"
            user.save()

            messages.success(request, 'User berhasil ditambahkan!')
            return redirect('users')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})


# def add_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Task berhasil ditambahkan!')
#             return redirect('task_list') 
#     else:
#         # form = TaskForm()
#         users = User.objects.all()
    
#     return render(request, 'add_task.html', {'users': users})

def add_task(request):
    users = User.objects.all() 
    if request.method == 'POST':
        nama_task = request.POST.get('nama_task')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        user_id = request.POST.get('user_id')

        # Validasi dan simpan task baru
        # user = User.objects.get(id=user_id)
        print(user_id)
        task = Task(nama_task=nama_task, start_date=start_date, end_date=end_date, user_id=user_id)
        task.save()

        return redirect('task_list')
    
    else:
        # form = TaskForm()
        users = User.objects.all()
        return render(request, 'add_task.html', {'users': users})

def task_list(request):
    users_with_tasks = User.objects.filter(task__isnull=False).distinct()

    print(users_with_tasks)  

    tasks = Task.objects.all()  # Mengambil semua task

    # Menampilkan ke template
    return render(request, 'task_list.html', {'users': users_with_tasks, 'tasks': tasks})