from typing import Optional
from fastapi import FastAPI
from faqengine import FAQEngine

app = FastAPI()
faqengine = FAQEngine(csv_file='faqs.csv')


@app.get("/")
def home():
    return {"message": "This is root of FAQEngine API. use route /faqengine?query=your-question-here"}


@app.get("/faqengine")
def get_similary_queries(query: Optional[str] = ""):
    results = faqengine.perform_query(query)
    return {"query": query, "results": results}
