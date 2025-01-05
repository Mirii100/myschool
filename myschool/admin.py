from django.contrib import admin
from .models import Signup,Testimonial,courses,Instructor,Specialization,Book,Project,CoursesCategory,MyUser
# Register your models here.
admin.site.register(Signup)
admin.site.register(Testimonial)
admin.site.register(courses)
admin.site.register(Specialization)
admin.site.register(CoursesCategory)
admin.site.register(MyUser)
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('specialization',)  # For Many-to-Many fields



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date', 'available_copies')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('genre', 'language', 'publication_date')





@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_name', 'start_date', 'end_date', 'status', 'progress_percentage')
    search_fields = ('name', 'client_name', 'description')
    list_filter = ('status', 'start_date', 'end_date')
