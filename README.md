# Analyseur Multi-Agents

Ce projet est une application en ligne de commande qui permet d'analyser un dépôt Git distant grâce à des agents spécialisés orchestrés avec LangChain.

---

## Fonctionnalités

- Analyse d’un dépôt Git via URL (saisie en ligne de commande)
- Orchestration des appels agents via LangChain
- Réponse simulée des agents (résultats statiques pour le moment)
- Communication en ligne de commande uniquement

---

## Installation

### 1. Cloner le projet

```bash
git clone git@github.com:meliouar16/multi_agent.git
cd multi_agent
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Exécution

Lancer l’application :

```bash
python cli.py
```

Puis entrer une URL de dépôt Git à analyser, par exemple :

```
https://github.com/octocat/Hello-World.git
```

> Pour l’instant, les résultats sont simulés avec des réponses statiques dans les agents.

---

## Structure du projet

```
multi_agent/
├── cli.py                 # Lancement de l'analyse en CLI
├── agents/                # Agents spécialisés
├── orchestrator/          # Orchestrateur LangChain
└── requirements.txt       # Dépendances du projet
```

---

## Licence

Projet pédagogique développé à des fins d’apprentissage.
