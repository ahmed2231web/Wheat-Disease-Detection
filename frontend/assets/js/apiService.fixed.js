/**
 * API Service
 * 
 * This service handles all API calls related to disease detection and chat functionality
 */

// Create a self-executing function to avoid global namespace pollution
(function(window) {
    // Define API_URL in a local scope
    const API_URL = 'http://localhost:8000/api';
    
    // Create the ApiService object
    const apiService = {
        /**
         * Get authentication headers for API requests
         * @param {boolean} isFormData - Whether the request is for form data
         * @returns {Object} - Headers object with Authorization header
         */
        getAuthHeaders(isFormData = false) {
            const accessToken = sessionStorage.getItem('accessToken');
            const headers = {
                'Authorization': `Bearer ${accessToken}`
            };
            
            if (!isFormData) {
                headers['Content-Type'] = 'application/json';
            }
            
            return headers;
        },
        
        /**
         * Upload an image for disease detection
         * @param {File} imageFile - The image file to upload
         * @returns {Promise} - Promise that resolves with detection results
         */
        async detectDisease(imageFile) {
            try {
                const formData = new FormData();
                formData.append('image', imageFile);
                
                console.log('Sending disease detection request with token:', sessionStorage.getItem('accessToken'));
                
                const response = await axios.post(`${API_URL}/disease/detect/`, formData, {
                    headers: this.getAuthHeaders(true)
                });
                
                return response.data;
            } catch (error) {
                console.error('Error detecting disease:', error);
                throw error.response?.data || error.message;
            }
        },
        
        /**
         * Send a chat message to the AI assistant
         * @param {string} message - The user's message
         * @param {number} detectionId - The ID of the detection to associate with the message
         * @returns {Promise} - Promise that resolves with chat response
         */
        async sendChatMessage(message, detectionId) {
            try {
                const response = await axios.post(`${API_URL}/disease/chat/`, {
                    message,
                    detection_id: detectionId
                }, {
                    headers: this.getAuthHeaders()
                });
                
                return response.data;
            } catch (error) {
                console.error('Error sending chat message:', error);
                throw error.response?.data || error.message;
            }
        },
        
        /**
         * Get chat history for a specific detection
         * @param {number} detectionId - The ID of the detection to get chat history for
         * @returns {Promise} - Promise that resolves with chat history
         */
        async getChatHistory(detectionId) {
            try {
                const url = detectionId 
                    ? `${API_URL}/disease/chat-history/${detectionId}/` 
                    : `${API_URL}/disease/chat-history/`;
                    
                const response = await axios.get(url, {
                    headers: this.getAuthHeaders()
                });
                
                return response.data;
            } catch (error) {
                console.error('Error getting chat history:', error);
                throw error.response?.data || error.message;
            }
        },
        
        /**
         * Get user's detection history
         * @returns {Promise} - Promise that resolves with detection history
         */
        async getDetectionHistory() {
            try {
                const response = await axios.get(`${API_URL}/disease/history/`, {
                    headers: this.getAuthHeaders()
                });
                
                return response.data;
            } catch (error) {
                console.error('Error getting detection history:', error);
                throw error.response?.data || error.message;
            }
        }
    };

    // Expose apiService to the global scope
    window.apiService = apiService;
    
    console.log('ApiService initialized and exposed globally');
})(window);
