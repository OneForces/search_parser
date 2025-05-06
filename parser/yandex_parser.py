import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urlparse


def normalize_domain(url: str) -> str | None:
    try:
        domain = urlparse(url).netloc.lower().replace("www.", "")
        if domain.endswith(".ru"):
            return domain
    except:
        return None
    return None


def get_search_results_yandex(query: str, region_code: int = 213, depth: int = 50) -> list:
    headers = {"User-Agent": UserAgent().random}
    domains = []

    for page in range(0, depth, 10):
        url = f"https://yandex.ru/search/?text={query}&lr={region_code}&p={page // 10}"
        print(f"🔹 Yandex стр. {page // 10}: {url}")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                print(f"⚠️ Ошибка ответа: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')

            tags = soup.select("a.link") or soup.select("a.serp-item__title-link")
            for tag in tags:
                href = tag.get("href")
                domain = normalize_domain(href)
                if domain and domain not in domains:
                    domains.append(domain)

            time.sleep(1)

        except Exception as e:
            print(f"❌ Ошибка при запросе: {e}")
            continue

    return domains
