from fastapi import FastAPI
import time

app = FastAPI()

@app.post("/detect-patterns")
async def detect_patterns(data: dict):
    """
    Analyse le dépôt Git et détecte les patterns de conception.
    """
    print(f"Analyzing Git repo: {data['depot_git_url']}")
    time.sleep(2)  # Simule une analyse

    # Résultats simulés
    return {"patterns_found": ["Singleton", "Factory Method", "Observer"]}
