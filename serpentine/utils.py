import argparse
import pkg_resources
import os

def _get_serpentine_resource_filename(path):
    return(pkg_resources.resource_filename('serpentine',path))

def list_rules(full_path=True):
    """List all discovered rule files"""
    rulefiles = os.listdir(_get_serpentine_resource_filename('supporting/rules'))
    if(full_path):
        return [os.path.join(_get_serpentine_resource_filename('supporting/rules'),r) for r in rulefiles]
    return rulefiles

def _list_rules(args):
    for r in list_rules(full_path=True):
        print(r)

def list_workflows(full_path=True):
    """List all discovered rule files"""
    wffiles = os.listdir(_get_serpentine_resource_filename('supporting/workflows'))
    if(full_path):
        return [os.path.join(_get_serpentine_resource_filename('supporting/workflows'),w) for w in wffiles]
    return wffiles

def _list_workflows(args):
    for r in list_workflows(full_path=False):
        print(r)

