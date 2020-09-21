from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def home_page(request):
    return render(request, "home.html", context={"header": "ИНФОРМАЦИЯ о проекте 'БЕЗОПАСНЫЙ ГОРОД'"})


class HomeView(View):
    def dispatch(self, request, *args, **kwargs):
        return render(request, "home.html", context={"header": "Main Page"})


class AboutUsView(TemplateView):
    template_name = "about_us.html"

    def get_context_data(self, **kwargs):
        return {
            "header":"About us:"
        }

class ContactView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        return {
            "header":"Our contact page"
        }

class FeedBackView(TemplateView):
    template_name = "feedback.html"

    def get_context_data(self, **kwargs):
        return {
            "header":"Our feedback page:"
        }