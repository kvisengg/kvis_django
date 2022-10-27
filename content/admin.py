from django.contrib import admin
from content.models import AboutUs, Product, ProjectComplete, Reviews

# Register your models here.


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading1', 'description1', 'heading2', 'description2', 'li_item_heading1',
                    'li_item_description1', 'li_item_heading1', 'li_item_description1', 'description', 'image_url')


class ProjectCompleteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'happy_clients', 'projects', 'total_hours', 'total_workers'
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_description')


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'user_position', 'description', 'image')


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ProjectComplete, ProjectCompleteAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Reviews, ReviewsAdmin)
