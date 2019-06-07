#!/usr/bin/python3
'''
    Ansible module to submit or terminate an AWS Batch Job
    Author: majmoham@
    Arguments:
        job_name: Name of the Batch Job to submit job defaults to Test_ansible_job
        job_queue_name: Name of the Batch Queue to sublit
        job_definition: Batch Job definition
        region: AWS Region defaults to ap-southeast-2
        state: State of the job defaults to submit, other option is terminate
        job_id: Job Id to terminate, only required if you are terminating a Batch job
        

'''

import boto3

from ansible.module_utils.basic import *


def batchJobSubmitApiCall(module,client):
    '''
        Function to call AWS Batch submit_job Api. This fuction would take Ansilbe module,Boto client as its arguments
    '''
    try:
        response = client.submit_job(
                     jobName=module.params["job_name"],
                     jobQueue=module.params["job_queue_name"],
                     jobDefinition=module.params["job_definition"])
        return {"changed":True, "meta" :{"jobID":response["jobId"]}}

    except Exception as e:
        return {"changed":False, "meta":{"Error":e.args}}


def batchJobTerminateApiCall(module,client):
    '''
        Function to call AWS Batch terminate_job Api. This fuction would take Ansilbe module,Boto client as its arguments
    '''
    try:
        response = client.terminate_job(
                   jobId=module.params["job_id"],
                   reason="Terminated from Ansible"
                   )
        return {"changed":True, "meta" :{"Job":module.params["job_id"] +  " - Job terminated successfully"}}
    except Exception as e:
        return {"changed":False, "meta":{"Error":e.args}}
    



def main():
    ''' 
       Main function called by Ansible Module
    '''

    fields = {
        "job_name": {"default": "Test_ansible_job", "type": "str"},
        "job_queue_name": {"default": "", "type": "str"},
        "region": {"default": "ap-southeast-2", "type": "str"},
        "state" : {"default": "submit", "type": "str"},
        "job_definition":  {"default": "", "type": "str"},
        "job_id": {"default": "", "type": "str"}
    }
    
    module = AnsibleModule(argument_spec=fields)
    client = boto3.client('batch',region_name=module.params["region"])
    if module.params["state"] == "submit":
        result_of_api_call=batchJobSubmitApiCall(module,client)
   
    if module.params["state"] == "terminate":
        result_of_api_call=batchJobTerminateApiCall(module,client)

####################
#Room to extend logic
####################
    module.exit_json(**result_of_api_call)


if __name__ == '__main__':
    main()
