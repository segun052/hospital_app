from accounts.views import UserAuthenticationViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register(
    r'accounts',
    UserAuthenticationViewset,
    basename='user_authentication')
    
# router.register(
#     r'accounts',
#     AuthViewSet,
#     basename='user_login')

urlpatterns = router.urls
