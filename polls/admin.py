from django.contrib import admin

# Register your models here.
from .models import GeeksModel, Question, Choice

## optional for reordering
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

## optional split the form up into fieldsets
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]  
# admin.site.register(Question)

## you can do this but two models are connected with foreign keys it is not good
# admin.site.register(Choice)

## To properly show relation add this
# class ChoiceInline(admin.StackedInline):

## to reduce space you can use class ChoiceInline(admin.TabularInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
## By default, Django displays the str() of each object With list_display we can display individual fields
    # list_display = ('question_text', 'pub_date')

## you can also include methods in this
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(GeeksModel) 
