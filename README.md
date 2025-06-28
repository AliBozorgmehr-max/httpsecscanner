# 🛡️ HTTP Security Headers Scanner

A Python-based tool to check for common HTTP security headers on websites.

Developed with 💻 by **Ali Bozorgmehr**

## 🎯 Features
- Supports scanning for 15+ security headers
- Categorization: Required, Recommended, Deprecated, Warning, etc.
- Security scoring based on headers present
- Output in plain text or JSON
- Batch scan support from a file of URLs

## 🛠️ Installation & Setup

### Clone the repository from GitHub:
```bash
git clone https://github.com/AliBozorgmehr-max/httpsecscanner.git
```
```bash
cd httpsecscanner
```

### Install required dependencies:
```bash
pip install -r requirements.txt
```


## 🚀 How to Use

### Simple Scan:
```bash
python main.py https://example.com
```

### Save Output to File:
```bash
python main.py https://example.com -o result.txt
```

### JSON Output:
```bash
python main.py https://example.com -j -o result.json
```

### Scan from File:
```bash
python main.py -f urls.txt -j -o full_report.json
```
