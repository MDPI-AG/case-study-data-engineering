# Case Study: Data Engineering

## Getting Started

Install the required packages using pip. It is recommended to use a virtual environment t
avoid conflicts with other projects.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Project Structure

```plaintext
.
├── data
│   ├── processed
│   └── raw
├── dbt
│   ├── models
│   │   ├── staging
│   │   └── marts
│   ├── seeds
│   └── snapshots
├── src
│   ├── data
│   │   ├── __init__.py
│   │   ├── data_extractor.py
│   │   └── data_preprocessor.py
│   ├── utils
│       ├── __init__.py
│       ├── config.py
│       └── logger.py
├── requirements.txt
├── README.md
└── main.py
```

## Some Ideas for Todos

- save the raw data from the API (loop a few pages)
- a pipeline to load the raw data, preprocess it (e.g., deduplicate items), and dump it to a parquet file
- a pipeline in dbt to query the parquet file
- an orchestrator to run the pipelines
- Dockerize the python app
