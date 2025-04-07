from fastapi import FastAPI
import time

app = FastAPI()

@app.post("/analyze-risks")
async def analyze_risks(data: dict):
    """
    Recherche les risques dans le code (erreurs potentielles, vulnérabilités, etc.).
    """
    print(f"Analyzing Git repo: {data['depot_git_url']}")
    time.sleep(2)  # Simule une analyse

    # Résultats simulés
    return {"risks_found": ["Duplicated Code", "Hardcoded Credentials"]}
