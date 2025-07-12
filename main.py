from fastapi import FastAPI, UploadFile, File
import requests

@app.post("/summarize")
async def summarize_file(file: UploadFile = File(...)):
    contents = await file.read()
    text = contents.decode("utf-8")

    # Send to local Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "11AMA2",
            "prompt": f"Summarize the following text:\n\n{text}",
            "stream": False
        }
    )

    summary = response.json().get("response", "No summary generated.")
    return {"filename": file.filename, "summary": summary}

