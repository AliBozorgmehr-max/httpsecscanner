def scan_from_file(filepath):
    from .headers import scan_headers
    urls = []
    try:
        with open(filepath, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except Exception as e:
        return [{"url": filepath, "error": f"Failed to read file: {e}"}]

    return [scan_headers(url) for url in urls]