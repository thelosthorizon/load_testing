#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:43:49 2017

@author: sulav
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

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def success_histogram(filename):
    """
    Makes histogram of response times for each endpoint data
    """
    try:
        df = pd.read_csv(
            os.path.join(RESULTS_DIR, filename),
            names=["Name", "RequestType", "ResponseTime"])
    except pd.errors.EmptyDataError:
        LOGGER.info("Empty csv file")
        return
    grouped = df["ResponseTime"].groupby(df["Name"])
    LOGGER.info("Stats: %s", str(grouped.describe()))
    means = grouped.mean()
    errors = grouped.std()
    ax2 = means.plot.bar(
        yerr=errors,
        legend=False,
        figsize=(11.69, 8.27),
        title="Average Response Time For Different Endpoints",
        )
    ax2.set_xlabel("Endpoints")
    ax2.set_ylabel("Average Response Time")
    fig2 = ax2.get_figure()
    fig2.savefig(
        os.path.join(
                RESULTS_DIR,
                'success_bar_{}.png'.format(settings.CUR_TIME)),
        bbox_inches='tight',
        dpi=300)
    plt.cla()
    for name, group in grouped:
        ax = group.plot.hist(
            figsize=(11.69, 8.27),
            label=name,
            legend=True,
            title="Response Time Histogram")
    ax.set_xlabel("Response Time")
    ax.set_ylabel("Count")
    fig = ax.get_figure()
    fig.savefig(
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
    ax = data.plot.bar(
        title="Response Time Percentiles",
        figsize=(11.69, 8.27))
    ax.set_xlabel("Endpoints")
    ax.set_ylabel("Response Time")
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
