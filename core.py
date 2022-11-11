# -*- coding: utf-8 -*-
import subprocess
import time

import requests
import hashlib


class soft:
    def __init__(self):
        self.ver = "1.0"
        self.name = "BITCOIN MINING WALLETS"
        self.tlgrm = "@mining_21_bot"
        self.title = "FIND FORGOTTEN WALLETS"
        self.sol = "12fdgas329"


    def get_balance(self, addr):

        try:
            response = requests.get(f'https://blockchain.info/q/addressbalance/{addr}').text
            if response.isnumeric():
                return (int(response) / 100000000)
            else:
                return 0
        except:
            pass

    def get(self):
        return self.name

    def chack_offline(self, secret=False, log=True):
        import sys
        try:
            sys.path.insert(0, '../main.py')
        except:
            import main


        return True







soft = soft()

