import json

def generate_report(data, output_path=None, as_json=False, batch=False):
    if batch:
        print("\n🔎 Batch scan results:")
        for result in data:
            _print_result(result)
    else:
        _print_result(data)

    if output_path:
        with open(output_path, "w") as f:
            if as_json:
                json.dump(data, f, indent=2)
            else:
                for result in (data if batch else [data]):
                    f.write(_text_report(result))
                    f.write("\n\n" + ("=" * 60) + "\n\n")
        print(f"\n📄 Report saved to: {output_path}")

def _print_result(data):
    if "error" in data:
        print(f"❌ {data['url']}: {data['error']}")
        return

    print(f"\n🔍 {data['url']} | Status: {data['status_code']}")
    for h, meta in data['headers'].items():
        mark = "✔️" if meta['value'] else "❌"
        level_tag = f"({meta['level']})"
        print(f"  {mark} {h} {level_tag}")
    print(f"🔒 Score: {data['score']}/{data['total']}")

def _text_report(data):
    if "error" in data:
        return f"URL: {data['url']}\nError: {data['error']}"
    lines = [f"URL: {data['url']}", f"Status Code: {data['status_code']}", ""]
    for h, meta in data['headers'].items():
        status = "Found" if meta['value'] else "Missing"
        lines.append(f"{h} ({meta['level']}): {status}")
    lines.append(f"\nScore: {data['score']}/{data['total']}")
    return "\n".join(lines)