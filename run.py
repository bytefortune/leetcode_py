# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# sys.path.append(os.path.dirname(os.getcwd()))
# from multiprocessing import Process

# from main.zdm_crawler import run_process as zdmCrawler
# from selfpool.proxy_crawler import run_process as proxyCrawler
# from selfpool.proxy_refresh import run_process as proxyRefresh


class Run(object):
    def __init__(self):
        # self.zdmCrawler = ZdmCrawler()
        # self.proxyCrawler = ProxyCrawler()
        # self.proxyRefresh = ProxyRefresh()
        pass

    def run_interface(self):
        pass


if __name__ == '__main__':
    run = Run()
    run.run_interface()
