from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               
            {'fields': ['question_text']}),
        ('Date information', 
            {'fields': ['pub_date'], 
            'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]    # the Choice objects are edited on the question page.
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # columns for the Quesetion admin page
    list_filter = ['pub_date']  # adds a filter sidebar to filter the change list.
    search_fields = ['question_text']   # admin can search through question texts

admin.site.register(Question, QuestionAdmin)