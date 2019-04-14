from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
# ...  # code

urlpatterns = [
    path('admin/', admin.site.urls),
]
