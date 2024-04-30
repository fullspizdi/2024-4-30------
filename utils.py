import json
import logging

def load_config(file_path='config.json'):
    """
    Load the configuration from a JSON file.
    
    Args:
        file_path (str): The path to the configuration file.
    
    Returns:
        dict: The configuration dictionary.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        logging.info("Configuration loaded successfully.")
        return config
    except FileNotFoundError:
        logging.error(f"Configuration file {file_path} not found.")
        raise
    except json.JSONDecodeError:
        logging.error("Error decoding the configuration file.")
        raise

def log_setup():
    """
    Setup basic configuration for logging.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

