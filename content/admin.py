from django.contrib import admin
from content.models import AboutUs

# Register your models here.
class AboutUsAdmin(admin.ModelAdmin):
    list_display =('id','heading1','description1','heading2','description2','li_item_heading1','li_item_description1','li_item_heading1','li_item_description1','description','image_url')


admin.site.register(AboutUs,AboutUsAdmin)
