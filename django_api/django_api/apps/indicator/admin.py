from django.contrib import admin

from .models import (
    IndicatorBlueprint,
    Reportable,
    IndicatorReport,
)

admin.site.register(IndicatorBlueprint)
admin.site.register(Reportable)
admin.site.register(IndicatorReport)
