from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from wagtail.core.models import Page

from home import models as home_models


class AllBlogsPage(Page):
    max_count = 1
    parent_page_type = ['HomePage']
    subpage_types = ['BlogPage']

    def get_context(self, request, *args, **kwargs):
        context = super(AllBlogsPage, self).get_context(request)
        all_resources = home_models.BlogPage.objects.live().public()
        paginator = Paginator(all_resources, 6)
        page = request.GET.get('page')
        try:
            resources = paginator.page(page)
        except PageNotAnInteger:
            resources = paginator.page(1)
        except EmptyPage:
            resources = paginator.page(paginator.num_pages)
        context['resources'] = resources
        return context
