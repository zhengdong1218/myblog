from . import views
from django.urls import path,include
urlpatterns=[
    path('article-list/',views.article_list,name='article_list_article_urls'),
    path('article-detail/<int:id_detail>/',views.article_detail,name='article_detail_article_urls'),
    path('article-create/', views.article_create, name='article_create_article_urls'),
    path('article-delete/<int:id_delete>/',views.article_delete, name='article_delete_article_urls'),
    path('article-update/<int:id_update>/',views.article_update, name='article_update_article_urls')
]
