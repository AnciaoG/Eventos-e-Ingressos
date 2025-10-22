from apps.users.views import login_view, logout_view

urlpatterns += [
    path('api/login/', login_view),
    path('api/logout/', logout_view),
]
