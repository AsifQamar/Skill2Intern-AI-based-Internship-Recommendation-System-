from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# --- Load and Prepare Internship Data ---
try:
    internships_df = pd.read_csv('data/internship.csv')
    
    # Clean the 'stipend' column
    internships_df['stipend'] = internships_df['stipend'].str.replace('₹', '').str.replace('/month', '').str.strip()
    internships_df['stipend'] = pd.to_numeric(internships_df['stipend'], errors='coerce').fillna(0).astype(int)
    
    # Create a master list of all unique skills from the dataset
    internships_df.dropna(subset=['required_skills'], inplace=True)
    all_skills = set()
    for skills_list in internships_df['required_skills'].str.lower().str.split(','):
        if isinstance(skills_list, list):
            for skill in skills_list:
                all_skills.add(skill.strip())
    
    # Fill any remaining NaN values
    internships_df.fillna('', inplace=True)

except FileNotFoundError:
    print("Error: 'internship.csv' not found. Make sure the file is in the 'data' directory.")
    all_skills = set() # Ensure all_skills exists even if file is not found
    exit()

# --- Scoring Weights for Accuracy ---
WEIGHT_SKILL = 15
WEIGHT_LOCATION = 10
WEIGHT_SECTOR = 5
WEIGHT_SKILL_PERCENTAGE = 10 # Bonus for matching a high percentage of skills

# --- Flexible Education Hierarchy ---
EDUCATION_LEVELS = {
    '10th pass': 0, '12th pass': 1, 'diploma': 2,
    'ba': 3, 'b.sc': 3, 'b.com': 3, 'bba': 3, 'b.tech': 3, 'b.design': 3, 'b.pharma': 3,
    'ma': 4, 'm.sc': 4, 'mba': 4, 'm.tech': 4, 'm.pharma': 4
}

@app.route('/')
def home():
    """Serves your main HTML page and passes the list of skills."""
    return render_template('index.html', all_skills=sorted(list(all_skills)))

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    API endpoint that receives candidate data and returns recommendations.
    """
    data = request.get_json()
    
    # Extract candidate details
    user_qualification = data.get('qualification', '').lower()
    user_skills_str = data.get('skills', '').lower()
    user_sector = data.get('sector_interested', '').lower()
    user_location = data.get('location_interested', '').lower()
    
    # Filter user skills to only include skills that exist in our master list
    user_skills_list = [skill.strip() for skill in user_skills_str.split(',') if skill.strip()]
    valid_user_skills = set(skill for skill in user_skills_list if skill in all_skills)
    
    user_education_level = EDUCATION_LEVELS.get(user_qualification, -1)

    scored_internships = []

    for index, internship in internships_df.iterrows():
        
        required_skills = set(skill.strip() for skill in internship['required_skills'].lower().split(',') if skill.strip())

        # --- CORRECTED LOGIC ---
        # If the user typed skills, but none of their valid skills match this internship, skip it.
        if user_skills_str and not valid_user_skills.intersection(required_skills):
            continue

        # Education Check
        required_education = internship['required_education'].lower()
        required_education_level = EDUCATION_LEVELS.get(required_education, 0)
        
        if user_education_level < required_education_level:
            continue

        current_score = 0
        
        # Location match score
        if user_location and user_location in internship['location'].lower():
            current_score += WEIGHT_LOCATION

        # Sector match score
        if user_sector and user_sector in internship['sector'].lower():
            current_score += WEIGHT_SECTOR
        
        # Skill match score
        if required_skills and valid_user_skills:
            matching_skills_count = len(valid_user_skills.intersection(required_skills))
            if matching_skills_count > 0:
                current_score += matching_skills_count * WEIGHT_SKILL
                skill_match_ratio = matching_skills_count / len(required_skills)
                current_score += skill_match_ratio * WEIGHT_SKILL_PERCENTAGE

        if current_score > 0:
            internship_data = internship.to_dict()
            internship_data['score'] = current_score
            scored_internships.append(internship_data)

    # Rank and select top 3
    sorted_internships = sorted(scored_internships, key=lambda x: x['score'], reverse=True)
    top_recommendations = sorted_internships[:3]

    return jsonify(top_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
