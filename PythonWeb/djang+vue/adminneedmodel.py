from import_export import resources
from infer.models import UserProfile, SubmitDraft


class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile


class SubmitDraftResource(resources.ModelResource):
    class Meta:
        model = SubmitDraft

# from infer.usemethod.adminneedmodel import UserProfileResource, SubmitDraftResource


# class UserProfileAdmin(ImportExportModelAdmin):
#     resource_class = UserProfileResource
#     list_display = ('__str__', 'logstatus', 'userrole')
#     search_fields = ('logstatus', 'userrole')
#     list_per_page = 10
#     admin.AdminSite.site_header = '用户管理'


# class SubmitDraAdmin(ImportExportModelAdmin):
#     resource_class = SubmitDraftResource
#     list_display = ('__str__', 'submitter', 'publicdate', 'checkstatus')
#     search_fields = ('publicdate', 'checkstatus')
#     list_per_page = 10
#     admin.AdminSite.site_header = '上传管理'
