"""
This script contains functions to query revisions from a database.
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
    Queries the database for all revisions.

    Returns:
        A list of revisions.
    """
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)

def query_exact_revisions():
    """
    Queries the database for exact revisions.

    Returns:
        A list of exact revisions.
    """
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)


def main():
    """
    Main function that calls the query functions.
    """
    query_all_revisions()
    query_exact_revisions()
