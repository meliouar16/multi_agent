import requests

def main():
    # Demander à l'utilisateur l'URL du dépôt Git à analyser
    depot_git_url = input("Entrez l'URL du dépôt Git à analyser : ")

    # Construire l'URL avec le paramètre de requête
    orchestrator_url = f"http://127.0.0.1:8000/analyze?depot_git_url={depot_git_url}"

    # Faire la requête à l'orchestrateur (l'URL doit correspondre à l'adresse de l'orchestrateur)
    response = requests.post(orchestrator_url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        print("Résultats de l'analyse :")
        print(response.json())
    else:
        print(f"Erreur lors de l'appel à l'orchestrateur.")
        print(f"Code de statut : {response.status_code}")
        print(f"Message d'erreur : {response.text}")

if __name__ == "__main__":
    main()
