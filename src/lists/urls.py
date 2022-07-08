from django.urls import path

from lists.views import ListsList, ListCreate, ListUpdate

app_name = "lists"

urlpatterns = [
	path('', ListsList.as_view(), name="list"),
	path('create/', ListCreate.as_view(), name="create"),
	path('update/<int:pk>', ListUpdate.as_view(), name="update"),
]