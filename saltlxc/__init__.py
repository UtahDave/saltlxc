#!/usr/bin/python3
import json
import subprocess


def list_containers(list_all=False):
    '''
    List all containers
    '''
    ret = subprocess.getoutput("lxc list --format json")
    data = json.loads(ret)
    vms = []
    for vm in data:
        if list_all:
            vms.append(vm['name'])
        else:
            if 'Running' in vm['status']:
                vms.append(vm['name'])
    return (vms)


def start_container(vm):
    '''
    Start a container
    '''
    subprocess.getoutput("lxc start {0}".format(vm))
    return (vm)


def stop_container(vm):
    '''
    Stop a container
    '''
    subprocess.getoutput("lxc stop {0} --force".format(vm))
    return (vm)


def stop_all():
    '''
    Stop all running containers
    '''
    vms = list_containers()
    for vm in vms:
        subprocess.getoutput("lxc stop {0} --force".format(vm))
    return(vms)


