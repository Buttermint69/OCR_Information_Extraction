import re

import pandas as pd


class regex:

    def __init__(self):
        self.s = {"phone": "Phone : (\d{10})",
                  "date": "Date : (\d{2}-\d{2}-\d{4})",
                  "patient": "Pat[a-z]ent Name\:([a-zA-Z0-90]+)",
                  "time": "Time : (\d{2}:\d{2})",
                  "total_items": "Total Item: (\d{1})",
                  "sub_total": "SUB TOTAL: (\d[0-9]+\.\d[0-9]+)",
                  "discount": "DISCOUNT: (\d[0-9]+\.\d[0-9]+)",
                  "sgst": "SGSTAmt (\d[0-9]+\.\d[0-9]+)",
                  "cgst": "CGST Amt: (\d[0-9]+\.\d[0-9]+)",
                  "round_off": "ROUND OFF\W (\D\d+\.\d[0-9]+)",
                  "grand_total": "G\.TOTAL \W\W (\d[0-9]+\.\d[0-9]+)",
                  "balance": "Balance (\d+\.\d[0-9]+)"
                  }
        self.empty = dict()

    def info_extract(self, txt):
        # Phone number
        phone_match = re.findall(self.s["phone"], txt)
        self.empty["Phone Number"] = phone_match

        # Date
        date_match = re.findall(self.s["date"], txt)
        self.empty["Date"] = date_match

        # Patient Name
        match_patient = re.findall(self.s["patient"], txt)
        self.empty["Patient Name"] = match_patient

        # Time
        time_match = re.findall(self.s["time"], txt)
        self.empty["Time"] = time_match

        # Total Item
        total_item_match = re.findall(self.s["total_items"], txt)
        self.empty["total_items"] = total_item_match

        # Sub Total
        sub_tot_match = re.findall(self.s["sub_total"], txt)
        self.empty["sub_total"] = sub_tot_match

        # Discount
        discnt_match = re.findall(self.s["discount"], txt)
        self.empty["discount"] = discnt_match

        # SGST
        sgst_match = re.findall(self.s["sgst"], txt)
        self.empty["sgst"] = sgst_match

        # CGST
        cgst_match = re.findall(self.s["cgst"], txt)
        self.empty["cgst"] = cgst_match

        # RoundOFF
        round_match = re.findall(self.s["round_off"], txt)
        self.empty["round_off"] = round_match

        # Total
        total_match = re.findall(self.s["grand_total"], txt)
        self.empty["grand_total"] = total_match

        # Balance
        balance_match = re.findall(self.s["balance"], txt)
        self.empty["balance"] = balance_match

        # Cash Recieved
        cash_r = float(total_match[0]) - float(balance_match[0])
        self.empty["cash_r"] = cash_r

        return self.empty
