import gspread as gs
import os

# GSheets credentials dict
credentials = {
  "type": os.environ['GAPI_TYPE'],
  "project_id": os.environ['PROJECT_ID'],
  "private_key_id": os.environ['PRIVATE_KEY_ID'],
  "private_key": os.environ['PRIVATE_KEY'].replace(r'\n', '\n'),
  "client_email": os.environ['CLIENT_EMAIL'],
  "client_id": os.environ['CLIENT_ID'],
  "auth_uri": os.environ['AUTH_URI'],
  "token_uri": os.environ['TOKEN_URI'],
  "auth_provider_x509_cert_url": os.environ['AUTH_CERT_URL'],
  "client_x509_cert_url": os.environ['CLIENT_CERT_URL']
}

all_sheets = gs.service_account_from_dict(credentials)
ph_equity_sh = all_sheets.open("PH Equity Data")

def get_worksheet(worksheet_name):
  return ph_equity_sh.worksheet(worksheet_name)

def get_ws_col_vals(worksheet_name, col_val):
  return ph_equity_sh.worksheet(worksheet_name).col_values(col_val)

def get_first_empty_cell(worksheet_name):
  # total_rows returns the number of rows INCLUDING the col header
  # We want to know where the very first empty cell starts
  total_rows = str(len(worksheet_name.col_values(1)) + 1)
  return total_rows

def update_sheet(worksheet_name, data):
  worksheet_to_update = get_worksheet(worksheet_name)
  worksheet_to_update.add_rows(1)
  worksheet_to_update.update("A" + get_first_empty_cell(worksheet_to_update), data)

