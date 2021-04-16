# Create a script that should find the lines by provided pattern in the provided path directory with recursion (it means
# if the directory has other directories, the script should get all the info from them as well) and threads.
import glob
import time
from concurrent.futures import ThreadPoolExecutor


def find_by_pattern(file, pattern):
    line_container = set()
    with open(file) as f:
        for line in f:
            if pattern in line:
                line_container.add(line)
    return line_container


def find_all_by_pattern(directory_path, pattern):
    files = glob.glob(f'{directory_path}/**/*.py', recursive=True)
    container = set()
    with ThreadPoolExecutor() as pool:
        result = pool.map(find_by_pattern, files, pattern*len(files))
        for res in result:
            container.update(res)
    return container


if __name__ == "__main__":
    start = time.time()
    search_by_pattern = find_all_by_pattern('/home/mariana/Документи/CURSOR', pattern=['import'])
    end = time.time() - start
    print(f'Search time in {end} seconds')
    for line in search_by_pattern:
        print(line)


# Output:
# Search time in 0.0265500545501709 seconds
# import pickle
#
# from sys import argv
#
# import HW10_AuthAndReg as Ar
#
# import openpyxl
#
# import dataclasses
#
# import getopt
#
# import random
#
# from ex4 import Open2
#
# import multiprocessing
#
# import json
#
# import time
#
# from threading import current_thread
#
#     search_by_patter = find_all_files('.', pattern='import')
#
# import threading
#
# from selenium import webdriver
#
# import functools as f
#
# import datetime
#
# import collections
#
# from select import select
#
# # '03:13': 'and not under the stressful conditions ', '03:15': 'when we usually make these very important decisions. ',
#
# from threading import Thread
#
# import requests
#
# import yaml
#
# from multiprocessing import Process
#
# import xml.etree.ElementTree as ET
#
# # day. ', '00:04': 'But a financial day is just as important. ', '00:07': '[Your Money and Your Mind with Wendy De La
#
# from multiprocessing import Process, Queue
#
# from functools import wraps
#
# import numpy
#
#     from time import sleep
#
# import csv
#
# from multiprocessing_examples import Process
#
# from check import *
#
# import asyncio
#
# from abc import ABC, abstractmethod
#
# import pytest
#
# import contextlib
#
# import flask
#
# from multiprocessing import Process, current_process
#
# import os
#
# from __future__ import annotations
#
# from pickle import loads
#
# import socket
#
# import uuid
#
# from flask_restful import Api, Resource, reqparse
#
# from ex1 import Calc
#
# from multiprocessing import Pool, Process
#
# from multiprocessing import Pool
#
# import keyword
#
# from logging import handlers
#
# from ex2 import Vector3f
#
# from functools import reduce
#
# import HW10_RobotCleaner
#
# import sys
#
# from selenium.webdriver.common import keys
#
# from apitest.exceptions import *
#
#     search_by_pattern = find_all_by_pattern('/home/mariana/Документи/CURSOR', pattern=['import'])
#
# import argparse
#
# import aiohttp
#
# from apitest.api_script import Register
#
# from requests import HTTPError, ConnectionError
#
# from concurrent.futures import ThreadPoolExecutor
#
#     search_by_pattern = find_all_files("C:/Users/YPanin01/PycharmProjects/pythonProject5", pattern='import')
#
# from typing import Dict, Any
#
# # productive as possible. ', '00:52': 'But here are the big headlines that are the most important to cover, ', '00:55':
#
# import glob
#
# from concurrent.futures import ProcessPoolExecutor
#
# from ex1 import __version__ as v
#
# import logging
#
# import unittest
#
#
# Process finished with exit code 0
