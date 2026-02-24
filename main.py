import argparse
from password_guard.checker import check_password
from password_guard.generator import generate_password

def main():
    parser = argparse.ArgumentParser(description="Password Guard CLI")
    parser.add_argument("--check", type=str, help="Check password strength")
    parser.add_argument("--generate", action="store_true", help="Generate password")
    parser.add_argument("--length", type=int, default=16, help="Generated password length")
    args = parser.parse_args()

    if args.check:
        result = check_password(args.check)
        print("Password Analysis:")
        for key, value in result.items():
            print(f"{key}: {value}")
    elif args.generate:
        password = generate_password(args.length)
        print(f"Generated password: {password}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()