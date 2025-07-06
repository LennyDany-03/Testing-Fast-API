from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.essay import Essay
from services.openai_client import get_essay_feedback

app = FastAPI()

# ✅ Enable CORS for frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://testing-ielts.vercel.app"],  # only allow frontend dev origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/evaluate-essay")
async def evaluate_essay(data: Essay):
    feedback = get_essay_feedback(data.text)
    return {"feedback": feedback}
