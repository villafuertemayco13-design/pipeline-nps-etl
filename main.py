import pandas as pd
from src.transformacion import limpiar_datos

def ejecutar_pipeline():
    # EXTRACT: leer datos
    df = pd.read_csv(
    "data/raw/encuestas.csv",
    dtype={
        "Cliente": "int32",
        "NPS": "float32",
        "Operacion": "category"
    }
)

    # TRANSFORM: limpiar datos
    df_limpio = limpiar_datos(df)

    # LOAD: exportar a Parquet
    df_limpio.to_parquet(
        "data/processed/encuestas_limpias.parquet",
        index=False
    )

    print("Pipeline ETL ejecutado correctamente")
    print("Filas originales:", len(df))
    print("Filas procesadas:", len(df_limpio))

if __name__ == "__main__":
    ejecutar_pipeline()
