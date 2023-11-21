from django.shortcuts import render,redirect
from django.views import View
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,"Home/Home.html")

from django.views import View
from .models import ProcessedImage
from .utils import process_image

class ProcessImageView(View):
    template_name = 'Home/Model.html'

    def get(self, request):
        # Handle GET request (display the form)
        return render(request, self.template_name)

    def post(self, request):
        image_file = request.FILES['image']

        processed_image = process_image(image_file)

        original_image_model = ProcessedImage(original_image=image_file)
        original_image_model.save()

        processed_image_model = ProcessedImage(processed_image=processed_image)
        processed_image_model.save()

        return redirect('Result')
    
from django.views.generic import TemplateView
from .models import ProcessedImage

class Result(TemplateView):
    template_name = 'Home/Result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        latest_original_image = ProcessedImage.objects.filter(original_image__isnull=False).latest('id')
        latest_processed_image = ProcessedImage.objects.filter(processed_image__isnull=False).latest('id')

        context['original_image'] = latest_original_image
        context['processed_image'] = latest_processed_image

        return context

