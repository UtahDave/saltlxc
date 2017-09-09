#!/usr/bin/python3
import click
import saltlxc

@click.group()
def cli():
    '''
    This is the Salt LXC environment command line client.

    All of saltlxc's features can be driven through the commands below.
    '''
    pass


@cli.command()
@click.option('--list-all', is_flag=True,
               help='list all containers even if shutdown')
def list(list_all):
    '''
    List all containers
    '''
    for vm in saltlxc.list_containers(list_all=list_all):
        click.echo(vm)


@cli.command()
@click.argument('vm')
def start(vm):
    '''
    Start up a vm
    '''
    saltlxc.start_container(vm)
    click.echo('% has been started' % vm)


@cli.command()
@click.argument('vm')
def stop(vm):
    '''
    Stop a vm
    '''
    saltlxc.stop_container(vm)
    click.echo('% has been stopped' % vm)

@cli.command()
def stop_all():
    '''
    Stop all running vms.
    '''
    vms = saltlxc.stop_all()
    click.echo('The following VMs have been stopped')
    for vm in vms:
        click.echo(vm)
