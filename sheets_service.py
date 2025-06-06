import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

def connect_to_sheet():
    creds_dict = st.secrets["gcp_service_account"]
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open(creds_dict["sheet_name"]).sheet1
    return sheet
