from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from config import Config
from search import google_search
from scraper import WebScraper
from rag import RAGPipeline
from database import Database

# ------------------------------------
# FastAPI App
# ------------------------------------
app = FastAPI(
    title="AI Research Assistant",
    version="1.0.0",
    description="RAG-based AI Research Assistant"
)

templates = Jinja2Templates(directory="templates")

# ------------------------------------
# Initialize Components
# ------------------------------------
scraper = WebScraper()
rag = RAGPipeline()
database = Database()

# ------------------------------------
# Home Page
# ------------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "question": "",
            "answer": "",
            "sources": []
        }
    )

# ------------------------------------
# Ask Question
# ------------------------------------
@app.post("/ask", response_class=HTMLResponse)
async def ask(
    request: Request,
    question: str = Form(...)
):
    answer = ""
    sources = []

    try:

        # Search the web
        urls = google_search(
            question,
            num_results=Config.SEARCH_RESULTS
        )

        sources = urls

        # Scrape and store documents
        for index, url in enumerate(urls):

            page = scraper.scrape(url)

            if not page.get("content"):
                continue

            rag.add_document(
                doc_id=str(index),
                title=page["title"],
                content=page["content"],
                source=url
            )

            database.add_document(
                doc_id=str(index),
                title=page["title"],
                source=url
            )

        # Generate answer
        answer = rag.answer(
            question,
            top_k=Config.TOP_K_RESULTS
        )

        # Save search history
        database.save_search(
            question,
            answer
        )

    except Exception as e:
        answer = f"Error: {str(e)}"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "question": question,
            "answer": answer,
            "sources": sources
        }
    )

# ------------------------------------
# Search History
# ------------------------------------
@app.get("/history")
async def history():
    return JSONResponse(
        content={
            "history": database.get_search_history()
        }
    )

# ------------------------------------
# Stored Documents
# ------------------------------------
@app.get("/documents")
async def documents():
    return JSONResponse(
        content={
            "documents": database.get_documents()
        }
    )

# ------------------------------------
# Health Check
# ------------------------------------
@app.get("/health")
async def health():
    return {
        "status": "running",
        "application": "AI Research Assistant"
    }

# ------------------------------------
# Run Server
# ------------------------------------
if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host=Config.HOST,
        port=Config.PORT,
        reload=Config.DEBUG
    )