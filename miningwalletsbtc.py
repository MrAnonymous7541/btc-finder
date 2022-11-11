# -*- coding: utf-8 -*-
import os
import time
import sys
import ctypes
import subprocess
import requests
import bit
from bit import Key
from core import soft
from colored import fg, bg, attr
from multiprocessing.pool import ThreadPool as Pool
import argparse
from ctypes import *
import urllib.request as urllib2
import urllib.parse as urlparse
import coincurve
import threading
import gzip
import io


threads = 3
os.system('mode con: cols=130 lines=30')
r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(3)
w = fg(15)
y = fg(3) + attr(1)
d = r2 + attr(21)
yl = fg("#000000") + bg("#F1C40F")
re = attr("reset")



class Files():
    profit = 'wet.txt'
    baseName = 'data/infile_base.txt'
    t = []


class Settings():
    title = f"BITCOIN MINING WALLETS v{soft.ver} | TELEGRAM: {soft.tlgrm}"
    log = False
    debug = False
    total_count = 0
    total_count_old = 0
    time_old = 0
    threading_count = 0
    wet_count = 0
    time_lastupdate = time.time()
    time_lastupdategift = time.time()
    key_count = 5456
    secretkey = False
    colortmp = False
    threads = threads #round(os.cpu_count()/2)
    start_time = time.time()

ctypes.windll.kernel32.SetConsoleTitleW(f"{Settings.title}")
lock = threading.Lock()


def counter():

    try:
        end = time.time()

        secheck = end - Settings.time_old
        timeHcheckh = round((3600 / secheck) * (Settings.total_count - Settings.total_count_old))
        timeHcheck = round((60 / secheck) * (Settings.total_count - Settings.total_count_old))
        timeDcheck = round(timeHcheck * 24)
        timeHcheckf = "{:0,.0f}".format(timeHcheck)
        timeDcheck = "{:0,.0f}".format(timeDcheck)
        total_count = "{:0,.0f}".format(Settings.total_count)
        seconds = end - Settings.start_time
        timer_start = time.strftime("%H:%M:%S",time.gmtime(seconds))

        if (end - Settings.time_lastupdate) > 60:
            Settings.time_lastupdate = end
            soft.update_totals(Settings.secretkey, round(Settings.total_count/1000000,2))
            soft.update_speed(Settings.secretkey,  round( timeHcheckh/1000000,2))


        ctypes.windll.kernel32.SetConsoleTitleW(
            f"{Settings.title} | With Balance: {Settings.wet_count} - Total checks: {total_count} - Speed Checks : ~{timeHcheckf}/sec ~{timeDcheck}/day - Threads: {Settings.threads} Time work: {timer_start}")
        if Settings.total_count_old != Settings.total_count:
            Settings.total_count_old = Settings.total_count
        if Settings.time_old != end:
            Settings.time_old = end


        return True
    except Exception as err:
        print(err)
        return False

def add_wet( Address, Private, Balance = True):
    if (Balance == True or Balance == "" or Balance == 0):
        Balance = soft.get_balance(Address)

    with open(Files.profit, 'a') as out:
        print('FIND')

        Settings.wet_count += 1
        out.write('Balance: {} | Address: {} | Private key: {}\n'.format(Balance,Address, Private))
        print('\n{}>>> Balance: {} | Address: {} | Private key: {}{}'.format(bg(2)+fg(15), Balance,Address, Private,
                                                         attr("reset")))


def check():

    Settings.threading_count += 1
    thist_count = Settings.threading_count;

    try:

        while True:

            if Settings.debug == True:
                print("{}Generation addresses{}".format(bg("#000000") + fg("#F1C40F"), attr("reset")))
            mass = {}
            for _ in range(Settings.key_count):
                k = Key()

                mass[k.address] = k.to_wif()
                mass[k.segwit_address] = k.to_wif()
            if Settings.debug == True:
                print("{}Checks addresses{}".format(fg("#000000") + bg("#F1C40F"), attr("reset")))

            with lock:
                for key in mass:
                    print(f"Balance: 0 | Address: {key} | Key: {mass[key]}")
                    Settings.total_count += 1
                    #PrintLog(key, mass[key])
                    if key in Files.t:
                        add_wet(key, mass[key])


            if thist_count == 1:
                counter()


    except Exception as err:
        print(err)


def getInternet():
    try:
        try:
            requests.get('https://www.google.com')
        except requests.ConnectTimeout:
            requests.get('http://1.1.1.1')
        return True
    except requests.ConnectionError:
        return False


def printLog(text=""):
    if Settings.log == False:
        return
    if Settings.colortmp:
        Settings.colortmp = False
        print('{}{}{}'.format(fg("#000000")+bg("#cccccc"), text, attr("reset")))
    else:
        Settings.colortmp = True
        print('{}{}{}'.format(fg(255) + bg(232), text, attr("reset")))

def start():
        print("Welcome to BITCOIN MINING WALLETS")
        print("==================================================================")
        print("   ")
        print("BITCOIN BALANCE FINDER by @mining_21_bot")
        print("   ")
        print("Don't forget to update the database!")
        up = input("Update base? (write 'Y' or 'N'): ")
        if up == 'Y':
            update()


        print("Starting...")
        start = time.time()
        f = open(Files.baseName, 'r')
        Files.t = set(f.read().split('\n'))
        end = time.time()
        f.close()

        print("Base opening time: {}/sec {}".format(round(end - start), attr("reset")))
        print(">>> Starting...")
        ctypes.windll.kernel32.SetConsoleTitleW(f"{Settings.title} | counting in progress")
        time.sleep(3)

        pool = Pool(threads)
        for _ in range(threads):
            pool.apply_async(check, ())
        pool.close()
        pool.join()




def updt(total, progress):
    barLength, status = 40, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r|{}| {:.0f}% {}".format(
        "█" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()



def is_accessible(path, mode='r'):
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True


def download_file(url, dest=None):
    """
    Download and save a file specified by url to dest directory,
    """
    u = urllib2.urlopen(url)

    scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
    filename = os.path.basename(path)
    if not filename:
        filename = 'downloaded.file'
    if dest:
        filename = os.path.join(dest, filename)

    with open(filename, 'wb') as f:
        meta = u.info()
        meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
        meta_length = meta_func("Content-Length")
        file_size = None
        if meta_length:
            file_size = int(meta_length[0])
        print("Downloading: {0} Bytes: {1}".format(url, file_size))

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)

            status = file_size_dl * 100 / file_size
            if file_size:
                updt(100, status)





    return filename

def update():
    filename = "Bitcoin_addresses_LATEST.txt.gz"
    url = f"http://addresses.loyce.club/{filename}"
    if (is_accessible(filename)):
        unzip(filename)
    else:
        print("Downloading base...")
        filename = download_file(url)
        unzip(filename)

def unzip(filename):
    tmpfile = "data/infile_tmp"
    outfile = "data/infile_base.txt"
    oldfile = "data/infile_base_old.txt"

    if (is_accessible(oldfile)):
        os.remove(oldfile)

    if (is_accessible(tmpfile)):
        os.remove(tmpfile)

    if (is_accessible(outfile)):
        os.rename(outfile, oldfile)

    gz = gzip.open(filename, 'rb')
    bsOut = open(outfile, 'w')
    try:

        print("Unpacked base...")

        f = io.BufferedReader(gz)
        for line in f.readlines():
            l = line.decode("utf-8")
            if l[0] in ["1", "3"]:
                bsOut.write('{}'.format(l))
    except:
        print("Error Unpacked Base!")
        if (is_accessible(outfile)):
            os.remove(outfile)
        print("Starting...")
        update()
        pass
    gz.close()
    bsOut.close()
    os.remove(filename)
    print("Deleting temp files...")
    print(">>> OK")



if __name__ == '__main__':
    start()
