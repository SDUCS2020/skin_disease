from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import SkinImage
from .utils import predict_disease, get_disease_info
import os


def home(request):
    """Home page view with upload form"""
    return render(request, 'skin_app/home.html')


def predict(request):
    """Handle image upload and prediction"""
    if request.method == 'POST' and request.FILES.get('skin_image'):
        # Save the uploaded image
        skin_image = SkinImage(image=request.FILES['skin_image'])
        skin_image.save()
        
        # Get the file path
        image_path = os.path.join(settings.MEDIA_ROOT, skin_image.image.name)
        
        # Make prediction
        disease_name, confidence = predict_disease(image_path)
        
        # Update the model with prediction results
        skin_image.prediction = disease_name
        skin_image.confidence = confidence
        skin_image.save()
        
        # Redirect to results page
        return redirect('result', image_id=skin_image.id)
    
    # If something went wrong, redirect back to home
    return redirect('home')


def result(request, image_id):
    """Display prediction results and recommendations"""
    skin_image = get_object_or_404(SkinImage, id=image_id)
    
    # Get disease information and recommendations
    disease_info = get_disease_info(skin_image.prediction)
    
    context = {
        'skin_image': skin_image,
        'disease_info': disease_info,
    }
    
    return render(request, 'skin_app/result.html', context)
