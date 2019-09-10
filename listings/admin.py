from django.contrib import admin
from listings.models import listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_published','list_date','realtor']
    list_diplay_links = ['id','title']
    list_filter = ['realtor']
    list_editable = ['is_published']
    search_fields = ['title','price','description','city','state','zipcode']
    list_per_page = 25
admin.site.register(listing, ListingAdmin)