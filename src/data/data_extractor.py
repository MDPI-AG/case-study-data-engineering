import os
import requests
from logging import Logger
from requests.exceptions import HTTPError
from tqdm import tqdm

from src.utils.config import Config

class DataExtractor:
    """
    DataLoader class for loading data from CrossRef API.

    Attributes:
        config (Config): Configuration object containing API endpoint and key.
        headers (Dict[str, str]): Headers for the API request.
    """

    def __init__(self, config: Config, logger: Logger):
        self.config = config
        self.headers = {
            "Accept": "application/json",
        }

        self.logger = logger
        self.logger.info("DataLoader initialized with config: %s", config.__dict__)
        self.logger.info("Headers set for API request: %s", self.headers)
        self.logger.info("DataLoader initialized successfully.")

    # todo - function to fetch data from CrossRef API by looping through the pages
    def fetch_api_data(self) -> dict:
        self.logger.info("Fetching data from CrossRef API...")
        self.logger.error("to be implemented...")
