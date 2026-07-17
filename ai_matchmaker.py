
from pydantic import BaseModel, Field
from google import genai
import json
import os

class MatchResult(BaseModel):
    ai_match_score: int = Field(..., description='0-100 match score')
    ai_reasoning: str = Field(..., description='Short explanation')

def run_ai_matchmaker(student_profile, job_listing):
    api_key = os.environ.get('GEMINI_API_KEY')

    if not api_key:
        return {
            'ai_match_score': 75,
            'ai_reasoning': 'Demo mode: Gemini API key not configured.'
        }

    client = genai.Client(api_key=api_key)

    prompt = f'''
    Analyze this student profile against the job listing.

    STUDENT:
    {student_profile}

    JOB:
    {job_listing}

    Return a score 0-100 and short reasoning.
    '''

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': MatchResult.model_json_schema()
        }
    )

    return json.loads(response.text)
