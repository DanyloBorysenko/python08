import sys
import os
import site


def outside_env_info() -> None:
    """
    prints instructions to activate venv
    """
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate   # On Windows")
    print("Then run this program again.")


def inside_env_info() -> None:
    """
    prints info about current venv
    """
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("\nPackage installation path:")
    for path in site.getsitepackages():
        print(path)


def main():
    # 'prefix' shows current path to the environment
    # 'base_prefix' shows default path to the environment
    # activation of venv is changing 'prefix'
    if sys.prefix == sys.base_prefix:
        outside_env_info()
    else:
        inside_env_info()


if __name__ == "__main__":
    main()
