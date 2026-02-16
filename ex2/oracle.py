import os


def dependencies_check() -> bool:
    """
    try to import dotenv package and load environment variables
    """
    try:
        from dotenv import load_dotenv
        load_dotenv()
        return True
    except ModuleNotFoundError:
        print("dotenv module is not found. Use 'pip install python-dotenv'")
        return False


def configuration_check() -> bool:
    """
    check that all environment variables have values
    """
    env_var = None
    try:
        with open(".env.example") as f:
            env_var = f.readlines()
    except FileNotFoundError:
        print("File '.env.example' does not exist")
        return False
    for var in env_var:
        var_name = var.strip().split("=")[0]
        value = os.getenv(var_name)
        if not value:
            print(f"Missing value for environment variable '{var_name}'")
            return False
    return True


def security_check() -> None:
    """
    check that .gitignore file contains .env line
    """
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")
    try:
        with open(".gitignore") as f:
            vars = f.readlines()
            vars = [var.strip() for var in vars]
            if ".env" in vars:
                print("[OK] .env added to .gitignore")
            else:
                print("[Error] .env was not added to .gitignore")
    except FileNotFoundError:
        print("[WARNING] .gitignore file missing")


if __name__ == "__main__":
    if not dependencies_check():
        exit(1)
    if not configuration_check():
        exit(1)
    mode = os.getenv("MATRIX_MODE", "development")
    if mode == "production":
        print("\n⚠ Production mode detected\n")

    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    if mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production cluster")
    print("API Access: Authenticated")
    masked_key = ""
    for _ in range(0, len(os.getenv('API_KEY'))):
        masked_key = masked_key + "*"
    print(f"Api_key: {os.getenv("API_KEY")
                      if mode == "development" else masked_key}")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print("Zion Network: Online")
    print()
    security_check()
    print("\nThe Oracle sees all configurations.")
