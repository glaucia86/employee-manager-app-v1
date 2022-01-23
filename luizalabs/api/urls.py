from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView

urlpatterns = {
    path(r'employee/', CreateView.as_view(), name="create"),
    path(r'employee/<int:pk>/', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
