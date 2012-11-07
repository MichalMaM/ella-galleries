from django.contrib import admin
from django.utils.translation import ugettext_lazy as _, ugettext
from django.forms.models import BaseInlineFormSet
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.helpers import InlineAdminForm

from ella.core.admin import ListingInlineAdmin
from ella.core.cache import get_cached_object

from ella_galleries.models import Gallery, GalleryItem

class GalleryItemFormset(BaseInlineFormSet):
    " Override default FormSet to allow for custom validation."

    def __iter__(self):
        for form, original in zip(self.formset.initial_forms, self.formset.get_queryset()):
            yield InlineAdminForm(self.formset, form, self.fieldsets,
                self.opts.prepopulated_fields, original, self.readonly_fields,
                model_admin=self.opts)
        for form in self.formset.extra_forms:
            yield InlineAdminForm(self.formset, form, self.fieldsets,
                self.opts.prepopulated_fields, None, self.readonly_fields,
                model_admin=self.opts)

    def clean(self):
        """Checks if all objects exist and searches for duplicate references to the same object in one gallery."""
        if not self.is_valid():
            return

        obj = self.instance
        items = set([])

        for i in self.cleaned_data:
            if 'photo' in i:
                # TODO: why cleaned data does not have target_ct_id prop?
                # check for duplicities
                if i['photo'] in items:
                    raise forms.ValidationError, ugettext('There are two references to %s in this gallery') % obj
                items.add(i['photo'])

        return self.cleaned_data


class GalleryItemTabularOptions(admin.TabularInline):
    model = GalleryItem
    extra = 10
    formset = GalleryItemFormset


class GalleryOptions(admin.ModelAdmin):
    list_display = ('title', 'created', 'category',)
    ordering = ('-created',)
    fieldsets = (
        (_("Gallery heading"), {'fields': ('title', 'slug',)}),
        (_("Gallery metadata"), {'fields': ('description', 'content', 'authors', 'category')}),
    )
    list_filter = ('created', 'category',)
    search_fields = ('title', 'description', 'slug',) # FIXME: 'tags__tag__name',)
    inlines = [ GalleryItemTabularOptions, ListingInlineAdmin ]
    prepopulated_fields = {'slug': ('title',)}
    rich_text_fields = {None: ('description', 'content',)}
    suggest_fields = {'owner': ('name', 'slug',), }

admin.site.register(Gallery, GalleryOptions)

