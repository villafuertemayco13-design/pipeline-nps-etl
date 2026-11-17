import pandas as pd

def limpiar_datos(df):
    df = df.copy()

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.drop_duplicates()
    df = df.dropna(subset=["nps"])

    return df
