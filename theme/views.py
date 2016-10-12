from django.views.generic import ListView, DetailView
from django.conf import settings
from django.http import HttpResponseBadRequest
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse
from .models import PortfolioItem
import json


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        # Convert the context dictionary into a JSON object
        # json.dumps is fine for our purpose.
        return json.dumps(context)


class AJAXPortfolioPageView(JSONResponseMixin, ListView):
    model = PortfolioItem
    paginate_by = 6
    context_object_name = "items"

    def render_to_response(self, context):
        if self.request.is_ajax():
            # AJAX req.
            context.update({'MEDIA_URL': settings.MEDIA_URL})
            section_html = render_to_string('pages/_portfolioitems_snippet.html',
                                            RequestContext(self.request, context)
                                            )
            return self.render_to_json_response({'section_html': section_html})
        else:
            return HttpResponseBadRequest('AJAX only')

# class AJAXPortfolioDetailView(JSONResponseMixin, DetailView):
#     model = PortfolioItem
#
#     def render_to_response(self, context):
#         if self.request.is_ajax():
#             # AJAX req.
#             context.update({'MEDIA_URL': settings.MEDIA_URL})
#             modal_html = render_to_string('pages/_portfolio_modal_snippet.html',
#                                           RequestContext(self.request, context)
#                                           )
#             return self.render_to_json_response({'section_html': section_html})
#         else:
#             return HttpResponseBadRequest('AJAX only')


class AJAXPortfolioDetailView(DetailView):
    model = PortfolioItem
    template_name = 'pages/_portfolio_modal_snippet.html'
