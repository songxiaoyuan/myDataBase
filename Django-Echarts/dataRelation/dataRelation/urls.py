from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^get_investment_relation', 'investment_relation.views.home', name='home'),
    url(r'^get_key_hot_words', 'key_hot_words.views.home', name='home'),
    url(r'^get_managers_of_company', 'managers_of_company.views.home', name='home'),
    url(r'^get_news_publish_time_count', 'news_publish_time_count.views.home', name='home'),
    url(r'^get_news_report_count_change', 'news_report_count_change.views.home', name='home'),
    url(r'^get_news_sentiment', 'news_sentiment.views.home', name='home'),
    url(r'^get_news_source', 'news_source.views.home', name='home'),
    url(r'^get_news_year_count', 'news_year_count.views.home', name='home'),
    url(r'^get_company_scope', 'company_scope.views.home', name='home'),
    url(r'^get_company_competitor', 'company_competitor.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
