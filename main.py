import argparse
from scanner.headers import scan_headers
from scanner.report import generate_report
from scanner.batch import scan_from_file

def main():
    parser = argparse.ArgumentParser(description="🛡️ HTTP Security Headers Scanner")
    parser.add_argument("url", nargs="?", help="Target URL to scan")
    parser.add_argument("-f", "--file", help="Scan multiple URLs from a file")
    parser.add_argument("-o", "--output", help="Path to save the report")
    parser.add_argument("-j", "--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    if args.file:
        results = scan_from_file(args.file)
        generate_report(results, output_path=args.output, as_json=args.json, batch=True)
    elif args.url:
        result = scan_headers(args.url)
        generate_report(result, output_path=args.output, as_json=args.json)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()