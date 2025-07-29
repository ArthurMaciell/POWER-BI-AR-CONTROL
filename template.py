import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "rdstation_api"

list_of_files = [
    f"{project_name}/app/__init__.py",
    f"{project_name}/app/main.py",
    f"{project_name}/app/config/__init__.py",
    f"{project_name}/app/config/settings.py",
    f"{project_name}/app/routes/__init__.py",
    f"{project_name}/app/routes/leads.py",           # pode deixar vazio para uso futuro
    f"{project_name}/app/routes/negociacoes.py",
    f"{project_name}/app/services/__init__.py",
    f"{project_name}/app/services/negociacoes.py",
    f"{project_name}/.env",
    f"{project_name}/requirements.txt",
    f"{project_name}/README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Criando pasta: {filedir}")

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Criando arquivo vazio: {filepath}")
    else:
        logging.info(f"{filepath} já existe.")
