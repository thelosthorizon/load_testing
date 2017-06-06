#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:45:30 2017

@author: sulav

This module holds all the settings
"""
import time

# current time
CUR_TIME = time.strftime("%Y_%m_%d_%H_%M")


# The URL to the host thats running the service
SERVICE_URL = r"http://54.229.152.248:8967"

# To get Locust data in JSON format
LOCUST_STATUS_URL = r"http://localhost:8089/stats/requests"

ENDPOINTS = ["endpoint1", "endpoint2", "endpoint3", "endpoint4"]

# Bokeh plot config
BOKEHCONFIG = {
    "figures": [
        {
            "charts": [
                {
                    "color": "black",
                    "legend": "average response time",
                    "marker": "diamond",
                    "id": "avg_response_time"},
                {
                    "color": "blue",
                    "legend": "median response time",
                    "marker": "triangle",
                    "id": "median_response_time"},
                {
                    "color": "green",
                    "legend": "min response time",
                    "marker": "inverted_triangle",
                    "id": "min_response_time"},
                {
                    "color": "red",
                    "legend": "max response time",
                    "marker": "circle",
                    "id": "max_response_time"}],
            "xlabel": "Requests count",
            "ylabel": "Milliseconds",
            "title": "{} response times"
        },
        {
            "charts": [
                {
                    "color": "green",
                    "legend": "current rps",
                    "marker": "circle",
                    "id": "current_rps"},
                {
                    "color": "red",
                    "legend": "failures",
                    "marker": "cross",
                    "id": "num_failures",
                    "skip_null": True}],
            "xlabel": "Requests count",
            "ylabel": "RPS/Failures count",
            "title": "{} RPS/Failures"
         }],
    # names of endpoint tested
  }
