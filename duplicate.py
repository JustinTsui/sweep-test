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
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)

def query_exact_revisions():
    sql = "SELECT c.`project`, p.`revision`, p.`id` FROM patch_set p, `change` c WHERE c.`change_number` = p.`change_number`"
    return db.query(sql)


def main():
  query_all_revisions()
  query_exact_revisions()
