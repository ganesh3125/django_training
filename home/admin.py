from django.contrib import admin
from home.models import student,library,book,teacher,section
# Register your models here.
#admin.site.register(student)
#admin.site.register(library)
#admin.site.register(section)
#admin.site.register(teacher)
#admin.site.register(book)

@admin.register(book)
class bookadmin(admin.ModelAdmin):
    pass

@admin.register(student)
class studentadmin(admin.ModelAdmin):
    search_fields=('student_name','department')
    list_filter=('student_name','department')
    fields=('student_name','department')

@admin.register(teacher)
class teacheradmin(admin.ModelAdmin):
    pass

@admin.register(library)
class libraryadmin(admin.ModelAdmin):
    pass

@admin.register(section)
class sectionadmin(admin.ModelAdmin):
    pass