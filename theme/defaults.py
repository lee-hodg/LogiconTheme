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
    name="GPG_KEY",
    label=_("Public key for gpg"),
    description=_("Link to gpg public key on keyserver "
        "header."),
    editable=True,
    default="",
)


register_setting(
    name="UPWORK_PROFILE",
    label=_("Upwork profile"),
    description=_("Link to upwork profile"),
    editable=True,
    default="http://www.upwork.com/o/profiles/users/_~01dcfbf8526ffd5b29/",
)

register_setting(
    name="EMAIL",
    label=_("Email address"),
    description=_("Email address for contact"),
    editable=True,
    default="lee@logicon.io",
)

#TEMPLATE_ACCESSIBLE_SETTINGS is one of the existing settings
#specifying all setting names available within templates, thus
#we want to append our new settings to it so we can use them in templates
register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,                           #Because we append these to
    default=("SOCIAL_LINK_FACEBOOK",       #existing templatate accessible settings.
             "EMAIL",
			 "UPWORK_PROFILE",
			 "GPG_KEY",
             ),
)
