from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _  #import as '_', used for trans

#These register setting to editable in the admin easily.
# http://mezzanine.jupo.org/docs/configuration.html#registering-settings

#Register our new settings, so we can change their vals in admin.
#this also makes them available in a view say as
#from mezzanine.conf import settings
#settings.SOCIAL_LINK_FACEBOOK.
#But if we want avail in template see further down.
register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the "
                  "header."),
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="GMAP_LOC",
    label=_("Google map location"),
    description=_("Address for google maps. "),
    editable=True,
    default="Manchester, England",
)

#TEMPLATE_ACCESSIBLE_SETTINGS is one of the existing settings
#specifying all setting names available within templates, thus
#we want to append our new settings to it so we can use them in templates
register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,                           #Because we append these to
    default=("SOCIAL_LINK_FACEBOOK",       #existing templatate accessible settings.
             "GMAP_LOC",
             ),
)
