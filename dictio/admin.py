from django.contrib import admin
from django import forms
from .models import EnglishToDarija, Example
from .forms import ExampleForm


class ExampleInline(admin.TabularInline):
    model = Example
    form = ExampleForm
    extra = 1



class EnglishToDarijaForm(forms.ModelForm):
    class Meta:
        model = EnglishToDarija
        fields = '__all__'


@admin.register(EnglishToDarija)
class EnglishToDarijaAdmin(admin.ModelAdmin):
    list_display = ('english_word', 'darija_translation')
    search_fields = ('english_word__icontains', 'darija_translation__icontains', 'example__example_text__icontains')
    inlines = [ExampleInline]
    form = EnglishToDarijaForm

    def get_examples(self, obj):
        examples = obj.example_set.all().values_list('example_text', flat=True)
        return examples

    get_examples.short_description = 'Examples'
    get_examples.admin_order_field = 'example__example_text'


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    form = ExampleForm
    list_display = ('english_to_darija', 'example_text')
    search_fields = ('english_to_darija__english_word__icontains', 'example_text__icontains')


admin.site.site_header = 'My Dictionary Administration'
