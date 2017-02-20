# from django.utils.translation import ugettext_lazy as _
# from cms.toolbar_pool import toolbar_pool
# from cms.toolbar_base import CMSToolbar
# from cms.utils.urlutils import admin_reverse
# from theblog.models import Post


# class TheBlogToolbar(CMSToolbar):
#     watch_models = [Post]

#     def populate(self):
#         if not self.is_current_app:
#             return

#         menu = self.toolbar.get_or_create_menu('theblog', _('Post'))
        
#         menu.add_modal_item(
#             name=_('Add new Post'),
#             url=admin_reverse('polls_poll_add'),
#         )


# toolbar_pool.register(TheBlogToolbar)  # register the toolbar
