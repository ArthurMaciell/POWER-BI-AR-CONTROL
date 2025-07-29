import requests
import pandas as pd
from datetime import datetime, timezone
import ast
from app.config.settings import RDSTATION_TOKEN

def get_negociacoes():
    page = 1
    start_date = "2025-01-01"
    end_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    df_total = pd.DataFrame()

    while True:
        url = (
            f"https://crm.rdstation.com/api/v1/deals?page={page}"
            f"&limit=200&created_at_period=true&start_date={start_date}"
            f"T08%3A00%3A00&end_date={end_date}"
            f"T18%3A00%3A00&token={RDSTATION_TOKEN}"
        )

        response = requests.get(url, headers={"accept": "application/json"})

        if response.status_code != 200:
            break

        dados = response.json()
        negociacoes = dados.get("deals", [])

        if not negociacoes:
            break

        df_pagina = pd.json_normalize(negociacoes)
        df_total = pd.concat([df_total, df_pagina], ignore_index=True)
        page += 1

    if df_total.empty:
        return []

    def parse_custom_fields(s):
        if isinstance(s, str):
            try:
                return ast.literal_eval(s)
            except:
                return []
        elif isinstance(s, list):
            return s
        else:
            return []

    def expandir_campos(campos):
        resultado = {}
        for campo in campos:
            cf = campo.get("custom_field", {})
            label = cf.get("label")
            if label:
                resultado[label] = campo.get("value")
        return resultado

    df_total["deal_custom_fields"] = df_total["deal_custom_fields"].apply(parse_custom_fields)
    df_custom = df_total["deal_custom_fields"].apply(expandir_campos).apply(pd.Series)
    df_final = pd.concat([df_total, df_custom], axis=1)

    return df_final.fillna("").to_dict(orient="records")
