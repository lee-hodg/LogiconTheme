from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _  # import as '_', used for trans

# These register setting to editable in the admin easily.
# http://mezzanine.jupo.org/docs/configuration.html#registering-settings

# Register our new settings, so we can change their vals in admin.
# this also makes them available in a view say as
# from mezzanine.conf import settings
# settings.SOCIAL_LINK_FACEBOOK.
# But if we want avail in template see further down.
register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label=_("Facebook link"),
    description=_("If present a Facebook icon linking here will be in the "
                  "header."),
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_FLICKR",
    label=_("Flickr link"),
    description=_("If present a Flickr icon linking here will be in the "
                  "header."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_GPLUS",
    label=_("Google plus link"),
    description=_("If present a Google-plus icon linking here will be in the "
                  "header"),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label=_("Twitter link"),
    description=_("If present a Twitter icon linking here will be in the "
                  "header."),
    editable=True,
    default="https://twitter.com/MEZZaTHEME",
)

register_setting(
    name="SOCIAL_LINK_DELICIOUS",
    label=_("Delicious link"),
    description=_("If present a delicious icon linking here will be in the "
                  "header"),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_TUMBLR",
    label=_("Tumblr link"),
    description=_("If present a tumblr icon linking here will be in the "
                  " header"),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_GPG_KEY",
    label=_("Public key for gpg"),
    description=_("Link to gpg public key on keyserver header."),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_UPWORK_PROFILE",
    label=_("Upwork profile"),
    description=_("Link to upwork profile in header"),
    editable=True,
    default="",
)

register_setting(
    name="SOCIAL_LINK_EMAIL",
    label=_("Email address"),
    description=_("Email address for contact"),
    editable=True,
    default="me@somewhere.com",
)

register_setting(
    name="GMAP_LOC",
    label=_("Google map location"),
    description=_("Centre address for google maps. "),
    editable=True,
    default="London, UK",
)

register_setting(
    name="GMAP_APIKEY",
    label=_("Google maps API key"),
    description=_("Google maps API Key"),
    editable=True,
    default=" ",
)

register_setting(
    name="GMAP_ZOOM",
    label=_("Google map zoom level"),
    description=_("Google maps zoom level"),
    editable=True,
    default="4",
)

register_setting(
    name="GMAP_DISABLE_UI",
    label=_("User control of map disabled"),
    description=_("Can user zoom, pan etc disabled?"),
    editable=True,
    default=False,
)

register_setting(
    name="GMAP_ICON_SIZE",
    label=_("Size of marker (px)"),
    description=_("The size of icon on the map in pixels"),
    editable=True,
    default=16
)

register_setting(
    name="PORTFOLIO_ITEMS_PER_PAGE",
    label=_("Portfolio items per page"),
    description=_("The number of portfolio items per page (restart after change)"),
    editable=True,
    default=6
)

# TEMPLATE_ACCESSIBLE_SETTINGS is one of the existing settings
# specifying all setting names available within templates, thus
# we want to append our new settings to it so we can use them in templates
register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,                           # Because we append these to
    default=("SOCIAL_LINK_FACEBOOK",       # existing templatate accessible settings.
             "SOCIAL_LINK_TWITTER",
             "SOCIAL_LINK_FLICKR",
             "SOCIAL_LINK_GPLUS",
             "SOCIAL_LINK_TUMBLR",
             "SOCIAL_LINK_DELICIOUS",
             "SOCIAL_LINK_UPWORK_PROFILE",
             "SOCIAL_LINK_GPG_KEY",
             "SOCIAL_LINK_EMAIL",
             "GMAP_LOC",
             "GMAP_ZOOM",
             "GMAP_APIKEY",
             "GMAP_DISABLE_UI",
             "GMAP_ICON_SIZE",
             "PORTFOLIO_ITEMS_PER_PAGE",
             ),
)
