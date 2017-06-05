# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 11:36:44 2017

@author: sulav


This module enables us to visualize results in real-time using bokeh

Two figures for each endpoint
 - To show avg_response_time, median_response_time,
  min_response_time, and max_response_time
 - To show current_rps, num_failures
"""
import requests
from bokeh.client import push_session
from bokeh.layouts import gridplot
from bokeh.plotting import figure, curdoc
import settings

# configurations of the plot
bokeh_config = settings.BOKEHCONFIG

data_sources = {}  # dict with data sources for the figures
figures = []  # list to store figures

for endpoint in settings.ENDPOINTS:  # Make figures for each endpoint
    data_sources[endpoint] = {}
    # dict with data sources for each endpoint figure
    for figure_data in bokeh_config['figures']:
        # initialization of a figure
        new_figure = figure(
            title=figure_data['title'].format(endpoint.capitalize()))
        new_figure.xaxis.axis_label = figure_data['xlabel']
        new_figure.yaxis.axis_label = figure_data['ylabel']
        # adding charts to figure
        for chart in figure_data['charts']:
            # adding both markers and line for chart
            marker = getattr(new_figure, chart['marker'])
            scatter = marker(
                x=[0],
                y=[0],
                color=chart['color'],
                size=10,
                legend=chart['legend'])
            line = new_figure.line(
                x=[0],
                y=[0],
                color=chart['color'],
                line_width=1,
                legend=chart['legend'])
            # adding data source for markers and line
            data_sources[endpoint][chart['id']] = scatter.data_source = line.data_source
        figures.append(new_figure)

# Open a new session with the Bokeh Server,
# initializing it with our current Document.
# This local Document will be automatically kept in sync with the server.
session = push_session(curdoc())


# a periodic callback to be run every 1 second:
def update():
    try:
        resp = requests.get(settings.LOCUST_STATUS_URL)
    except requests.RequestException:
        return
    resp_data = resp.json()
    if resp_data['state'].upper() == "running".upper():
        # when all the users are hatched
        for index, endpoint in enumerate(settings.ENDPOINTS):
            new_data = resp_data['stats'][index]
            # Getting "/endpoint{index}" data from locust
            if endpoint in new_data["name"]:  # if endpoint matches
                for key, val in data_sources[endpoint].iteritems():
                    # adding data from locust to data_source of our graphs
                    # i.e updating the data source
                    val.data['x'].append(new_data["num_requests"])
                    val.data['y'].append(new_data[key])
                    # trigger data source changes
                    val.trigger('data', val.data, val.data)

curdoc().add_periodic_callback(update, 1000)
session.show(gridplot(figures, ncols=2))
# open browser with gridplot containing 2 figures in row for each endpoint
session.loop_until_closed()
# run forever
