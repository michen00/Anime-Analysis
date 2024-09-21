# src/io/save_data.py
import os
import json
import pandas as pd
import logging
import yaml


# Load config paths from settings.yml
def load_config():
    with open("./config/settings.yml", "r") as f:
        return yaml.safe_load(f)


config = load_config()
json_dir = config["paths"]["json_dir"]
csv_dir = config["paths"]["csv_dir"]


def save_json(data, filename):
    """
    Saves data as a JSON file.
    """
    filepath = os.path.join(json_dir, filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"Data saved as JSON: {filepath}")


def save_csv(df, filename):
    """
    Saves a DataFrame as a CSV file.
    """
    filepath = os.path.join(csv_dir, filename)
    df.to_csv(filepath, index=False)
    logging.info(f"Data saved as CSV: {filepath}")