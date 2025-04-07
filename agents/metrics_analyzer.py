from fastapi import FastAPI
import time

app = FastAPI()

@app.post("/analyze-metrics")
async def analyze_metrics(data: dict):
    """
    Analyse les métriques du code (complexité cyclomatique, etc.).
    """
    print(f"Analyzing Git repo: {data['depot_git_url']}")
    time.sleep(2)  # Simule une analyse

    # Résultats simulés
    return {"complexity": 120, "lines_of_code": 3500}
