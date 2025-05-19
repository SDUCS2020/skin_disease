# Skin Disease Detection Web Application

This Django application uses an Attention U-Net model to predict skin diseases from uploaded images.

## Setup Instructions

1. Clone this repository
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Place your trained `attention_unet_model.h5` file in the `skin_app/model/` directory
4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Visit http://127.0.0.1:8000/ in your browser

## Features

- User-friendly interface for image upload
- AI-powered skin disease prediction
- Detailed disease information and recommendations
- Modern and responsive design

## Model Information

The application uses an Attention U-Net model for image classification. The model should be trained to recognize various skin diseases and provide accurate predictions.

## Important Note

This application is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions regarding a medical condition.
