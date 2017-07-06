#! /usr/bin/env python
import gspread
import logging
from oauth2client.service_account import ServiceAccountCredentials

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

def authorize():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client.json', scope)
    client = gspread.authorize(creds)
    return client

def update(message):
    client = authorize()
    sheet = client.open("Copy of Summer Fun Spending").sheet1
    marker = sheet.find("--PREV--")
    print("Found marker at R%sC%s" % (marker.row, marker.col))
    sheet.update_cell(marker.row + 2, marker.col, message)


