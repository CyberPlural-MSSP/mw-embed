from vendor import disitool
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        "embed.py",
        description="A malware embedder designed to create malware laden EXEs from a base EXE"
    )

    parser.add_argument("--payload", required=True, help="Path to the payload directory")
    parser.add_argument("--target", required=True, help="The target .exe file you want to attach the payload")

    args = parser.parse_args()
    print(args)

    
if __name__ == "__main__":
    main()