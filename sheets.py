#! /usr/bin/env python
import gspread
import logging
from oauth2client.service_account import ServiceAccountCredentials
from server import SMS

# NEED BETTER WAY FOR DEFINE TYPE THINGS
KEVIN = '17153387410'
####### HOW DOE WE LOG STUFF THAT ISNT PRINT############
# log = logging.getLogger('log')
# logging.basicConfig()
# log.setLevel(logging.DEBUG)
# # When changing sheets, need to make sure to go and share this client.json email with the sheet you want to work on
# scope = ['https://spreadsheets.google.com/feeds']
# creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)
# client = gspread.authorize(creds)
# 
# sheet = client.open("Copy of Summer Fun Spending").sheet1
# 
# # Leave a marker term and use cell find instead of trying anything fancy?
# x# marker = sheet.find("--PREV--")
# # For every API call, if it fails exit gracefully with log messages
# print("Found marker at R%sC%s" % (marker.row, marker.col))
# 
# # Move marker down to the next row
# 
# # Fill in prev row values
# 
# # sheet.update_cell(marker.row +1, marker.col, marker.value)

def get_sheet():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Copy of Summer Fun Spending").sheet1
    return sheet 

def split_message(message):
    # [ Date, Description, Price ]
    # If has date listed use, otherwise get current date
    # Separate by commas in text for ease of use?
    msg_parts = []
    
def input_message(sms, marker, sheet):
    print("Found marker at R%sC%s" % (marker.row, marker.col))
    sheet.update_cell(marker.row+1, marker.col, marker.value)
    # Split up message into the correct pieces and input
    msg_parts = sms.text.split(',')
    # if correct num chunks, 3 with date or 2 and use current date
    for i in range(0,3):
        sheet.update_cell(marker.row, marker.col + i, msg_parts[i])
    # sheet.update_cell(marker.row, marker.col, sms.text)

######### Main #########################

def update(sms):
    sheet = get_sheet()
    # Error check
    marker = sheet.find("--PREV--")
    if (sms.from_num == KEVIN):
        input_message(sms, marker, sheet)
    else:
        print sms.from_num
