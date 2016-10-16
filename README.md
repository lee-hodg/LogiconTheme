## Getting started

### HomePage

The first thing to do is add a HomePage in the admin, and in the meta data set the URL to '/'

Next, add links #services, #contact, #portfolio to enable links to the various sections of the one-page theme. The link hash
must be unchanged, but you can set the title to whatever you like. Deselect the (dummy) "Footer menu" and select the "Top navigation bar" menu.

Now, configure your home page, for example by changing the site logo, the background image of each section, the headings and sub-headings of each section.
You can use font-awesome classes or images for the icons in the "services" section, and update the title and text of each according to your needs. N.B.
If you decide to use an image, set the font-awesome class field to 'none'.

While you're here, you may also want to add some "Map places", which are markers to be shown on the google map, if you are using it, along with
the icon for the marker itself. Each Map place allows a custom message to be displayed on-click, and you can use the placeholder `%LOC_PLACEHOLDER%' to
have the Map place title substituted in your text, which is useful if you want the same message for each marker only with location changed accordingly.

### Settings and map

The map is highly customizable. Just add you google API key in the `GMAP_APIKEY` setting, and you can configure the centering of the map, the zoom level, and if the user can control it. You can add markers to the map under the "Map places" section of HomePage, and set the icon to be used for the marker and its size. You can even set a msg for each marker such that when the user clicks this message is displayed. 

Other settings you may wish to configure are your social links (these appear in the top-right of the page), the site name, and the number
of portfolio-items per page.

You can also add your google analytics ID 


### Portfolio

Portfolio items, consist of the featured image (the one that displays on the homepage portfolio section), along with other images for the image slider
in the modal popup for the portfolio item detail. They of course also have a title, description and category tags. If you want a portfolio item to show
on the homepage then 'Featured' should be checked, and if you want the item to be highlighted with a big image then check 'Highlighted' too.

### settings.py 

Set your Django `SECRET_KEY` and `NEVERCACHE_KEY` (consider setting them in `local_settings.py` file or from the environment).  Add your site's domain to `ALLOWED_HOSTS`, and also remember to set `DEBUG=False` when you make the site live. You will also need to ensure that `STATIC_ROOT` and `MEDIA_ROOT` point to the correct location on your server, and finally make sure the database is setup correctly for your server.


