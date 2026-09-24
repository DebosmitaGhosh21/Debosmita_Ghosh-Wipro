
import json
from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Test data file
DATA_FILE = BASE_DIR / "test_data" / "test_data.json"

# Screenshot directory
SCREENSHOT_DIR = BASE_DIR / "screenshots"

# Output directory
OUTPUT_DIR = BASE_DIR / "outputs"


def load_test_data():
    """Load test data from JSON file."""
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)