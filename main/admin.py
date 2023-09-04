from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Employees
from .models import Participants



admin.site.site_title = 'Админ-панель сайта Олимпиады'
admin.site.site_header = 'Админ-панель сайта Олимпиады'


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ("name", "about", "emp_img")



class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ("name", "title_univer", "phone","email")
    search_fields = ("name", "title_univer","phone", "email")
    readonly_fields = ("title_univer","email")


admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Participants, ParticipantsAdmin)