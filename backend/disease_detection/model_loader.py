import os
import numpy as np
from tensorflow.keras.models import load_model
import logging

logger = logging.getLogger(__name__)

# Global variable to cache the model
_model_instance = None

# Disease labels
DISEASE_LABELS = ['healthy', 'leaf rust', 'crown and root rot', 'loose smut']

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_disease_model():
    """Load and return the pre-trained model, caching it globally."""
    global _model_instance
    
    if _model_instance is not None:
        logger.info("Returning cached model instance")
        return _model_instance
    
    try:
        possible_paths = [
            os.path.join(BASE_DIR, 'disease_detection', 'models', 'wheatDiseaseModel.h5'),
            os.path.join(BASE_DIR, 'models', 'wheatDiseaseModel.h5'),
            os.path.join(os.path.dirname(__file__), 'models', 'wheatDiseaseModel.h5')
        ]
        
        model_path = None
        for path in possible_paths:
            if os.path.exists(path):
                model_path = path
                break
                
        if model_path is None:
            raise FileNotFoundError(f"Model file not found. Tried paths: {possible_paths}")
            
        logger.info(f"Loading model from: {model_path}")
        _model_instance = load_model(model_path)
        
        if not _model_instance.optimizer:
            _model_instance.compile(
                optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy']
            )
            logger.info("Model compiled with default settings")
        
        # Warm up the model
        dummy_input = np.zeros((1, 64, 64, 3))
        _model_instance.predict(dummy_input, verbose=0)
        logger.info("Model warmed up successfully")
        
        return _model_instance
        
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise

def predict_disease(image_array):
    """Make a prediction with the loaded model."""
    try:
        model = get_disease_model()
        
        if len(image_array.shape) != 4 or image_array.shape[1:] != (64, 64, 3):
            raise ValueError(f"Expected input shape (batch, 64, 64, 3), got {image_array.shape}")
            
        if image_array.max() > 1.0 or image_array.min() < 0.0:
            logger.warning("Input values not in range [0,1], normalizing...")
            image_array = image_array / 255.0
        
        logger.info("Making prediction...")
        prediction = model.predict(image_array, verbose=0)
        disease_index = np.argmax(prediction[0])
        logger.info(f"Prediction complete: {DISEASE_LABELS[disease_index]}")
        
        return prediction
        
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise