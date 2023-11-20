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

    This function executes a SQL query that selects the project, revision, and id from the patch_set and change tables.
    The change_number from the change table is used as a condition to match the corresponding records in the patch_set table.

    Returns:
        list: A list of tuples where each tuple represents a row from the result of the SQL query.
    """
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)

def query_exact_revisions():
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)


def main():
  query_all_revisions()
  query_exact_revisions()
        list: A list of tuples where each tuple represents a row from the result of the SQL query.
    """
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)


def main():
  query_all_revisions()
  query_exact_revisions()
