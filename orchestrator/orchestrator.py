import logging
from fastapi import FastAPI
import requests

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# URLs des agents
pattern_agent_url = "http://127.0.0.1:8001/detect-patterns"
metrics_agent_url = "http://127.0.0.1:8002/analyze-metrics"
risk_agent_url = "http://127.0.0.1:8003/analyze-risks"

@app.post("/analyze")
async def analyze_depot(depot_git_url: str):
    logger.debug(f"Received Git URL: {depot_git_url}")  # Remplace print par logging

    try:
        # Appels aux agents
        pattern_response = requests.post(pattern_agent_url, json={"depot_git_url": depot_git_url})
        metrics_response = requests.post(metrics_agent_url, json={"depot_git_url": depot_git_url})
        risk_response = requests.post(risk_agent_url, json={"depot_git_url": depot_git_url})

        # Débogage des réponses
        logger.debug(f"Pattern Agent response: {pattern_response.status_code}")
        logger.debug(f"Metrics Agent response: {metrics_response.status_code}")
        logger.debug(f"Risk Agent response: {risk_response.status_code}")

        # Vérification des réponses des agents
        if pattern_response.status_code != 200:
            return {"error": f"Pattern agent returned an error: {pattern_response.status_code}"}
        if metrics_response.status_code != 200:
            return {"error": f"Metrics agent returned an error: {metrics_response.status_code}"}
        if risk_response.status_code != 200:
            return {"error": f"Risk agent returned an error: {risk_response.status_code}"}

        # Rassembler et retourner les résultats
        results = {
            "patterns": pattern_response.json(),
            "metrics": metrics_response.json(),
            "risks": risk_response.json()
        }
        return results

    except requests.exceptions.RequestException as e:
        logger.error(f"Error while making requests: {str(e)}")  # Remplace print par logging
        return {"error": f"An error occurred while making requests: {str(e)}"}
