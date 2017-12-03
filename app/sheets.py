#! /usr/bin/env python
import gspread
import logging
from oauth2client.service_account import ServiceAccountCredentials
import config
import datetime

# Depending on how this shapes up, a class for each person and their
#    number might be nice -- or dictionary

class SMS(object):
    from_num = ""
    to_num = ""
    text = ""

    def __init__(self, from_num, to_num, text):
        self.from_num = from_num
        self.to_num = to_num
        self.text = text

log = logging.getLogger('log')
logging.basicConfig(filename='sheets.log', level=logging.DEBUG)
# # When changing sheets, need to make sure to go and share this client.json email with the sheet you want to work on
def get_total():
    sheet = get_sheet(config.sheet_name)
    try:
        val = sheet.acell('E11').value
    except GSpreadException:
        return -1
    return val

def get_sheet(sheet_name):
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(config.client_file, scope)
    client = gspread.authorize(creds)
    try:
        sheet = client.open(sheet_name).sheet1
    except  gspread.exceptions.SpreadsheetNotFound:
        log.debug('Sheet "%s" not found' % sheet_name)
        return None
    else:
        return sheet

def input_message(sms, marker, sheet):
    print("Found marker at R%sC%s" % (marker.row, marker.col))
    # Split up message into the correct pieces and input
    msg_parts = sms.text.split(',')
    size = len(msg_parts)
    # TODO: Check if first chunk is an actual date
    if size is 2:
        current_date = datetime.datetime.today()
        day_str_item = [str(current_date.month) + '/' + str(current_date.day)]
        msg_parts = day_str_item + msg_parts
        print(msg_parts)
    elif size is 3:
        pass
    else:
        log.debug('Invalid message setup, has %s piece(s)' % str(size))
        log.debug('Cont: message was-> "%s"' % sms.text)
        return
    print(marker)
    sheet.update_cell(marker.row+1, marker.col, marker.value)
    for i in range(0,3):
        sheet.update_cell(marker.row, marker.col + i, msg_parts[i])

######### Main ###############################

# Change the return value here to indicate what http response to send
def handle_sms(sms):
    sheet = get_sheet(config.sheet_name)
    if ( sheet != None):
        try:
            marker = sheet.find(config.marker)
        # Dictionary of people and function for each person
        # Probably more efficient to just pass sheet or something
        except gspread.exceptions.CellNotFound:
            log.debug('Unable to find marker')
        else:
            # use PEOPLE to check incoming number
            # check values against sms.from_num
            input_message(sms, marker, sheet)
    else:
        log.debug('Sheet error,  message not input\n "%s"' % sms.text)
