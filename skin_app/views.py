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
        try:
            skin_image = SkinImage(image=request.FILES['skin_image'])
            skin_image.save()
            
            image_path = os.path.join(settings.MEDIA_ROOT, skin_image.image.name)
            
            print(f"Image path: {image_path}")
            print(f"File exists: {os.path.exists(image_path)}")
            
            disease_name, confidence = predict_disease(image_path)
            
            print(f"Prediction result: {disease_name}, confidence: {confidence}")
            
            skin_image.prediction = disease_name
            skin_image.confidence = confidence
            skin_image.save()
            
            return redirect('result', image_id=skin_image.id)
        except Exception as e:
            import traceback
            print(f"Prediction error: {str(e)}")
            print(traceback.format_exc())
            
            if 'skin_image' in locals():
                skin_image.prediction = "error"
                skin_image.confidence = 0
                skin_image.save()
                return redirect('result', image_id=skin_image.id)
    
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
