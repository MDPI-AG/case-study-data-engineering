from typing import Dict

class Config:
    """
    Configuration class for the application.

    Attributes:
        api_endpoint (str): API endpoint for CrossRef.
        log_file (str): Path to the log file.
        log_level (str): Logging level.
    """

    def __init__(self, config: Dict[str, str]):
        self.api_endpoint = config.get("API_ENDPOINT", "")
        self.log_file = config.get("LOG_FILE", "app.log")
        self.log_level = config.get("LOG_LEVEL", "INFO").upper()
        self.__validate_config()

    def __validate_config(self):
        """
        Validate the configuration values.
        Raises:
            ValueError: If any required configuration is missing or invalid.
        """
        if not self.api_endpoint:
            raise ValueError("API_ENDPOINT is required.")
        if not self.log_file:
            raise ValueError("LOG_FILE is required.")
        if self.log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            raise ValueError("LOG_LEVEL must be one of DEBUG, INFO, WARNING, ERROR, CRITICAL.")
