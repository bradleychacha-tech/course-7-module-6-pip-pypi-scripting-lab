
import requests
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


def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    try:
        post = fetch_data()

        log_data = [
            f"Post ID: {post['id']}",
            f"Title: {post['title']}",
            f"Body: {post['body']}"
        ]

        filename = generate_log(log_data)
        print(f"Log written to {filename}")

    except requests.RequestException as error:
        print(f"Could not fetch data: {error}")


if __name__ == "__main__":
    main()
