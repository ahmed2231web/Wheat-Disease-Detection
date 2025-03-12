from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
from .model_loader import get_disease_model, DISEASE_LABELS, predict_disease
from .chatbot import get_gemini_response
from PIL import Image
import numpy as np
import logging

logger = logging.getLogger(__name__)

# Load model once at startup
model = get_disease_model()

def preprocess_image(image_file):
    """Preprocess the uploaded image for prediction."""
    try:
        img = Image.open(image_file).convert('RGB').resize((64, 64))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        logger.info("Image preprocessed successfully")
        return img_array
    except Exception as e:
        logger.error(f"Error preprocessing image: {str(e)}")
        raise

class UploadImageView(APIView):
    def post(self, request):
        logger.info("Received image upload request")
        serializer = ImageUploadSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        image_file = serializer.validated_data['image']
        try:
            img_array = preprocess_image(image_file)
            logger.info("Starting prediction")
            prediction = predict_disease(img_array)
            disease_index = np.argmax(prediction)
            detected_disease = DISEASE_LABELS[disease_index]
            logger.info(f"Detected disease: {detected_disease}")
            
            chatbot_response = get_gemini_response(detected_disease)
            logger.info("Chatbot response received")
            
            return Response({
                'disease': detected_disease,
                'chatbot_response': chatbot_response
            }, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChatWithGeminiView(APIView):
    def post(self, request):
        logger.info("Received chat request")
        disease = request.data.get('disease')
        user_query = request.data.get('query')
        
        if not disease or not user_query:
            logger.warning("Missing disease or query in chat request")
            return Response({'error': 'Missing disease or query'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            response = get_gemini_response(disease, user_query)
            logger.info("Chatbot response received")
            return Response({'chatbot_response': response}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error in chat response: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)