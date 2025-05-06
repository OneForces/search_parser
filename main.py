import pandas as pd
from parser.search_google import get_google_results
from parser.yandex_parser import get_search_results_yandex
from datetime import datetime

def load_keywords() -> list[str]:
    url = "https://docs.google.com/spreadsheets/d/1o_zA2oyRCFDeyFBrpuvTvM0GaRutNJKkPM9Wmxbt8O0/export?format=csv&gid=1384320761"
    df = pd.read_csv(url, header=None)
    keywords = df[0].dropna().astype(str).str.strip().tolist()
    if keywords and keywords[0].lower() == "список":
        keywords = keywords[1:]
    return keywords

def main():
    print("📦 Модуль parser загружен.\n")
    keywords = load_keywords()

    results = []

    for keyword in keywords:
        print(f"\n🔍 Обрабатываем запрос: {keyword}")

        # Yandex
        yandex_domains = get_search_results_yandex(keyword)
        for i, domain in enumerate(yandex_domains):
            print(f"🔹 Yandex стр. {i}: {domain}")
            results.append({"Запрос": keyword, "Источник": "Yandex", "Домен": domain})

        # Google
        google_domains = get_google_results(keyword)
        for domain in google_domains:
            print(f"🔹 Google: {domain}")
            results.append({"Запрос": keyword, "Источник": "Google", "Домен": domain})

    # Выгрузка результатов
    df = pd.DataFrame(results)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    df.to_csv(f"results_{timestamp}.csv", index=False)
    df.to_html(f"results_{timestamp}.html", index=False)
    print(f"\n💾 Результаты сохранены: results_{timestamp}.csv / .html")

if __name__ == "__main__":
    main()
