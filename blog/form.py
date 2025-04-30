from django import forms
from .models import User
from .models import Task
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'kategori', 'material', 'lokasi']  # Tambahkan kategori, material, lokasi

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise ValidationError('Nama minimal 3 karakter.')
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        # Cek apakah email sudah dipakai user lain (kecuali saat edit dirinya sendiri)
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Email sudah digunakan.')
        return email
    

# class TaskForm(forms.ModelForm):
#     user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Pilih User", widget=forms.Select(attrs={'class': 'form-control'}))

#     class Meta:
#         model = Task
#         fields = ['nama_task', 'start_date', 'end_date', 'user']  # Menambahkan field 'user'
#         widgets = {
#             'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#         }