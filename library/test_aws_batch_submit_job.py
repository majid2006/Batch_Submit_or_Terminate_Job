#!/usr/bin/python3

from aws_batch_submit_job import *
import unittest
from unittest.mock import MagicMock
import json

##Patching batchJobSubmitApiCall to mock successful API call ####
batchJobSubmitApiCall = MagicMock(return_value={"changed":True, "meta" :{"jobID":"xxxxxxxxxxxxxxxxx"}})
fields = {
        "job_name": "test1",
        "job_queue_name": "TestQueue",
        "region": "ap-southeast-2",
        "state" : "submit",
        "job_definition": "testJD"
    }

#class testAnsibleModule(unittest.TestCase):
def test_main():
    intializeAnsibleModule(fields)
    print(main())

test_main()
