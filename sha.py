import hashlib
import sys

# SHA-256
def sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# SHA-512
def sha512_hash(data: str) -> str:
    return hashlib.sha512(data.encode()).hexdigest()

def option1_loop(input_string: str, output_file: str):
    """Endlessly hash the input string with SHA-256."""
    with open(output_file, "w") as file:
        current_hash = input_string
        while True:
            current_hash = sha256_hash(current_hash)
            file.write(current_hash + "\n")
            file.flush()

def option2_loop(input_string: str, output_file: str):
    """Endlessly alternate between SHA-512 and SHA-256."""
    with open(output_file, "w") as file:
        current_hash = input_string
        while True:
            current_hash = sha512_hash(current_hash)
            current_hash = sha256_hash(current_hash)
            file.write(current_hash + "\n")
            file.flush()

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <option> <input_string>")
        print("Option 1: SHA-256 endlessly")
        print("Option 2: Alternate SHA-512 and SHA-256 endlessly")
        sys.exit(1)

    option = int(sys.argv[1])
    input_string = sys.argv[2]
    output_file = "infinitesha.txt"

    if option == 1:
        print("Running Option 1: SHA-256 endlessly")
        option1_loop(input_string, output_file)
    elif option == 2:
        print("Running Option 2: Alternate SHA-512 and SHA-256")
        option2_loop(input_string, output_file)
    else:
        print("Invalid option. Choose 1 or 2.")
        sys.exit(1)

if __name__ == "__main__":
    main()

