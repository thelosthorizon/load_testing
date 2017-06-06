#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:43:49 2017

@author: skype
"""
import os
import logging
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import settings


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s %(message)s')

LOGGER = logging.getLogger(__name__)

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
        LOGGER.info("Empty csv file")
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
        LOGGER("Empty csv file")
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
    parser = argparse.ArgumentParser(
        description='Run static_plotter to get histrogram/distribution plots')
    parser.add_argument(
        '-s',
        '--success_csv',
        help='Success histogram csv file name',
        required=True)
    parser.add_argument(
        '-d',
        '--distribution_csv',
        help='Distributed csv file name',
        required=True)
    args = vars(parser.parse_args())
    LOGGER.info("success file %s", args["success_csv"])
    success_histogram(args["success_csv"])
    LOGGER.info("distribution file %s", args["distribution_csv"])
    distribution_barchart(args["distribution_csv"])
