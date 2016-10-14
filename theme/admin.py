# Register your models here.
from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, IconBlurb, MapPlace


# TabularDynamicInlineAdmin for the Slide and IconBlurb
# NB the dynamic just gives some js to "add another" easily.
class IconBlurbInline(TabularDynamicInlineAdmin):
    model = IconBlurb


class MapPlaceInline(TabularDynamicInlineAdmin):
    model = MapPlace


# HomePage admin custom class.
class HomePageAdmin(PageAdmin):
    inlines = [IconBlurbInline, MapPlaceInline]

# register HomePage with its custom admin model
admin.site.register(HomePage, HomePageAdmin)

from .models import Portfolio, PortfolioItem, PortfolioItemImage, PortfolioItemCategory

# register Portfolio with default PageAdmin
admin.site.register(Portfolio, PageAdmin)


class PortfolioItemImageInline(TabularDynamicInlineAdmin):
    model = PortfolioItemImage


class PortfolioItemAdmin(PageAdmin):
    inlines = (PortfolioItemImageInline,)

admin.site.register(PortfolioItem, PortfolioItemAdmin)
admin.site.register(PortfolioItemCategory)
