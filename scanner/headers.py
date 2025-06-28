import requests


SECURITY_HEADERS = {
    "Content-Security-Policy": "required",
    "Strict-Transport-Security": "required",
    "X-Content-Type-Options": "required",
    "X-Frame-Options": "required",
    "Referrer-Policy": "recommended",
    "Permissions-Policy": "recommended",
    "Cross-Origin-Opener-Policy": "advanced",
    "Cross-Origin-Embedder-Policy": "advanced",
    "Cross-Origin-Resource-Policy": "advanced",
    "X-DNS-Prefetch-Control": "optional",
    "X-Permitted-Cross-Domain-Policies": "optional",
    "Expect-CT": "recommended",
    "Cache-Control": "required",
    "Pragma": "recommended",
    "Access-Control-Allow-Origin": "warning",
    "Clear-Site-Data": "recommended",
    "Report-To": "recommended",
    "NEL": "recommended",
    "Public-Key-Pins": "deprecated",
    "Server": "warning",
    "X-Powered-By": "warning",
    "Timing-Allow-Origin": "optional",
}

def scan_headers(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        result = {
            "url": url,
            "status_code": response.status_code,
            "headers": {},
            "score": 0,
            "total": sum(1 for k, v in SECURITY_HEADERS.items() if v in ["required", "recommended"]),
        }

        for header, level in SECURITY_HEADERS.items():
            value = headers.get(header)
            result["headers"][header] = {
                "value": value,
                "status": "found" if value else "missing",
                "level": level
            }
            if level in ["required", "recommended"] and value:
                result["score"] += 1

        return result

    except requests.RequestException as e:
        return {"url": url, "error": str(e)}