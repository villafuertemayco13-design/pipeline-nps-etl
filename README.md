# Pipeline ETL de Encuestas NPS

## Descripción
Proyecto desarrollado en Python para automatizar
la extracción, transformación y carga de encuestas NPS.

## Tecnologías
- Python
- Pandas
- PyArrow
- Parquet

## Estructura
- main.py: ejecuta el pipeline completo.
- src/transformacion.py: contiene la función de limpieza.
- data/raw/: almacena los datos originales.
- data/processed/: almacena los datos procesados.

## Etapas del pipeline

### 1. Extracción
Se leen las encuestas desde un archivo CSV utilizando Pandas.

### 2. Transformación
Se aplican las siguientes operaciones:
- Normalización de nombres de columnas.
- Eliminación de registros duplicados.
- Exclusión de registros sin calificación NPS.

Los registros sin NPS se excluyen porque imputar una
calificación podría distorsionar el indicador.

### 3. Carga
Se exportan los datos procesados a formato Parquet.

Parquet utiliza almacenamiento columnar y compresión,
lo que permite optimizar el espacio y la lectura de
columnas para análisis y procesos de Machine Learning.

## Instalación

pip install -r requirements.txt

## Ejecución

python main.py

## Resultado
El pipeline genera:
data/processed/encuestas_limpias.parquet

## Datos
Se utiliza un conjunto de datos ficticios para
fines educativos, sin información real de clientes.
