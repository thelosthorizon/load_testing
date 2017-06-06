## Introduction

Load test a service running in AWS with four end-points that support get requests only. 

## Getting Started

- Start by installing conda(https://conda.io/docs/install/quick.html), the reason for using conda instead of virtualenv and pip is simply because conda
combines them both(package management as well as environment management), and makes it very easy to create and manage environments and also manage packages.

- Now its a good time to clone this repository, then run
```
$ cd PATH-TO-THE-ROOT-OF-THE-REPOSITORY
$ conda env create --file environment.yml 
```
Use -n to specify the environment name, if not specified, it will create an environment called fun_with_load_testing

- Some Useful Conda Commands:
```
$ conda env list --> lists all the environment (ensure fun_with_load_testing is there)
$ conda list -n fun_with_load_testing --> lists all the packages installed in fun_with_load_testing environment
```

- Activate the created environment (load_testing) by running
```
$ source activate fun_with_load_testing On Mac 
$ activate fun_with_load_testing On Win 
```
All the dependencies are automatically installed in fun_with_load_testing environment

## Running Test

- Run locust with the python locust file by simply running
```
$ locust (assuming you are in ROOT-OF-THE-REPOSITORY)
```
web-interface exposed by locust should be now visible at http://127.0.0.1:8089/

- Now start bokeh server(in a new terminal window, do not forget to activate fun_with_load_testing environment) by running
```
$ bokeh serve
```
- Run the real_time_plotter.py by executing(in a new terminal window, do not forget to activate fun_with_load_testing environment)
```
$ python real_time_plotter.py
```
This will open a new tab in the browser with plots, if browser is running or will open the defauly browser

- Start the test by adding Number of Users (200) and Hatch rate (30) in the web interface at http://127.0.0.1:8089/

## Viewing Results

- Once all the locusts are hatched, you can switch to tab opened by bokeh to see plots in real time.

- After reaching a desired number of requests, you can just stop the test in locust web interface at http://127.0.0.1:8089/.

- Go to download data tab, and download response time distribution CSV file to the ROOT-OF-THE-REPOSITORY/results

- Quit locust process(Ctrl+C), bokeh server and real_time_plotter.py

- This will automatically trigger on_locust_quit event, which saves all the individual request stats (collected by event handlers) as CSV file in ROOT-OF-THE-REPOSITORY/results

- Now Run
```
$ python static_plotter.py --success_file NAME_OF_SUCCESS_CSV_IN_RESULTS_FOLDER --distribution_csv NAME_OF_DISTRIBUTION_CSV_IN_RESULTS_FOLDER
```
This will create response time histogram/distribution plots in results folder.


