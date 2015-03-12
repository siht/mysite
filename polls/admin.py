from django.contrib import admin
from polls.models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class QuestionAdmin1(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class QuestionAdmin2(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class ChoiceInline1(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin3(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline1]

class QuestionAdmin4(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline1]
    list_display = ('question_text', 'pub_date')

class QuestionAdmin4(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline1]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin4)
admin.site.register(Choice)
