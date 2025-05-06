import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_keywords_from_sheet(sheet_url: str, worksheet_name: str = None) -> list:
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials/credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(sheet_url)
    worksheet = sheet.get_worksheet(0) if worksheet_name is None else sheet.worksheet(worksheet_name)
    keywords = worksheet.col_values(1)
    return [kw.strip() for kw in keywords if kw.strip()]
