#!/usr/bin/python3
import json
import os
import requests
import subprocess
import click


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


def update_bootstrap():
    '''
    update the bootstrap script.
    '''
    url = 'https://bootstrap.saltstack.com'
    req = requests.get(url)
    if req.status_code != 200:
        return ('Failed to download stable version of the bootstrap script')
    script_content = req.text
    bootstrapscript = _bootstrap_path()
    with open(bootstrapscript, 'w') as bfile:
        bfile.write(script_content)
    return(bootstrapscript)


def _bootstrap_path():
    '''
    return bootstrap path and create it if it's not there.
    '''
    bootstrapscript_dir = click.get_app_dir('saltlxc')
    if not os.path.exists(bootstrapscript_dir):
        os.makedirs(bootstrapscript_dir)
    bootstrapscript = os.path.join(bootstrapscript_dir, 'bootstrap.sh')
    return(bootstrapscript)


def deploy_bootstrap(vm):
    '''
    Copy the bootstrap script to the lxc container.
    '''
    script = _bootstrap_path()
    path = '/root/bootstrap.sh'
    ret = subprocess.getoutput('lxc file push {0} {1}{2}'.format(script, vm, path))
    return(ret)

