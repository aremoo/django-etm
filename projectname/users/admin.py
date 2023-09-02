from django.contrib import admin

# Register your models here.
from .models import ETMInfo
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'employee_id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('employee_id', 'phone_number', 'pay', 'vacation_balance', 'job_title', 'third_party_username', 'third_party_password', 'agreement_accepted')}),
    )
    def get_readonly_fields(self, request, obj=None):
            if obj:  # This means the object is already created i.e. it's an edit
                return self.readonly_fields
            return self.readonly_fields + ('employee_id',)



class ETMInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'employee_id_display', 'etm_username']

    def employee_id_display(self, obj):
        return obj.user.employee_id
    employee_id_display.short_description = "Employee ID"


admin.site.register(ETMInfo, ETMInfoAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
