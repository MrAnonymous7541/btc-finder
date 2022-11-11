# -*- coding: utf-8 -*-
import time
from colored import fg, bg, attr
import json
import os
import subprocess
import sys
import re
w = fg("#000000") + bg(15)
r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(244)
i = fg("#FFFFFF") + bg(4)
yl = fg("#000000") + bg("#F1C40F")
re = attr("reset")




class BitcoinOffline:
    def __init__(self):
        self.log = True
        self.colortmp = False

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("")

    def printLog(self, id = "", text = ""):
        if self.log == False:
            return
        if self.colortmp:
            self.colortmp = False
            print('{}{}{}{}'.format(id ,fg("#FFFFFF"), text, attr("reset")))
        else:
            self.colortmp = True
            print('{}{}{}{}'.format(id , fg("#000000") + bg(251), text, attr("reset")))
    def updt(self, total, progress):
        barLength, status = 40, ""
        progress = float(progress) / float(total)
        if progress >= 1.:
            progress, status = 1, ""
        block = int(round(barLength * progress))
        text = "|{}| {:.0f}% {}".format(
            "█" * block + "-" * (barLength - block), round(progress * 100, 0),
            status)
        return text

    def main(self):
        #self.cls()
        indx = 0
        for key, val in self.menu.items():
            num = f"{r2}[{b}{key}{r2}]"
            print(

                f" {num:<6} {val['name']:<{20 if int(key) < 10 else 19}}",
                end=""
                    "\n" if indx % 2 == 0 else "\n"
            )
            indx += 1

        option = input(f"\n {yl}[{b}?{r2}{yl}] Option : {re} ").strip()

        if option in self.menu:
            data = self.menu[option]
            data["function"]()
            input(f"\n {yl}[{b}!{r2}{yl}] Press Enter to continue{re}\n")
        else:
            input(f"\n {yl}[{b}!{r2}{yl}] There is no such option. Press Enter to continue{re}\n")
        self.main()

    def go(self):
        self.main()

    def random_gen(self):
        print("\nStart random_gen")

    def puzzle_gen(self):
            f = open('modules/pazzles.json', )
            pazzles = json.load(f)
            pazl = 0

            for key in pazzles:
                val = pazzles[key]
                num = f" {r2}[{b}{val['bit']}{r2}] "
                bal = '{:.2f}'.format(float(val['balance']))
                self.printLog(num, f"Balance: {bal} | Rage: {val['rage']} | Address: {val['adr']} ")
                pazl += 1
            f.close()
            print("")
            print(f" {r2}[{b}0{r2}{r2}] Back")
            print(f'\n{i}>>> What is a bitcoin puzzle?\nIn 2015, to show the huge size of the private key space (or maybe just for fun), someone created a "puzzle" in which he chose keys in a certain smaller space and sent increasing amounts to each of those keys. (total 32,896 BTC)\nAs of June 2020, the first addresses 63 and 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115 have been hacked. People are still trying to hack address #64, which requires scanning 9.223.372.036. 854.775.808 keys.{re}')
            option = input(f"\n {yl}[{b}?{r2}{yl}] Option : {re} ").strip()
            print(">>> Found private keys will be in the file: /data/wet_cuda.txt")
            if option in pazzles:
                #print(pazzles[option])


                cmds = f"SP_mode.exe -o wet_cuda.txt -r -c --keyspace {pazzles[option]['startKey']}:{pazzles[option]['stopKey']} {pazzles[option]['adr']}"

                try:

                    process = subprocess.Popen(
                        cmds,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        shell=True,
                        encoding='utf-8',
                        cwd="./data/",
                        errors='replace'
                    )

                    while True:
                        realtime_output = process.stdout.readline()

                        if realtime_output == '' and process.poll() is not None:
                            break

                        if realtime_output:
                            if "total" in realtime_output.strip():
                                sys.stdout.write("\r{}".format(realtime_output.strip()))
                                sys.stdout.flush()
                            elif "%" in realtime_output.strip():
                                real = realtime_output.strip().split(' ')
                                percent = round(float(real[2][:-1]))

                                bar = self.updt(100, percent)
                                data = real[0]
                                bar = f"{bar}\n" if percent == 100 else bar
                                sys.stdout.write(f"\r{data} [Info] {bar}")
                                sys.stdout.flush()
                            elif "Bitcrack" not in realtime_output.strip() and realtime_output.strip() != "":
                                print(realtime_output.strip(), flush=True)

                finally:
                    process.terminate()

                print("Process closed")


            elif option == "0":
                self.main()
            else:
                input(f"\n {yl}[{b}!{r2}{yl}] {option} There is no such option. Press Enter to continue{re}\n")
            #self.cls()
            self.puzzle_gen()
    def puzzle_gen_cl(self):
            f = open('modules/pazzles.json', )
            pazzles = json.load(f)
            pazl = 0

            for key in pazzles:
                val = pazzles[key]
                num = f" {r2}[{b}{val['bit']}{r2}] "
                bal = '{:.2f}'.format(float(val['balance']))
                self.printLog(num, f"Balance: {bal} | Rage: {val['rage']} | Address: {val['adr']} ")
                pazl += 1
            f.close()
            print("")
            print(f" {r2}[{b}0{r2}{r2}] Back")
            print(f'\n{i}>>> What is a bitcoin puzzle?\nIn 2015, to show the huge size of the private key space (or maybe just for fun), someone created a "puzzle" in which he chose keys in a certain smaller space and sent increasing amounts to each of those keys. (total 32,896 BTC)\nAs of June 2020, the first addresses 63 and 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115 have been hacked. People are still trying to hack address #64, which requires scanning 9.223.372.036. 854.775.808 keys.{re}')
            option = input(f"\n {yl}[{b}?{r2}{yl}] Option : {re} ").strip()
            print(">>> Found private keys will be in the file: /data/wet_cl.txt")
            if option in pazzles:


                cmds = f"SP2_mode.exe -b 64 -t 256 -p 1024 --rstride 12 -o wet_cl.txt --keyspace {pazzles[option]['startKey']}:{pazzles[option]['stopKey']} {pazzles[option]['adr']}"
                try:

                    process = subprocess.Popen(
                        cmds,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        shell=True,
                        encoding='utf-8',
                        cwd="./data/",
                        errors='replace'
                    )

                    tmp = ""
                    while True:
                        realtime_output = process.stdout.readline()

                        if realtime_output == '' and process.poll() is not None:
                            break

                        if realtime_output:
                            if "TOTAL" in realtime_output.strip() or "total" in realtime_output.strip():

                                try:
                                    tlog = realtime_output.strip().replace("\r", "").replace("\n", "")
                                    tlog = tlog.split("[")
                                    sys.stdout.write(
                                        "\r[{}[{}[{}[{}[{}".format(tlog[1].replace("DEV: ", ""), tlog[4], tlog[5],
                                                                   tlog[6], tlog[7]))
                                    sys.stdout.flush()
                                except:
                                    sys.stdout.write("\r{}".format(realtime_output.strip()))
                                    sys.stdout.flush()


                            elif "%" in realtime_output.strip():
                                real = realtime_output.strip().split(' ')
                                data = real[0]
                                if "%" in data:
                                    data = tmp
                                else:
                                    tmp = data
                                try:
                                    if "Done" in realtime_output.strip():
                                        percent = 10

                                    else:
                                        percent = round(float(real[2][:-1]))
                                except:
                                    percent = 100
                                bar = self.updt(100, percent)
                                bar = f"{bar}\n" if percent == 100 else bar
                                sys.stdout.write(f"\r{data} [Info] {bar}")
                                sys.stdout.flush()
                                time.sleep(1)
                            elif realtime_output.strip() != "":
                                pass
                                print(realtime_output.strip(), flush=True)

                finally:
                    process.terminate()

                print("Process closed")


            elif option == "0":
                self.main()
            else:
                input(f"\n {yl}[{b}!{r2}{yl}] {option} There is no such option. Press Enter to continue{re}\n")
            #self.cls()
            self.puzzle_gen()

offline = BitcoinOffline()
offline.puzzle_gen()


