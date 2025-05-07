# 🔍 Поисковый парсер Google + Yandex

Проект предназначен для извлечения `.ru`-доменов из результатов поиска **Google** и **Yandex** по ключевым словам из Google Sheets.

---

## 📁 Содержание

- [🚀 Установка](#-установка)
- [📊 Источник ключевых слов](#-источник-ключевых-слов)
- [🔧 Настройка Google API](#-настройка-google-api)
- [💻 Запуск](#-запуск)
- [📦 Зависимости](#-зависимости)
- [📈 Ограничения и квоты](#-ограничения-и-квоты)
- [📚 Примеры](#-примеры)

---

## 🚀 Установка

1. Клонируй/скачай проект. git clone repo
2. Установи зависимости:

```bash
pip install -r requirements.txt
```

---

## 📊 Источник ключевых слов

По умолчанию используется Google Sheets:
```
https://docs.google.com/spreadsheets/d/ID/edit#gid=GID
```

**ВАЖНО**: Документ должен быть доступен публично по ссылке (`Просмотр по ссылке`).

### Как получить ссылку CSV:

1. Зайди в нужный лист Google Таблиц.
2. Замените в URL:
   ```
   /edit#gid=1384320761
   ⟶
   /export?format=csv&gid=1384320761
   ```

3. Вставь её в `main.py`:

```python
url = "https://docs.google.com/spreadsheets/d/ID/export?format=csv&gid=GID"
```

---

## 🔧 Настройка Google API

### 1. Перейди в Google Cloud Console:
👉 https://console.cloud.google.com/

### 2. Создай проект (если ещё нет)

### 3. Включи API:
- Зайди сюда:  
  👉 https://console.developers.google.com/apis/api/customsearch.googleapis.com/overview  
- Выбери свой проект.
- Нажми **"Включить"**.

### 4. Создай API ключ:

1. В Google Console открой: `APIs & Services > Credentials`
2. Нажми `+ Create Credentials > API Key`
3. Скопируй `API_KEY`

### 5. Создай Поисковую систему (CX):

1. Перейди на:  
   👉 https://programmablesearchengine.google.com/all
2. Нажми "Добавить"
3. Укажи `*.ru` в поле "Сайты для поиска"
4. Нажми "Создать"
5. Перейди в "Панель управления" > "ID поисковой системы" (это и есть **CX**)

---

## 💻 Запуск

```bash
python main.py
```

---

## 📦 Зависимости

---
Важно. 
В таблице нужно добавить mail аккаунт из credentials.json "client_email": "profi-641@resolute-bloom-459017-h8.iam.gserviceaccount.com", здесь он - profi-641@resolute-bloom-459017-h8.iam.gserviceaccount.com , далее дать доступ к таблице как аккаунту gmail. Сделать доступ по ссылке всем с разрешением на чтение.
---

Всё перечислено в `requirements.txt`. Основные:

```txt
gspread
oauth2client
requests
beautifulsoup4
fake-useragent
pandas
selenium
webdriver-manager
openpyxl
```


---

## 📚 Примеры

**main.py** извлекает ключевые слова из Google Sheets и запускает поиск:

```python
keywords = load_keywords()
for keyword in keywords:
    yandex_domains = get_search_results_yandex(keyword)
    google_domains = get_google_results(keyword)
```

---

## 🧠 Поддержка

Если при запуске:
- Ошибка `403` — значит API не включён или ключ не подходит к проекту
- Ошибка `429` — квота на день исчерпана
