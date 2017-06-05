## Introduction

Load test a service running in AWS with four end-points that support get requests only. 

## Getting Started

- Start by installing conda(https://conda.io/docs/install/quick.html), the reason for using conda instead of virtualenv and pip is simply because conda
combines them both(pakaage management as well as environment management), and makes it very easy to create and manage environments and manage packages.
- Now its a good time to clone this repository, then run
```
$ cd PATH-TO-THE-ROOT-OF-THE-REPOSITORY
$ conda env create -f environment.yml 
```
- Activate the created environment (load_testing) by running
```
$ source activate load_testing On Mac 
$ activate load_testing On Win 
```
all the dependencies are automatically installed
- Run locust with the python locust file by simply running
```
$ locust (assuming you are in ROOT-OF-THE-REPOSITORY)
```
web-interface exposed by locust should be now visible at http://127.0.0.1:8089/
- Now start bokeh server by running
```
$ bokeh serve
```
- Run the real_time_plotter.py by executing
```
$ python real_time_plotter.py
This will open a new tab in the browser with plots
```
- Start the test by adding Number of Users (200) and Hatch rate (30) in the web interface
- Once all the locusts are hatched, you can switch to tab opened by bokeh to see metrics in real time
- After reaching a desired number of requests, you can just stop the test in locust web interface
- Go to download data tab, and download response time distribution CSV file to the ROOT-OF-THE-REPOSITORY/results
- Quit locust process(Ctrl+c), bokeh server and real_time_plotter.py
- This will automatically trigger on_locust_quit event, which saves all the resuest stats (collected by event handlers) as CSV file in ROOT-OF-THE-REPOSITORY/results
- Run static_plotter.py (change names of success stat file and distribution file) to get histogram/distribution plot.


