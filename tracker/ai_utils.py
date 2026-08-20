import os
import json
from google import genai
from google.genai import types
from django.conf import settings

def get_gemini_client():
    api_key = getattr(settings, 'GEMINI_API_KEY', '') or os.environ.get('GEMINI_API_KEY', '')
    return genai.Client(api_key=api_key)

def generate_job_analysis(job_description, user_skills=""):
    client = get_gemini_client()
    
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
    
    models_to_try = [
        'gemini-3.6-flash',
        'gemini-3.5-flash-lite',
        'gemini-3.1-flash-lite',
        'gemini-2.5-flash-lite'
    ]

    config = types.GenerateContentConfig(
        response_mime_type="application/json"
    )

    last_error = None
    for model_name in models_to_try:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=config
            )
            text_response = response.text or ""
            
            if text_response.startswith('```json'):
                text_response = text_response.replace('```json', '', 1)
            if text_response.startswith('```'):
                text_response = text_response.replace('```', '', 1)
            if text_response.endswith('```'):
                text_response = text_response.rsplit('```', 1)[0]
                
            parsed_data = json.loads(text_response.strip())
            return parsed_data
        except Exception as e:
            last_error = e
            continue
            
    raise Exception(f"Failed to analyze job description with AI. Error: {str(last_error)}")
