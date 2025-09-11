from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# --- Load and Prepare Internship Data ---
try:
    internships_df = pd.read_csv('data\internship.csv')
    internships_df.fillna('', inplace=True)
except FileNotFoundError:
    print("Error: 'internship.csv' not found. Make sure the file is in the correct directory.")
    exit()

# --- Scoring Weights for Accuracy ---
WEIGHT_SKILL = 15
WEIGHT_LOCATION = 10
WEIGHT_SECTOR = 5
WEIGHT_SKILL_PERCENTAGE = 10 # Bonus for matching a high percentage of skills

# --- Flexible Education Hierarchy ---
# A higher number indicates a more advanced degree.
EDUCATION_LEVELS = {
    '10th pass': 0,
    '12th pass': 1,
    'diploma': 2,
    'ba': 3, 'b.sc': 3, 'b.com': 3, 'bba': 3, 'b.tech': 3, 'b.design': 3, 'b.pharma': 3,
    'ma': 4, 'm.sc': 4, 'mba': 4, 'm.tech': 4, 'm.pharma': 4
}

@app.route('/')
def home():
    """Serves your main HTML page."""
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    API endpoint that receives candidate data and returns the most accurate recommendations.
    """
    data = request.get_json()
    
    # Extract candidate details from the frontend
    user_qualification = data.get('qualification', '').lower()
    user_skills_str = data.get('skills', '').lower()
    user_sector = data.get('sector_interested', '').lower()
    user_location = data.get('location_interested', '').lower()
    
    user_skills = set(skill.strip() for skill in user_skills_str.split(',') if skill.strip())
    user_education_level = EDUCATION_LEVELS.get(user_qualification, -1)

    scored_internships = []

    for index, internship in internships_df.iterrows():
        
        # --- Rule 1: Flexible Education Check ---
        required_education = internship['required_education'].lower()
        required_education_level = EDUCATION_LEVELS.get(required_education, 0)
        
        if user_education_level < required_education_level:
            continue # Skip if user's education is not sufficient

        # --- Rule 2: Calculate Weighted Match Score ---
        current_score = 0
        
        # Score for location match
        if user_location and user_location == internship['location'].lower():
            current_score += WEIGHT_LOCATION

        # Score for sector match
        if user_sector and user_sector == internship['sector'].lower():
            current_score += WEIGHT_SECTOR
        
        # Score for skill matches
        required_skills = set(skill.strip() for skill in internship['required_skills'].lower().split(',') if skill.strip())
        if required_skills:
            matching_skills_count = len(user_skills.intersection(required_skills))
            current_score += matching_skills_count * WEIGHT_SKILL
            
            # Bonus score for matching a higher percentage of skills
            skill_match_ratio = matching_skills_count / len(required_skills)
            current_score += skill_match_ratio * WEIGHT_SKILL_PERCENTAGE

        if current_score > 0:
            internship_data = internship.to_dict()
            internship_data['score'] = current_score
            scored_internships.append(internship_data)

    # --- Rule 3: Rank and Select ---
    sorted_internships = sorted(scored_internships, key=lambda x: x['score'], reverse=True)
    top_recommendations = sorted_internships[:5]

    return jsonify(top_recommendations)

if __name__ == '__main__':
    app.run(debug=True)