// ============================================
// Healthy Dietary Recommendation System JS
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('recommendationForm');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
        
        // Calculate BMI on input change
        const weight = document.getElementById('weight');
        const height = document.getElementById('height');
        if (weight && height) {
            weight.addEventListener('change', calculateBMI);
            height.addEventListener('change', calculateBMI);
        }
    }
});

/**
 * Calculate and display BMI
 */
function calculateBMI() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    const bmiDisplay = document.getElementById('bmi_display');
    
    if (weight && height && height > 0) {
        const bmi = (weight / ((height / 100) ** 2)).toFixed(2);
        let category = '';
        
        if (bmi < 18.5) category = '(Underweight)';
        else if (bmi < 25) category = '(Normal weight)';
        else if (bmi < 30) category = '(Overweight)';
        else category = '(Obese)';
        
        bmiDisplay.value = `${bmi} ${category}`;
    }
}

/**
 * Handle form submission
 */
async function handleFormSubmit(e) {
    e.preventDefault();
    
    // Show loading state
    const submitBtn = document.querySelector('button[type="submit"]');
    const submitText = document.getElementById('submitText');
    const spinner = document.getElementById('spinner');
    
    submitBtn.disabled = true;
    submitText.textContent = 'Processing...';
    spinner.style.display = 'inline-block';
    
    try {
        // Collect form data
        const age = parseInt(document.getElementById('age').value);
        const weight = parseFloat(document.getElementById('weight').value);
        const height = parseFloat(document.getElementById('height').value);
        const activityLevel = document.getElementById('activity_level').value;
        
        // Get health conditions
        const healthConditionsSelect = document.getElementById('health_conditions');
        const healthConditions = Array.from(healthConditionsSelect.selectedOptions)
            .map(option => option.value);
        
        // Get preferences
        const preferencesSelect = document.getElementById('preferences');
        const preferences = Array.from(preferencesSelect.selectedOptions)
            .map(option => option.value);
        
        // Prepare request payload
        const payload = {
            age: age,
            weight: weight,
            height: height,
            activity_level: activityLevel,
            health_conditions: healthConditions,
            preferences: preferences,
            k: 5
        };
        
        // Make API request
        const response = await fetch('/api/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to get recommendations');
        }
        
        const data = await response.json();
        
        if (data.success) {
            displayRecommendations(data);
        } else {
            showError(data.message || 'Failed to get recommendations');
        }
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message);
    } finally {
        // Reset button state
        submitBtn.disabled = false;
        submitText.textContent = 'Get Recommendations';
        spinner.style.display = 'none';
    }
}

/**
 * Display recommendations on page
 */
function displayRecommendations(data) {
    const resultsContainer = document.getElementById('resultsContainer');
    const recommendationsContainer = document.getElementById('recommendationsContainer');
    const similarUsersContainer = document.getElementById('similarUsersContainer');
    
    // Hide form section
    document.getElementById('recommendationForm').parentElement.parentElement.style.display = 'none';
    
    // Update metrics
    document.getElementById('result_bmi').textContent = data.user_metrics.bmi;
    document.getElementById('result_tdee').textContent = Math.round(data.user_metrics.tdee) + ' cal';
    document.getElementById('result_similar').textContent = data.similar_users.length;
    
    // Display recommendations
    let recommendationsHTML = '';
    data.recommendations.forEach((rec, index) => {
        recommendationsHTML += `
            <div class="recommendation-item fade-in">
                <div class="diet-name">${index + 1}. ${rec.diet}</div>
                <p><strong>Description:</strong> ${rec.description}</p>
                <div>
                    <span class="confidence-badge">Confidence: ${rec.confidence}%</span>
                    <span style="margin-left: 10px; color: #666; font-size: 0.9rem;">
                        Based on ${rec.count} similar profile${rec.count > 1 ? 's' : ''}
                    </span>
                </div>
            </div>
        `;
    });
    recommendationsContainer.innerHTML = recommendationsHTML;
    
    // Display similar users
    let usersHTML = '';
    data.similar_users.slice(0, 5).forEach((user, index) => {
        const profile = user.profile;
        usersHTML += `
            <div class="user-profile-card fade-in">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                    <strong>Profile ${index + 1}</strong>
                    <span class="similarity-score">Match: ${(user.similarity_score * 100).toFixed(1)}%</span>
                </div>
                <div class="profile-metric"><strong>Age:</strong> ${profile.age} years</div>
                <div class="profile-metric"><strong>Weight:</strong> ${profile.weight} kg</div>
                <div class="profile-metric"><strong>Height:</strong> ${profile.height} cm</div>
                <div class="profile-metric"><strong>Activity Level:</strong> ${capitalizeFirst(profile.activity_level)}</div>
                <div class="profile-metric"><strong>Health Conditions:</strong> ${profile.health_conditions.join(', ')}</div>
                <div class="profile-metric"><strong>Preferences:</strong> ${profile.preferences.join(', ')}</div>
            </div>
        `;
    });
    similarUsersContainer.innerHTML = usersHTML;
    
    // Show results section
    resultsContainer.style.display = 'block';
    
    // Scroll to results
    setTimeout(() => {
        resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
}

/**
 * Display error message
 */
function showError(message) {
    const errorContainer = document.getElementById('errorContainer');
    const errorMessage = document.getElementById('errorMessage');
    
    errorMessage.textContent = message;
    errorContainer.style.display = 'block';
    
    // Auto-hide error after 10 seconds
    setTimeout(() => {
        errorContainer.style.display = 'none';
    }, 10000);
}

/**
 * Capitalize first letter of string
 */
function capitalizeFirst(str) {
    return str.charAt(0).toUpperCase() + str.slice(1).replace(/_/g, ' ');
}

/**
 * Validate form inputs
 */
function validateForm() {
    const age = parseInt(document.getElementById('age').value);
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    
    if (isNaN(age) || age < 1 || age > 120) {
        showError('Age must be between 1 and 120');
        return false;
    }
    
    if (isNaN(weight) || weight < 10 || weight > 500) {
        showError('Weight must be between 10 and 500 kg');
        return false;
    }
    
    if (isNaN(height) || height < 50 || height > 250) {
        showError('Height must be between 50 and 250 cm');
        return false;
    }
    
    return true;
}

/**
 * Reset form and start over
 */
function resetForm() {
    document.getElementById('recommendationForm').reset();
    document.getElementById('resultsContainer').style.display = 'none';
    document.getElementById('errorContainer').style.display = 'none';
    document.getElementById('recommendationForm').parentElement.parentElement.style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
}
