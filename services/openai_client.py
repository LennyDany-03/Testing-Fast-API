import os
from dotenv import load_dotenv
from openai import AzureOpenAI  # ✅ Correct client for Azure

# Load environment variables from .env
load_dotenv()

# Load your Azure deployment name
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_VERSION")
)

# Define the feedback function
def get_essay_feedback(text: str) -> str:
    prompt = f"""
You are an expert IELTS examiner and academic coach. Evaluate the following IELTS Writing Task 2 essay and provide detailed, structured feedback.

Please break your response into these sections:

1. Task Response
- Did the essay fully address the prompt?
- Was a clear thesis/position stated and maintained?
- Were arguments well-supported with relevant examples?

2. Coherence and Cohesion
- Was the essay logically organized?
- Were transitions and cohesive devices used effectively?
- Was paragraphing appropriate?

3. Lexical Resource
- Analyze vocabulary range and accuracy.
- Highlight advanced words or idiomatic usage.
- Flag inappropriate or awkward word choices with alternatives.

4. Grammatical Range and Accuracy
- Identify issues with tenses, articles, agreement, sentence structure, punctuation.
- Provide 2–3 example sentences from the essay and explain errors + corrections.

5. Paragraph-Level Suggestions
- Go through each paragraph and mention:
    • Strengths
    • Specific improvements (e.g., clarity, structure, detail)

6. Tone and Register
- Assess if the tone was academic/formal enough.
- Flag any casual or informal language.

7. Band Score Estimation
- Provide an overall band score (1–9)
- Also give sub-scores for:
    • Task Response
    • Coherence & Cohesion
    • Lexical Resource
    • Grammar

8. Word Count and Time Efficiency
- Estimate word count.
- Suggest ideal time taken to write this essay during an exam (e.g., 35–40 mins).
- Was the essay too long or short?

9. Comparative Feedback (optional)
- If the essay is Band 8+, describe what a Band 9 would improve slightly better (e.g., nuance, conciseness, lexical depth).

10. Recommendations to Improve
- Suggest 3–5 actionable steps with links if possible.
    • Grammar: [e.g., Perfect Tense practice]
    • Vocabulary: [e.g., Academic Word List drills]
    • Structure: [e.g., Cohesive devices guide]

Essay:
\"\"\"{text}\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model=AZURE_DEPLOYMENT,
            messages=[
                {"role": "system", "content": "You are an IELTS examiner evaluating a Writing Task 2 essay."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=2000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[ERROR]: {str(e)}"
