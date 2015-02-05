from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import lazy

try:
    from django.conf.urls import patterns, url
except:
    from django.conf.urls.defaults import patterns, url

from ella.core.custom_urls import resolver

from ella_galleries.views import gallery_item_detail
from ella_galleries.models import Gallery

lazy_slugify = lazy(slugify, str)
lazy_regex = lazy(lambda regex, res_dict: regex % res_dict, str)

res = {
    'item_slug': r'(?P<item_slug>[\w-]+)',
    'url_remainder': r'(?P<url_remainder>.+/)',
    'item_prefix': lazy_slugify(_('Item')),
}


urlpatterns = patterns(
    '',
    url(lazy_regex(r'^%(item_prefix)s/%(item_slug)s/%(url_remainder)s$', res), gallery_item_detail, name='gallery-item-detail-custom'),
    url(lazy_regex(r'^%(item_prefix)s/%(item_slug)s/$', res), gallery_item_detail, name='gallery-item-detail'),
)

resolver.register(urlpatterns, model=Gallery)
resolver.register_custom_detail(Gallery, gallery_item_detail)
