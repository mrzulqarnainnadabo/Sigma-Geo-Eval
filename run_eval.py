"""Run the SIGMA-GEO reference pipeline check."""
import argparse
import json
from sigma_geo.runner import run

def main() -> None:
    parser = argparse.ArgumentParser(description="SIGMA-GEO benchmark scaffold")
    parser.add_argument("--adapter", choices=["reference"], default="reference")
    parser.parse_args()
    print(json.dumps(run(), indent=2))
    print("\nNOTE: Reference pipeline checks are not AI model performance results.")

if __name__ == "__main__":
    main()
