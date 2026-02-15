import os


def dependencies_check() -> bool:
    try:
        from dotenv import load_dotenv
        return True
    except ModuleNotFoundError:
        print("dotenv module is not found. Use 'pip install python-dotenv'")
        return False


if __name__ == "__main__":
    if not dependencies_check():
        exit(1)
    from dotenv import load_dotenv
    load_dotenv()
    db_url = os.environ["DATABASE_URL"]
    print(db_url)
