from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Contact
from ..serializers import ContactSerializer


class ContactApiDetail(APIView):
    def get(self, request, slug):
        contact = get_object_or_404(Contact, slug=slug)
        s_contact = ContactSerializer(
            contact,
            context={"request": request}
        )
        return Response(s_contact.data)


class ContactApiList(APIView):
    def get(self, request):
        contact_list = get_list_or_404(Contact)
        s_contact = ContactSerializer(
            contact_list,
            many=True,
            context={"request": request}
        )
        return Response(s_contact.data)
