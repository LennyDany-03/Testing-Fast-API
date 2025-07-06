import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = os.getenv("AZURE_OPENAI_VERSION")  # like "2023-12-01-preview"

def get_essay_feedback(text: str):
    prompt = f"""
You're an IELTS examiner. Give:
1. Band Score (0-9)
2. Grammar Feedback
3. Vocabulary Feedback
4. Coherence and Cohesion
5. Suggestions for Improvement

Essay:
{text}
"""
    response = openai.ChatCompletion.create(
        engine=os.getenv("AZURE_DEPLOYMENT"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response['choices'][0]['message']['content']
