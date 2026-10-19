
from datetime import datetime


def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("Log data must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename
