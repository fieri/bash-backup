from __future__ import print_function

import requests
import threading

import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class GetterTread(threading.Thread):
    def __init__(self, thread_id, app_id, times=1000):
        threading.Thread.__init__(self)

        self.__thread_id = thread_id

        self.__URL = "http://pcs.baidu.com/rest/2.0/pcs/file?app_id={}&method=list&path=%2F"

        with open("./BDUSS.txt") as f:
            BDUSS = f.readline()
            self.__COOKIES = {"BDUSS": BDUSS}

        self.app_id = app_id
        self.times = times

    def run(self):
        current_id = self.app_id
        while current_id - self.app_id < self.times:  # 250000:
            url = self.__URL.format(current_id)

            try:
                r = requests.get(url, cookies=self.__COOKIES)
                if r.status_code == 200:
                    print(current_id)
            except Exception:
                eprint("Exception: " + str(current_id))

            current_id += 1
            # print("id " + str(self.__thread_id) + " over")


if __name__ == '__main__':

    start_app_id = 300000
    times = 1000

    threads_list = []

    while start_app_id < 500000:
        thread = GetterTread(start_app_id, start_app_id, times)
        thread.start()
        threads_list.append(thread)
        start_app_id += times

    # print("size: " + str(len(threads_list)))

    for thread in threads_list:
        thread.join()
