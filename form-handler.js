// Form submission handler for ALMA Visa Consultants
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('consultationForm');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(form);
        
        try {
            // Simple email delivery using Formspree
            const response = await fetch('https://formspree.io/f/xeqyqvkj', { // Using a verified Formspree endpoint
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });
            
            if (!response.ok) {
                throw new Error('Form submission failed');
            }
            
            const result = await response.json();
            
            if (result.ok) {
                // Success - show confirmation and reset form
                alert('Thank you for your inquiry! We will contact you shortly.');
                form.reset();
            } else {
                throw new Error('Form submission failed');
            }
            
        } catch (error) {
            console.error('Form submission error:', error);
            alert('There was an issue submitting your form. Please try again or contact us directly at contact@almaukvisas.co.uk');
        }
    });
});
