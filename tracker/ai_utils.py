import os
import json
import google.generativeai as genai
from django.conf import settings

def get_gemini_model():
    genai.configure(api_key=settings.GEMINI_API_KEY)
    
    # User's specified fallback order
    models_to_try = [
        'gemini-3.5-flash-lite',
        'gemini-3.1-flash-lite',
        'gemini-2.5-flash-lite',
        'gemini-2.0-flash-lite'
    ]
    
    # Try to fetch available models and find the best match
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        for model_name in models_to_try:
            full_model_name = f'models/{model_name}'
            if full_model_name in available_models:
                return genai.GenerativeModel(model_name)
                
        # If none found in list, fallback to a known default or just try the first one and let it fail
        # Sometime models aren't listed but are available. We'll try the list in order using an exception block.
    except Exception:
        pass
        
    return genai.GenerativeModel(models_to_try[0])

def generate_job_analysis(job_description, user_skills=""):
    model = get_gemini_model()
    
    candidate_context = ""
    if user_skills and str(user_skills).strip():
        candidate_context = f"\n    Candidate Profile Skills & Background:\n    {str(user_skills).strip()}\n"
    else:
        candidate_context = "\n    Candidate Profile Skills & Background:\n    Fullstack Software Engineer with Python, Django, JavaScript, React, PostgreSQL, Docker, REST APIs, Git\n"

    prompt = f"""
    Analyze the following job description against the candidate's skills profile and provide a JSON response with exactly these keys:
    - job_summary: A brief 2-3 sentence summary of the role.
    - required_skills: A comma-separated list or short text describing core skills.
    - required_experience: A short description of the required years of experience and background.
    - important_technologies: A list of the main tools, languages, or software mentioned.
    - interview_preparation_suggestions: 3-4 bullet points on what to prepare for the interview.
    - match_score: An integer number (0-100) representing the exact match percentage between the Candidate Skills and the Job Requirements.
    - match_analysis: 2-3 sentences evaluating the candidate's matching skills, identifying any skill gaps, and giving an overall fit assessment.
    - interview_questions: 3-4 role-specific technical and behavioral interview questions with brief answer strategies (format as a list of strings or bullet points).

    Return ONLY valid JSON without markdown blocks or other text.
    {candidate_context}
    Job Description:
    {job_description}
    """
    
    try:
        response = model.generate_content(prompt)
        text_response = response.text
        
        # Clean up markdown if the model still returns it
        if text_response.startswith('```json'):
            text_response = text_response.replace('```json', '', 1)
        if text_response.endswith('```'):
            text_response = text_response.rsplit('```', 1)[0]
            
        parsed_data = json.loads(text_response.strip())
        return parsed_data
    except Exception as e:
        # Fallback loop trying other models if the first one fails due to model availability
        models_to_try = [
            'gemini-3.5-flash-lite',
            'gemini-3.1-flash-lite',
            'gemini-2.5-flash-lite',
            'gemini-2.0-flash-lite'
        ]
        
        for fallback_model in models_to_try[1:]:
            try:
                fallback = genai.GenerativeModel(fallback_model)
                resp = fallback.generate_content(prompt)
                
                text_resp = resp.text
                if text_resp.startswith('```json'):
                    text_resp = text_resp.replace('```json', '', 1)
                if text_resp.endswith('```'):
                    text_resp = text_resp.rsplit('```', 1)[0]
                    
                return json.loads(text_resp.strip())
            except Exception:
                continue
                
        raise Exception(f"Failed to analyze job description with AI. Error: {str(e)}")
