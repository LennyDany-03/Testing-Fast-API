import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = os.getenv("AZURE_OPENAI_VERSION")  # e.g., "2023-12-01-preview"

def get_essay_feedback(text: str):
    prompt = f"""
You are an expert IELTS examiner. Analyze the following IELTS Writing Task 2 essay and provide comprehensive, actionable, and student-friendly feedback based on the official IELTS band descriptors.

Break your feedback into the following detailed sections:

1. Task Response
- Did the writer address all parts of the prompt?
- Was a clear position (thesis) presented and maintained?
- Were ideas fully developed and supported with relevant examples?

2. Coherence and Cohesion
- Was the essay well organized and logically structured?
- Were appropriate cohesive devices used without overuse?
- Was paragraphing effective?

3. Lexical Resource
- Analyze the range and accuracy of vocabulary.
- Mention any advanced or less common words used well.
- Point out incorrect word choices, inappropriate collocations, or awkward phrasing — and explain why.

4. Grammatical Range and Accuracy
- Highlight errors in tense, agreement, articles, and punctuation.
- Evaluate the range of sentence structures (simple, compound, complex).
- Include specific examples from the essay and suggest corrections.

5. Specific Error Examples
- Quote 2–3 exact sentences from the essay that contain errors or weaknesses.
- Explain what the issue is and how to correct it.

6. Band Score Estimation
- Provide an overall estimated IELTS band score (1–9).
- Optionally, break it down per category (TR, CC, LR, GRA).

7. Suggestions for Improvement
- Give 3–5 specific tips or exercises to improve weak areas.
- Recommend resources (e.g., grammar websites, vocabulary tools, writing practice).

Essay:
\"\"\"
{text}
\"\"\"
"""

    response = openai.ChatCompletion.create(
        engine=os.getenv("AZURE_DEPLOYMENT"),  # Example: "gpt-35-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response['choices'][0]['message']['content']
