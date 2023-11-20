import optparse
import socket
import urllib
import urllib2
import sys
import json
import db

reload(sys)
sys.setdefaultencoding('utf-8')

db = db.ReviewDB()

def update_diff_count(id, add, delete):
    sql = "update patch_set set lines_inserted=" + str(add) + ", lines_deleted=" + str(delete) + " where id = " + str(id)
    print sql
    return db.execute(sql)

  
