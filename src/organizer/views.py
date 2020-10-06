from django.views.generic import TemplateView


class Status(TemplateView):
    """ Healthcheck provider """
    extra_context = {"status": "Good"}
    template_name = "organizer/status.html"
