#!/usr/bin/env python3
"""
Referee Agent Entry Point.
"""
import os
import json
import logging
from pathlib import Path
from q21_referee import RLGMRunner
from my_referee import MyRefereeAI

# Setup logging
logging.basicConfig(level=logging.INFO)

def main():
    # Load configuration
    config_path = Path("js/config.json")
    if not config_path.exists():
        print("Error: js/config.json not found. Run setup_config.py first.")
        return

    with open(config_path) as f:
        config = json.load(f)

    # Initialize and run the Referee
    print("Starting Referee Agent...")
    try:
        runner = RLGMRunner(config=config, ai=MyRefereeAI())
        runner.run()
    except Exception as e:
        print(f"Error running referee: {e}")
        raise

if __name__ == "__main__":
    main()
