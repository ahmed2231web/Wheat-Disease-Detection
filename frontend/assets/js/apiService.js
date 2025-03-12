/**
 * API Service
 * 
 * This service handles all API calls related to disease detection and chat functionality
 */

// Create a self-executing function to avoid global namespace pollution
(function(window) {
    // Define API_URL in a local scope
    const API_URL = 'http://localhost:8000/disease';
    
    // Create the ApiService object
    const apiService = {
        /**
         * Upload an image for disease detection
         * @param {File} imageFile - The image file to upload
         * @returns {Promise} - Promise that resolves with detection results
         */
        async detectDisease(imageFile) {
            try {
                const formData = new FormData();
                formData.append('image', imageFile);
                
                const response = await axios.post(`${API_URL}/upload/`, formData);
                console.log('Detection response:', response.data);
                return response.data;
            } catch (error) {
                console.error('Error detecting disease:', error);
                throw error.response?.data || error.message;
            }
        },
        
        /**
         * Send a chat message to the AI assistant
         * @param {string} disease - The detected disease
         * @param {string} query - The user's query
         * @returns {Promise} - Promise that resolves with chat response
         */
        async sendChatMessage(disease, query) {
            try {
                const response = await axios.post(`${API_URL}/chat/`, {
                    disease,
                    query
                });
                return response.data;
            } catch (error) {
                console.error('Error sending chat message:', error);
                throw error.response?.data || error.message;
            }
        }
    };

    // Expose apiService to the global scope
    window.apiService = apiService;
    
    console.log('ApiService initialized and exposed globally');
})(window);
