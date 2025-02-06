�
     �g.  �                   �|   � d Z ddlmZ ddlmZmZ  edej                  j                  �       ed ed�      �      gZy)a�  
URL configuration for meal_mate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
�    )�admin)�path�includezadmin/� zdelivery.urlsN)	�__doc__�django.contribr   �django.urlsr   r   �site�urls�urlpatterns� �    �7/Users/kodnest/learn-django/meal_mate/meal_mate/urls.py�<module>r      s<   ���  !� %� 	��5�:�:�?�?�#���W�_�%�&��r   