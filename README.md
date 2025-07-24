# genai_project
This project simulates a research and development ecosystem where distinct agents collaborate, compete, and adapt their strategies based on real-time inputs from external sources.
Project Title: Gen AI Adaptive Research & Innovation Agent Ecosystem

Author: Abdelghany Elshershapy

Description:
This FastAPI application fetches data from a public URL, extracts age values, and counts how many people are aged 50 or older.

Key Code Parts:
- varOcg: stores the API response
- varFiltersCg: stores filtered age results >= 50
- __define-ocg__: marks the filtering logic area

Run Instructions:
1. Create virtual environment
2. Install FastAPI and Uvicorn
3. Run with: uvicorn api.main:app --reload
4. Go to: http://127.0.0.1:8000/docs and click "Try it out"

Result:
Returns a JSON object with the count of people aged 50+
