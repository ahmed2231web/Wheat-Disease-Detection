import google.generativeai as genai
from decouple import config
import logging

logger = logging.getLogger(__name__)

# Configure the Gemini API
genai.configure(api_key=config('GEMINI_API_KEY'))  # Store in .env file

def get_gemini_response(disease, user_query=None):
    """Generate a response using the Gemini API in Urdu."""
    logger.info(f"Generating Urdu response for disease: {disease}, query: {user_query}")
    model = genai.GenerativeModel('gemini-2.0-pro-exp-02-05')  # Ensure this model exists
    
    if user_query:
        prompt = f"""Please respond in Urdu language only.
        The wheat plant has been detected with {disease}. User asks: {user_query}. 
        Provide a detailed but concise response about this specific query related to the detected disease."""
    else:
        prompt = f"""Please respond in Urdu language only.
        A wheat plant has been detected with {disease}. 
        Provide a brief overview of this disease, its impact on wheat crops, and basic management recommendations. 
        Keep the response concise but informative."""

    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.7,
                top_p=0.95,
                top_k=64,
                max_output_tokens=8192,
            )
        )
        logger.info("Urdu response received from Gemini API")
        return response.text.strip()
    except Exception as e:
        logger.error(f"Error generating Urdu response: {str(e)}")
        raise Exception(f"Failed to generate response: {str(e)}")