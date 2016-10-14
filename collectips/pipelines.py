# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class CollectipsPipeline(object):
    def process_item(self, item, spider):
        DBKWARFS = spider.settings.get('DBKWARGS')
        # print DBKWARFS
        con = MySQLdb.connect(**DBKWARFS)
        # print con
        # print con.messages
        cur = con.cursor()
        # print cur.messages
        sql = ("insert into proxy(IP,PORT,TYPE,POSITION,LAST_CHECK_TIME)"
               "values(%s,%s,%s,%s,%s)")
        lis = (item['IP'],item['PORT'],item['TYPE'],item['POSITION'],item['LAST_CHECK_TIME'])
        try:
            # cur.execute('insert into proxy(ip) value("111")')
            print sql
            print lis
            cur.execute(sql,lis)
            # cur.commit()
        except Exception, e:
            print "Insert error:", e
            con.rollback()
        con.commit()
        cur.close()
        con.close()

        return item
