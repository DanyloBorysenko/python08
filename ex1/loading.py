import sys
from typing import Dict, Optional


def dependencies_checker() -> Dict[str, Optional[str]]:
    print("Checking dependencies:")
    dependencies = {}
    try:
        import pandas
        dependencies["pandas"] = pandas.__version__
    except ModuleNotFoundError:
        dependencies["pandas"] = None
    try:
        import numpy
        dependencies["numpy"] = numpy.__version__
    except ModuleNotFoundError:
        dependencies["numpy"] = None
    try:
        import requests
        dependencies["requests"] = requests.__version__
    except ModuleNotFoundError:
        dependencies["requests"] = None
    try:
        import matplotlib
        dependencies["matplotlib"] = matplotlib.__version__
    except ModuleNotFoundError:
        dependencies["matplotlib"] = None
    return dependencies


def process_data() -> None:
    print("\nAnalyzing Matrix data...")

    # requests
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    print(f"Processing {len(data)} data rows...")

    # pandas
    import pandas
    df = pandas.DataFrame(data)
    df["title_len"] = df["title"].apply(len)

    # numpy
    import numpy
    avg_title_len = numpy.mean(df["title_len"])
    print(f"Average title length is {avg_title_len}")

    # matplotlib
    import matplotlib.pyplot as plt
    print("Generating visualization..")
    plt.figure()
    plt.bar(df["id"], df["title_len"])
    plt.xlabel("ID")
    plt.ylabel("Title Length")
    plt.title("Title Length by Post ID")
    plt.show()


def main():
    print("LOADING STATUS: Loading programs...")
    dependencies_info = dependencies_checker()
    for module, version in dependencies_info.items():
        if version:
            print(f"[OK] {module} ({version}) - is ready")
        else:
            print(f"[ERROR] {module} - not installed")
    if None in list(dependencies_info.values()):
        print("\nInstall missing dependencies using:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    process_data()


if __name__ == "__main__":
    print("Python executable:", sys.executable)
    print("Virtual environment prefix:", sys.prefix)
    main()
