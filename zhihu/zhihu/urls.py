"""zhihu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from zhihu.settings import MEDIA_ROOT

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from Account.views import UserProfileViewSet, UserRegisterViewset, SmsCodeViewSet
from Question.views import AnswerViewset, TopicViewset, QuestionViewset
from AccountOperation.views import UserVoteViewSet, UserFlowQuestionViewSet, UserFavViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, base_name='user')

router.register(r'codes', SmsCodeViewSet, base_name='code')

router.register(r'register', UserRegisterViewset, base_name='register')

router.register(r'answers', AnswerViewset, base_name='answer')
router.register(r'topics', TopicViewset, base_name='topic')
router.register(r'questions', QuestionViewset, base_name='question')

router.register(r'votes', UserVoteViewSet, base_name='vote')
router.register(r'flow_questions', UserFlowQuestionViewSet, base_name='flow_question')
router.register(r'favs', UserFavViewSet, base_name='fav')


urlpatterns = [
    path('admin/', admin.site.urls),

    # 文件
    path('meida/<path:path>', serve, {'document_root': MEDIA_ROOT}),

    # drf文档， title自定义
    path('docs', include_docs_urls(title='Amir')),

    path('api-auth/', include('rest_framework.urls')),

    # API LOGIN
    path('login/', obtain_jwt_token),
    # API URL
    re_path('', include(router.urls)),
]
