from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
# from webapp.forms import SketchpadForm
from webapp.models import Guestbook, STATUS_CHOICES


def index_view(request):
    guestbooks = Guestbook.objects.order_by("-updated_time")
    context = {"guestbooks": guestbooks}
    return render(request, "index.html", context)

