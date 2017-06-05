#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:43:49 2017

@author: skype
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import settings

COLORS = "bgrcmykw"
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def success_histogram(filename):
    """
    Makes histogram of response times for each endpoint data
    """
    try:
        df = pd.read_csv(
            os.path.join(RESULTS_DIR, filename), header=None)
    except pd.errors.EmptyDataError:
        print("Empty csv file")
        return
    for i in range(1, 5):
        filtered_data = (df.loc[df[0] == 'endpoint{}'.format(i)])
        plt.hist(
            filtered_data[2],
            histtype='stepfilled',
            bins=50,
            label='endpoint{}'.format(i),
            alpha=1.0 if i == 1 else 0.5,
            color=COLORS[i-1])
    plt.title("response time for different endpoints")
    plt.xlabel("response time")
    plt.ylabel("count")
    plt.legend()
    fig = plt.gcf()
    fig.set_size_inches(11.69, 8.27)
    plt.savefig(
        os.path.join(
                RESULTS_DIR,
                'success_hist_{}.png'.format(settings.CUR_TIME)),
        bbox_inches='tight',
        dpi=300)


def distribution_barchart(filename, save_png=True):
    """
    Makes histogram of exceptions for each endpoint data
    """
    try:
        df = pd.read_csv(
            os.path.join(RESULTS_DIR, filename))
    except pd.errors.EmptyDataError:
        print("Empty csv file")
        return
    df2 = df.set_index("Name")
    data = df2.loc["GET /endpoint1":"GET /endpoint4", "50%":"100%"]
    ax = data.plot.bar(figsize=(11.69, 8.27))
    fig = ax.get_figure()
    fig.savefig(
        os.path.join(
                RESULTS_DIR,
                'distribution_{}.png'.format(settings.CUR_TIME)),
        bbox_inches='tight',
        dpi=300)

if __name__ == "__main__":
    success_file = r"2017_06_05_09_38_stats_success.csv"
    success_histogram(success_file)
    distribution_file = r"distribution_1496648280.13.csv"
    distribution_barchart(distribution_file)
