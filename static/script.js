document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('recommendation-form');
    const resultsContainer = document.getElementById('results-container');
    const recommendationsDiv = document.getElementById('recommendations');
    const loadingDiv = document.getElementById('loading');
    const errorDiv = document.getElementById('error-message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault(); // Stop the form from reloading the page

        // 1. Show loading spinner and clear previous results
        resultsContainer.classList.remove('hidden');
        loadingDiv.classList.remove('hidden');
        errorDiv.classList.add('hidden');
        recommendationsDiv.innerHTML = '';

        // 2. Get form data and map it to the keys the backend expects
        const formData = new FormData(form);
        const candidateData = {
            qualification: formData.get('education'),
            skills: formData.get('skills'),
            sector_interested: formData.get('sector_interests'),
            location_interested: formData.get('location')
        };

        try {
            // 3. Send the corrected data to the Flask backend
            const response = await fetch('/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(candidateData),
            });

            if (!response.ok) {
                throw new Error('Something went wrong with the request.');
            }

            const recommendations = await response.json();

            // 4. Hide loading spinner and display results
            loadingDiv.classList.add('hidden');
            displayRecommendations(recommendations);

        } catch (error) {
            // 5. Handle any errors
            loadingDiv.classList.add('hidden');
            errorDiv.textContent = `Error: ${error.message}`;
            errorDiv.classList.remove('hidden');
        }
    });

    function displayRecommendations(recs) {
        if (!recs || recs.length === 0) {
            recommendationsDiv.innerHTML = '<p style="text-align: center;">No matching internships found. Please try different criteria.</p>';
            return;
        }

        recs.forEach(rec => {
            const card = document.createElement('div');
            card.className = 'recommendation-card';

            // Format the stipend for display, providing a fallback
            const stipendText = (rec.stipend && !isNaN(rec.stipend))
                ? `₹${new Intl.NumberFormat('en-IN').format(rec.stipend)} /month`
                : 'Not Disclosed';

            // Ensure other data fields have fallbacks
            const title = rec.title || 'No Title';
            const company = rec.company_name || 'No Company Name';
            const location = rec.location || 'N/A';
            
            // Add the Match Score from the backend
            const score = rec.score ? rec.score.toFixed(0) : 'N/A';

            card.innerHTML = `
                <div class="card-header">
                    <h3>${title}</h3>
                    <p class="company">${company}</p>
                </div>
                <div class="card-details">
                    <p class="card-stipend">💰 ${stipendText}</p>
                    <p><strong>📍 Location:</strong> ${location}</p>
                    <p><strong>🎯 Match Score:</strong> ${score}</p>
                </div>
                <p class="card-description">${rec.description || 'No description available.'}</p>
            `;
            recommendationsDiv.appendChild(card);
        });
    }
});