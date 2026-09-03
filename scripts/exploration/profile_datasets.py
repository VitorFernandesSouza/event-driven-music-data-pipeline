from pathlib import Path

import pandas as pd


# Diretórios do projeto
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def format_size(size_bytes: int) -> str:
    """Converte bytes para uma representação legível."""
    size_mb = size_bytes / (1024 * 1024)
    return f"{size_mb:.2f} MB"


def profile_dataset(file_path: Path) -> None:
    """Exibe informações de profiling de um arquivo CSV."""

    print("\n" + "=" * 100)
    print(f"ARQUIVO: {file_path.name}")
    print("=" * 100)

    print(f"Fonte: {file_path.parent.relative_to(RAW_DATA_DIR)}")
    print(f"Tamanho: {format_size(file_path.stat().st_size)}")

    try:
        df = pd.read_csv(file_path)
    except Exception as exc:
        print(f"\nERRO AO LER O ARQUIVO: {exc}")
        return

    # Informações gerais
    print("\n--- DIMENSÕES ---")
    print(f"Linhas: {len(df):,}")
    print(f"Colunas: {len(df.columns):,}")

    # Colunas
    print("\n--- COLUNAS ---")
    for column in df.columns:
        print(f"- {column}")

    # Tipos
    print("\n--- TIPOS DE DADOS ---")
    print(df.dtypes.to_string())

    # Valores nulos
    print("\n--- VALORES NULOS ---")
    nulls = df.isnull().sum()

    nulls = nulls[nulls > 0]

    if nulls.empty:
        print("Nenhum valor nulo encontrado.")
    else:
        for column, count in nulls.items():
            percentage = (count / len(df)) * 100
            print(f"- {column}: {count:,} ({percentage:.2f}%)")

    # Duplicidades
    print("\n--- DUPLICIDADES ---")
    duplicated_rows = df.duplicated().sum()

    print(f"Linhas duplicadas: {duplicated_rows:,}")

    # Valores únicos
    print("\n--- CARDINALIDADE ---")

    cardinality = pd.DataFrame(
        {
            "unique_values": df.nunique(dropna=True),
            "null_values": df.isnull().sum(),
        }
    )

    print(cardinality.to_string())

    # Estatísticas numéricas
    numeric_columns = df.select_dtypes(include="number").columns

    print("\n--- ESTATÍSTICAS NUMÉRICAS ---")

    if len(numeric_columns) == 0:
        print("Nenhuma coluna numérica encontrada.")
    else:
        statistics = df[numeric_columns].describe().T

        statistics = statistics[
            ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
        ]

        print(statistics.to_string())

    # Amostra
    print("\n--- AMOSTRA ---")
    print(df.head(5).to_string(index=False))


def main() -> None:
    """Executa o profiling de todos os CSVs encontrados em data/raw."""

    if not RAW_DATA_DIR.exists():
        print(f"Diretório não encontrado: {RAW_DATA_DIR}")
        return

    csv_files = sorted(RAW_DATA_DIR.rglob("*.csv"))

    if not csv_files:
        print(f"Nenhum arquivo CSV encontrado em: {RAW_DATA_DIR}")
        return

    print("=" * 100)
    print("DATA PROFILING")
    print("=" * 100)
    print(f"Diretório analisado: {RAW_DATA_DIR}")
    print(f"Arquivos encontrados: {len(csv_files)}")

    for file_path in csv_files:
        profile_dataset(file_path)

    print("\n" + "=" * 100)
    print("PROFILING FINALIZADO")
    print("=" * 100)


if __name__ == "__main__":
    main()