 Prerequists
 1) boto3 installed
 2) AWS credentials configured (Either through awscli or IAM roles)
 3) Python 3 installed
 4) "pip3 install ansible" which should have the library (ansible.module_utils.basic) required.
 
 ============ Submit Job============================
 
 $ansible-playbook ansible_Submit_or_Terminate_Batch_Job.yaml -e '{"job_queue_name":"first-run-job-queue"}' -e '{"job_name":"myJob"}'
 
 [WARNING]: Unable to parse /etc/ansible/hosts as an inventory source

 [WARNING]: No inventory was parsed, only implicit localhost is available

 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'


PLAY [localhost] ****************************************************************************************************************************************************************

TASK [Test that my change_version module works] *********************************************************************************************************************************
changed: [localhost]

TASK [debug] ********************************************************************************************************************************************************************
ok: [localhost] => {
    "result": {
        "changed": true,
        "failed": false,
        "meta": {
            "jobID": "ffd2a0a5-bc04-4886-b3fe-5d5eaeddcd10"
        }
    }
}

PLAY RECAP **********************************************************************************************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0   







============== Terminate Job =======================


$ ansible-playbook ansible_Submit_or_Terminate_Batch_Job.yaml -e '{"state":"terminate"}' -e '{"job_id":"ffd2a0a5-bc04-4886-b3fe-5d5eaeddcd1"}'

 [WARNING]: Unable to parse /etc/ansible/hosts as an inventory source

 [WARNING]: No inventory was parsed, only implicit localhost is available

 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'


PLAY [localhost] ****************************************************************************************************************************************************************

TASK [Test that my change_version module works] *********************************************************************************************************************************
changed: [localhost]

TASK [debug] ********************************************************************************************************************************************************************
ok: [localhost] => {
    "result": {
        "changed": true,
        "failed": false,
        "meta": {
            "Job": "ffd2a0a5-bc04-4886-b3fe-5d5eaeddcd1 - Job terminated successfully"
        }
    }
}

PLAY RECAP **********************************************************************************************************************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0   
