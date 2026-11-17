
from pathlib import Path
import pandas as pd
from src.transformacion import limpiar_datos


def ejecutar_pipeline():

    # 1. EXTRACCIÓN
    print("Iniciando extracción de datos...")

    df = pd.read_csv(
        "data/raw/encuestas.csv",
        dtype={
            "Cliente": "int32",
            "NPS": "float32",
            "Operacion": "category"
        }
    )

    print(f"Registros originales: {len(df)}")

    # 2. TRANSFORMACIÓN
    print("Limpiando datos...")

    df_limpio = limpiar_datos(df)

    print(f"Registros procesados: {len(df_limpio)}")

    # 3. CARGA
    print("Exportando archivo Parquet...")

    ruta_salida = Path("data/processed")
    ruta_salida.mkdir(parents=True, exist_ok=True)

    df_limpio.to_parquet(
        ruta_salida / "encuestas_limpias.parquet",
        engine="pyarrow",
        index=False
    )

    print("¡Pipeline ETL ejecutado correctamente!")


if __name__ == "__main__":
    ejecutar_pipeline()
