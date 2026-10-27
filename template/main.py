import os

from dotenv import load_dotenv

load_dotenv()  # reads variables from .env and sets them in os.environ


def greet(name: str) -> str:
    return f"{os.getenv('GREETING', 'Hello')}, {name}!"


def main() -> None:
    print(greet("world"))


if __name__ == "__main__":
    main()
