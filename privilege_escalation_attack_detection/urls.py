"""privilege_escalation_attack_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from Remote_User import views as remoteuser
from privilege_escalation_attack_detection import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', remoteuser.login, name="login"),
    path('Register1/', remoteuser.Register1, name="Register1"),
    path('Predict_Escalation_Attack_Detection/', remoteuser.Predict_Escalation_Attack_Detection, name="Predict_Escalation_Attack_Detection"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path('serviceproviderlogin/',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    path('charts/(?P<chart_type>\)', serviceprovider.charts,name="charts"),
    path('charts1/(?P<chart_type>\)', serviceprovider.charts1, name="charts1"),
    path('likeschart/(?P<like_chart>\)', serviceprovider.likeschart, name="likeschart"),
    path('View_Predicted_Escalation_Attack_Detection_Ratio/', serviceprovider.View_Predicted_Escalation_Attack_Detection_Ratio, name="View_Predicted_Escalation_Attack_Detection_Ratio"),
    path('train_model/', serviceprovider.train_model, name="train_model"),
    path('View_Predicted_Escalation_Attack_Detection_Details/', serviceprovider.View_Predicted_Escalation_Attack_Detection_Details, name="View_Predicted_Escalation_Attack_Detection_Details"),
    path('Download_Trained_DataSets/', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),
     path('edit-client/<int:id>/', remoteuser.edit_client, name='edit_client'),
    path('delete-client/<int:id>/', remoteuser.delete_client, name='delete_client'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
