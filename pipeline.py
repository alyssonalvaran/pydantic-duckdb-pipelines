"""
Main ingestion and transformation pipeline.
Orchestrates reading JSON, validating schemas, and loading into DuckDB.
"""
import json
import logging
from typing import List, Dict, Any
import duckdb
import pandas as pd
from pydantic import ValidationError

from models.events import UserSignupEvent

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def load_raw_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Reads raw JSON event data from a local file.
    
    Args:
        file_path: The local path to the JSON log file.
        
    Returns:
        A list of unstructured event dictionaries.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Could not find {file_path}. Please check the path.")
        return []


def validate_events(raw_events: List[Dict[str, Any]]) -> List[UserSignupEvent]:
    """
    Validates raw event dictionaries against the Pydantic schema.
    Isolates bad data and prevents it from reaching the database.
    
    Args:
        raw_events: List of unstructured event payloads.
        
    Returns:
        A list of strongly-typed, validated UserSignupEvent objects.
    """
    valid_events = []
    
    for event in raw_events:
        try:
            # Enforce schema and type casting
            validated_event = UserSignupEvent(**event)
            valid_events.append(validated_event)
        except ValidationError as e:
            logging.warning(f"Validation failed for event {event.get('event_id', 'UNKNOWN')}: {e.errors()[0]['msg']}")
            
    return valid_events


def load_to_duckdb(events: List[UserSignupEvent], db_path: str = ":memory:") -> duckdb.DuckDBPyConnection:
    """
    Loads validated events into a DuckDB database for querying.
    """
    conn = duckdb.connect(db_path)
    
    # Convert Pydantic models to a list of dicts
    raw_list = [event.model_dump() for event in events]
    
    if raw_list:
        # Convert the list of dicts to a Pandas DataFrame
        validated_data = pd.DataFrame(raw_list) 
        
        # DuckDB seamlessly reads the Pandas DataFrame 'validated_data' from the local scope
        conn.execute("CREATE TABLE signups AS SELECT * FROM validated_data")
        logging.info(f"Successfully loaded {len(validated_data)} records into DuckDB.")
    else:
        logging.warning("No valid data to load into DuckDB.")
        
    return conn


def main() -> None:
    """Executes the core pipeline workflow."""
    file_path = "data/raw_events.json"
    
    logging.info("Starting data pipeline...")
    raw_data = load_raw_data(file_path)
    
    logging.info(f"Loaded {len(raw_data)} raw events. Starting validation...")
    clean_events = validate_events(raw_data)
    
    logging.info("Loading validated events into DuckDB...")
    conn = load_to_duckdb(clean_events)
    
    # Run a test analytical query
    print("\n--- Analytics Sample: Signups by Plan Type ---")
    query_result = conn.execute(
        "SELECT plan_type, COUNT(*) as signup_count FROM signups GROUP BY plan_type ORDER BY signup_count DESC"
    ).fetchdf()
    
    print(query_result)


if __name__ == "__main__":
    main()
