"""
This file contains functions to query revisions from the database.
"""

import optparse
import socket
import urllib
import urllib2
import sys
import json
import db

reload(sys)
sys.setdefaultencoding('utf-8')


def query_all_revisions():
    """
    This function queries all revisions from the database.

    Returns:
        A list of revisions.
    """
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)

def query_exact_revisions():
    """
    This function queries exact revisions from the database.

    Returns:
        A list of exact revisions.
    """
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)


def main():
    """
    This is the main function that calls the query functions.
    """
    query_all_revisions()
    query_exact_revisions()
