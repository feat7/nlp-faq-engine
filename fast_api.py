from typing import Optional
from fastapi import FastAPI
from faqengine import FAQEngine

app = FastAPI()
faqengine = FAQEngine(csv_file='gst_faq_1.csv')


@app.get("/")
def read_root():
    return {"message": "This is root of FAQEngine API. use route /faqengine?query=your-question-here"}


@app.get("/faqengine")
def read_item(query: Optional[str] = ""):
    results = faqengine.perform_query(query)
    return {"query": query, "results": results}
