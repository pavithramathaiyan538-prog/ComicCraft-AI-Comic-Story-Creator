from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Pydantic model for JSON payload validation
class PromptRequest(BaseModel):
    story_prompt: str
    character_name: str
    setting: str
    story_tone: str
    art_style: str

# Dummy AI backend function placeholders
def generate_outline(prompt): return {}
def generate_story(prompt): return "Once upon a time..."
def generate_image(prompt): return "image_path.jpg"
def build_comic_layout(data): return {}
def save_pdf(data): return "comic.pdf"

# 1. Homepage Route
@app.get("/", response_class=HTMLResponse)
async def homepage():
    return "<h1>Welcome to ComicCraft</h1>"

# 2. Form Submission Route
@app.post("/generate")
async def generate_comic_form(
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    story_tone: str = Form(...),
    art_style: str = Form(...)
):
    try:
        story = generate_story(story_prompt)
        image = generate_image(story_prompt)
        return {"status": "success", "story": story, "image": image}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. JSON Payload API Route
@app.post("/generate-comic/json")
async def generate_comic_json(payload: PromptRequest):
    try:
        outline = generate_outline(payload.story_prompt)
        story = generate_story(payload.story_prompt)
        image = generate_image(payload.story_prompt)
        layout = build_comic_layout({"story": story, "image": image})
        pdf_path = save_pdf(layout)
        
        return {
            "status": "success",
            "layout_data": layout,
            "pdf_path": pdf_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 4. Report Success Route
@app.get("/report-success")
async def report_success():
    return {"message": "Comic downloaded successfully!"}

# 5. Developer Test Route for Image Generation
@app.get("/test-image")
async def test_image():
    try:
        img = generate_image("Test Prompt")
        return {"status": "success", "image_path": img}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
