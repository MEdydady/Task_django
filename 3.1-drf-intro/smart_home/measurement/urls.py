from django.urls import path

from .views import SensorCreateView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path("sensors/", SensorCreateView.as_view(), name="create_sensor"),
    path("sensors/<int:pk>/", SensorDetailView.as_view(), name="sensor"),
    path("measurements/", MeasurementCreateView.as_view(), name="measurement"),
]
