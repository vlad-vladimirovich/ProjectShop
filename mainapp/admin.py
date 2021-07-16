from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *


class SofaAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sofa'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TableAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='table'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Table, TableAdmin)
admin.site.register(Sofa, SofaAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(CartProduct)
admin.site.register(Order)