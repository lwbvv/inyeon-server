from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.MemberCreate)
router.register('profileImage', views.ProfileImageCreate)
router.register('profileText', views.ProfileTextCreate)
router.register('profileImageTest', views.ProfileImageTestCreate)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', 'namespace=rest_framework')),
    path('gender/', views.GenderCreate.as_view()),
    path('login/', views.LoginDetail.as_view()),
    path('email/', views.ConfirmRepetition.as_view()),
    path('assessment/', views.GetAssessmentData.as_view()),
    path('assessment/<string>', views.GetAssessmentData.as_view()),
    path('appraisal/<string>', views.Appraisal.as_view()),
    path('recommend/<string>', views.RecommendOpposite.as_view()),
]
    # url('(?P<pk>[0-9]+)/', views.member_detail),

# urlpatterns = format_suffix_patterns(urlpatterns)
