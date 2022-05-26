from django.urls import path,include

from . import views

urlpatterns = [
    path('about',views.about,name="about"),
    path('amazon',views.amazon,name="amazon"),
    path('jpmc',views.jpmc,name="jpmc"),
    path('deloitte',views.deloitte,name="deloitte"),
    path('tcs',views.tcs,name="tcs"),
    path('infosys',views.infosys,name="infosys"),
    path('wipro',views.wipro,name="wipro"),
    path('accenture',views.accenture,name="accenture"),
    path('lti',views.lti,name="lti"),
    path('atlassian',views.atlassian,name="atlassian"),
    path('ncr',views.ncr,name="ncr"),
    path('cognizant',views.cognizant,name="cognizant"),
    path('factset',views.factset,name="factset"),
    path('capgemini',views.capgemini,name="capgemini"),
    path('acs',views.acs,name="acs"),
    path('accolite',views.accolite,name="accolite"),
    path('f5',views.f5,name="f5"),
    path('statestreet',views.statestreet,name="statestreet"),
    path('dbs',views.dbs,name="dbs"),
    path('others',views.others,name="others"),
    path('discussions',views.discussions,name="discussions"),
    path('statistics',views.statistics,name="statistics"),
    path('event',views.event,name="event"),
]
