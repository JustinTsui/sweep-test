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
    Query all revisions from the database.

    This function executes a SQL query that selects the project, revision, and id from the patch_set and change tables where the change_number matches.

    Returns:
        list: A list of tuples containing the project, revision, and id.
    """
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)

def query_exact_revisions():
    """
    Query exact revisions from the database.

    This function executes a SQL query that selects the project, revision, and id from the patch_set and change tables where the change_number matches.

    Returns:
        list: A list of tuples containing the project, revision, and id.
    """
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)


def main():
  query_all_revisions()
  query_exact_revisions()
