from src.utils.config import Config
from src.utils.logger import setup_logger

from src.data.data_extractor import DataExtractor

config = Config(config={
    "API_ENDPOINT": "https://api.crossref.org/works?sort=published&order=desc&rows=200",
    "LOG_FILE": "logs/app.log",
    "LOG_LEVEL": "INFO",
})

logger = setup_logger(
    name="data_loader",
    log_file=config.log_file,
    level=config.log_level,
)

# API client for CrossRef works api endpoint
client = DataExtractor(config, logger)
client.fetch_api_data()

# some ideas for todos:
#  - save the raw data from the API (loop a few pages)
#  - a pipeline to load the raw data, preprocess it, and dump it to a parquet file
#  - a pipeline in dbt to query the parquet file
#  - an orchestrator to run the pipelines
#  - Dockerize the python app
