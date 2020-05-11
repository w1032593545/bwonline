import xadmin

from django.urls import path, include, re_path

from django.views.generic.base import TemplateView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView

from organization.views import OrgView
from bwOnline.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    path('captcha/', include('captcha.urls')),
    path('xadmin/', xadmin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('org/', include('organization.urls', namespace='org')),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]
