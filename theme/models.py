# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=500,
                               default=("WELCOME TO LOGICON HEADQUARTERS."
                                        " OUR TEAM COMBINES STRONG TECHNICAL KNOW HOW"
                                        " WITH THE ABILITY TO DELIVER HIGHLY POLISHED SOLUTIONS."),
                               help_text='Heading under the logo')
    logo_icon = FileField(verbose_name=_('Logo Image'),
                          upload_to=upload_to('theme.HomePage.logo_icon', 'icons'),
                          format='Image', max_length=255, blank=True, null=True)
    services_heading = models.CharField(max_length=200,
                                        default='Services',
                                        help_text='The services heading')
    services_subheading = models.CharField(max_length=200,
                                           default=('We offer a full-stack of services incuding'
                                                    ' devops, backend and frontend'),
                                           help_text='The services subheading')
    portfolio_heading = models.CharField(max_length=200,
                                         default='Portfolio',
                                         help_text='The portfolio heading')
    portfolio_subheading = models.CharField(max_length=200,
                                            default=('Browse through our portfolio to see what'
                                                     ' we have to offer.'),
                                            help_text='The portfolio subheading')
    featured_portfolio = models.ForeignKey('Portfolio', blank=True, null=True,
                                           help_text='If selected items from this portfolio will be featured '
                                                     'on the home page.')

    contact_text = RichTextField(max_length=1000,
                                    default=('One of our team would be happy to discuss'
                                             ' in detail our skillset and experience'
                                             ' and how we fit in with your project.'
                                             ' Send us an email using the link below.'),
                                    help_text='Text for contact section')

    class Meta:
        verbose_name = _('Home page')
        verbose_name_plural = _('Home pages')


class IconBlurb(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name='blurbs')
    icon = FileField(verbose_name=_('Image'),
                     upload_to=upload_to('theme.IconBlurb.icon', 'icons'),
                     format='Image', max_length=255, blank=True, null=True)
    fa_icon = models.CharField(max_length=50)  # font-awesome classes
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=2000, blank=True,
                            help_text='Optional, if provided clicking the blurb will go here.')


COLUMNS_CHOICES = (
    ('6', 'Two columns'),  # two columns use span6
    ('4', 'Three columns'),  # three columns use span4
    ('3', 'Four Columns'),  # four columns use span3
)


class Portfolio(Page):
    '''
    A collection of individual portfolio items
    We nest the PortfolioItems under this page (i.e. in the admin
    add a portfolio page, then 'under it' add portfolio item pages)
    '''
    content = RichTextField(blank=True)
    columns = models.CharField(max_length=1, choices=COLUMNS_CHOICES,
                               default='3')

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolios')


class PortfolioItem(Page, RichText):
    '''
    An individual portfolio item, should be nested under a Portfolio
    '''
    # This is the featured image, but also we use PortfolioItemImage
    # to add more images that can be scrolled through (c.f. choices
    # associated with a Poll obj in django tut via Foreign key)

    # NB the related names are what you will need when grabbing these
    # objects in either view or template after dotting.
    featured = models.BooleanField()  # to be featured on homepage or not.
    highlighted = models.BooleanField()  # Is it big or small on homepage
    featured_image = FileField(verbose_name=_('Featured Image'),
                               upload_to=upload_to('theme.PortfolioItem.featured_image', 'portfolio'),
                               format='Image', max_length=255, null=True, blank=True)
    short_description = RichTextField(blank=True)
    categories = models.ManyToManyField('PortfolioItemCategory',
                                        verbose_name=_('Categories'),
                                        blank=True,
                                        related_name='portfolioitems')
    href = models.CharField(max_length=2000, blank=True,
                            help_text='A link to the finished project (optional)')

    class Meta:
        verbose_name = _('Portfolio item')
        verbose_name_plural = _('Portfolio items')


class PortfolioItemImage(Orderable):
    '''
    An image for a PortfolioItem
    '''
    portfolioitem = models.ForeignKey(PortfolioItem, related_name='images')
    file = FileField(_('File'), max_length=200, format='Image',
                     upload_to=upload_to('theme.PortfolioItemImage.file', 'portfolio items'))

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


class PortfolioItemCategory(Slugged):
    '''
    A category for grouping portfolio items into a series.
    '''

    class Meta:
        verbose_name = _('Portfolio Item Category')
        verbose_name_plural = _('Portfolio Item Categories')
        ordering = ('title',)
