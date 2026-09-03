# Arquitetura Medalhão

O projeto utiliza uma organização local em camadas:

```text
Fonte de dados
	↓
Ingestion
	↓
data/bronze
	↓
Processing
	↓
data/silver
	↓
Processing / Python
	↓
data/gold
	↓
Power BI
```

## Camadas

- **Bronze:** preserva os arquivos recebidos, sem transformações de negócio.
- **Silver:** receberá dados tratados, padronizados e validados.
- **Gold:** receberá datasets preparados para análises e indicadores.

O armazenamento e o processamento são locais nesta etapa. AWS, Snowflake e outros serviços pagos não fazem parte do projeto atual.
