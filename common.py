#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:23:51 2017

@author: sulav
"""
from locust import events
import settings

all_locust_hatched = False
request_success_stats = [[]]
request_fail_stats = [[]]


def process_result(names, save_stats=False):
    """
    This function processes test results, all the event handlers are defined
    here, the result is routed to a new end-point by default, but can also
    be saved to a local csv file if desired

    args:
        names: names of the endpoints
        save_stats: (optional) to save stats to json files
    """

    def on_request_success(
            request_type, name, response_time, response_length, **kwargs):
        """
        Event handler that get triggered on every successful request
        """
        if all_locust_hatched:  # Only store data when all locusts have hatched
            cur_endpoint_name = name.split("/")[1]
            request_success_stats.append(
                    [cur_endpoint_name, request_type, response_time])

    def on_request_fail(
            request_type, name, response_time, exception, **kwargs):
        """
        Event handler that get triggered on every successful request
        """
        if all_locust_hatched:  # Only store data when all locusts have hatched
            cur_endpoint_name = name.split("/")[1]
            request_fail_stats.append(
                [cur_endpoint_name, request_type, response_time, exception])

    def on_hatch_complete(user_count, **kwargs):
        """
        Event handler that gets triggered when all locusts hatch
        """
        global all_locust_hatched
        all_locust_hatched = True  # set all_locust_hatched identifier to True

    def on_locust_quit(**kwargs):
        """
        Event handler that gets triggered when when locust process is exiting
        """
        if save_stats:
            save_stats_to_disk()

    def save_stats_to_disk():
        """
        Save data to csv file (same directory as this file) with all the
        successful /failed requests from the test,
        file name contains timestamps as suffix
        """
        import os
        import csv
        results_dir = os.path.join(
            os.path.dirname(__file__), "results")
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        success_csv_file = os.path.join(
            results_dir,
            '{}_stats_success.csv'.format(settings.CUR_TIME))
        failed_csv_file = os.path.join(
            results_dir,
            '{}_stats_fail.csv'.format(settings.CUR_TIME))
        with open(success_csv_file, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for value in request_success_stats:
                writer.writerow(value)
        with open(failed_csv_file, 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for value in request_fail_stats:
                writer.writerow(value)
    events.request_success += on_request_success
    events.request_failure += on_request_fail
    events.quitting += on_locust_quit
    events.hatch_complete += on_hatch_complete
