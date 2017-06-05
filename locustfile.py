# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 11:36:44 2017

@author: sulav


This locustfile is intended for testing the service running at amazon aws

url: http://54.229.152.248:8967,
endpoints: /endpoint1-4

Each instance of the spawned Locust classe will start executing its
TaskSet(one task in this case). The task randomly generates the endpoint
between 1 and 4, generating an even load across all endpoints

min_wait, max_wait is left to default value (1 sec) i.e. each instance of
spawned locust class will wait for 1 sec before picking a new task
"""
import random
from locust import HttpLocust, TaskSet, task
import settings
import common


class TaskSet(TaskSet):

    @task
    def send_get_to_endpoints(self):
        """
        Task that makes a GET request to /endpoint1-4
        """
        self.client.get("/endpoint{}".format(random.randrange(1, 5, 1)))


class ApiUser(HttpLocust):
    """
    Locust class
    """
    task_set = TaskSet
    host = settings.SERVICE_URL

# Process test result
common.process_result(
    names=["endpoint{}".format(i) for i in range(1, 5)],
    save_stats=True)
