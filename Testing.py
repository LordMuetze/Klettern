import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)
TabellenListe = ["FinaleMannlich9","FinaleWeiblich9"]


TabellenBlatt = client.open("FinaleMannlich9").sheet1
wert = TabellenBlatt.cell(1,2).value
print(wert)