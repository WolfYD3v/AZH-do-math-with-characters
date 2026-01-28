#!/bin/bash

if [ -f .venv/bin/python ]; then
    .venv/bin/python main.py
else
    echo "Erreur: L'environnement virtuel (.venv) est introuvable."
fi
