#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from urllib import request


CORPUS_URL = "https://huggingface.co/datasets/gweltou/wikipedia-br-20240325/resolve/main/data.txt?download=true"


def download(url, filename):
    try:
        print(f"Downloading from {CORPUS_URL}")
        request.urlretrieve(url, filename)
        print(f"File successfully downloaded to '{filename}'")
    except Exception as e:
        print("Error downloading file")


if __name__ == "__main__":
    if not os.path.exists("corpus.txt"):
        download(CORPUS_URL, "corpus.txt")
    else:
        print("File 'corpus.txt' already present in directory")
