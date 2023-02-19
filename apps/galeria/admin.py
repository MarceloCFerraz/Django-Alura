from django.contrib import admin

from galeria.models import Photographies

# Register your models here.

class ListingPhotographies(admin.ModelAdmin):
    list_display = ("id", "title", "subtitle", "category", "published")
    list_editable = ("published", )
    list_per_page = 10
    list_filter = ("category", "user",)
    list_display_links = ("id", "title")

    search_fields = ("title", )


admin.site.register(Photographies, ListingPhotographies)



