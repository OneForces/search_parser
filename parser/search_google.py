import requests
from urllib.parse import urlparse
import time

API_KEY = "AIzaSyCvDkqxy8P0yLUh44whYN8jObQEojm9ne4"
CX = "40484ab3ef2384cb5"

def normalize_domain(url: str) -> str | None:
    try:
        domain = urlparse(url).netloc.lower().replace("www.", "")
        if domain.endswith(".ru"):
            return domain
    except:
        pass
    return None

def get_google_results(query: str, depth: int = 50) -> list:
    print(f"🔍 Google API: {query}")
    try:
        domains = []
        start = 1
        for _ in range(0, depth, 10):
            params = {
                "key": API_KEY,
                "cx": CX,
                "q": query,
                "start": start,
                "num": 10,
                "hl": "ru",
                "gl": "ru",
                "lr": "lang_ru"
            }
            resp = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
            if resp.status_code != 200:
                print(f"❌ Ошибка Google API: {resp.status_code} — {resp.text}")
                break

            data = resp.json()
            for item in data.get("items", []):
                link = item.get("link")
                domain = normalize_domain(link)
                if domain and domain not in domains:
                    domains.append(domain)

            start += 10
            time.sleep(1)

        return domains

    except Exception as e:
        print(f"❌ Ошибка Google API: {e}")
        return []