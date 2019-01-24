from django.contrib import admin
from .models import Question, Danfe, DanfeItem, SimCard, Team, Carrier, AccessoryType, Accessory, Build, SkuType, HardwareType, DeviceStatus, Device, AndroidVersion


class DanfeItemInline(admin.TabularInline):
    model = DanfeItem
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_test', 'pub_date')
    list_filter = ['question_test']
    search_fields = ['question_test']


@admin.register(Danfe)
class DanfeAdmin(admin.ModelAdmin):
    list_display = ('numero_nota_fiscal', 'data_emissao', 'data_entrada', 'user')
    fieldsets = [
        ('Dados da Nota Fiscal', {'fields': ['numero_nota_fiscal', 'data_emissao', 'user']}),
    ]
    inlines = [DanfeItemInline]


@admin.register(DanfeItem)
class DanfeItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'ncm', 'cst', 'cfop', 'qty')


@admin.register(SimCard)
class SimCardAdmin(admin.ModelAdmin):
    list_display = ('carrier', 'zone', 'phone_number', 'pin1', 'pin2', 'puk1', 'puk2')
    fieldsets = [
        (None, {'fields': ['carrier', 'zone', 'phone_number', 'iccid', 'serial_number', 'comments']}),
        ('Team and Responsible', {'fields': ['team', 'responsible'], 'classes': ['collapse']}),
        ('PIN and PUK', {'fields': ['pin1', 'pin2', 'puk1', 'puk2'], 'classes': ['collapse']}),
        ('Login and Password', {'fields': ['login', 'cloud_password', 'vvm_password'], 'classes': ['collapse']}),
        ('Others', {'fields': ['is_account', 'is_caller_name_id', 'is_vvm', 'is_volte', 'is_vowifi', 'is_hotspot'], 'classes': ['collapse']}),
    ]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(AccessoryType)
class AccessoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'serial_number', 'team', 'responsible', 'part_number')


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(SkuType)
class SkuTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(HardwareType)
class HardwareTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(DeviceStatus)
class DeviceStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'serial_number', 'public_name', 'internal_name', 'team', 'user_responsible', 'build', 'carrier', 'sku_type')


@admin.register(AndroidVersion)
class AndroidVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

