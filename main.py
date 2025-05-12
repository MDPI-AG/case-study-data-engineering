from datetime import datetime

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
data = client.fetch_api_data()

# dump raw json response data to a file
now = datetime.now()
filename = now.strftime("%Y%m%d_%H%M%S") + "_data.json"
filepath = f"./data/raw/{filename}"
with open(filepath, "w") as f:
    import json
    json.dump(data, f, indent=4)

# head the data
import pandas as pd
try:
    df = pd.DataFrame.from_dict(data["message"]["items"])
    print(df.head())
except KeyError as e:
    logger.error(f"KeyError: {e}")
    logger.error("Data format may have changed. Please check the API response.")


# some ideas for todos:
#  - save the raw data from the API (loop a few pages)
#  - a pipeline to load the raw data, preprocess it, and dump it to a parquet file
#  - a pipeline in dbt to query the parquet file
#  - an orchestrator to run the pipelines
#  - Dockerize the python app
