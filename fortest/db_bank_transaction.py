# coding:utf8

import MySQLdb
import sys


class Transaction:
    def __init__(self, conn):
        self.conn = conn

    def transact(self, src_accid, des_accid, money):
        try:
            self.check_account_available(src_accid)
            self.check_account_available(des_accid)
            self.check_enough_money(src_accid, money)
            self.reduct_money(src_accid, money)
            self.add_money(des_accid, money)

            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_account_available(self, accid):
        sql = 'select count(*) from bank where accid=%s' % accid
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            rs = cursor.fetchone()
            print 'check_account_available: %s' % sql
            if rs[0] != 1:
                raise Exception('出现问题：账号%s不存在' % accid)
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def check_enough_money(self, accid, money):
        sql = 'select count(*) from bank where accid=%s and money >= %s' % (accid, money)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            rs = cursor.fetchone()
            print 'check_enough_money: %s' % sql
            if rs[0] != 1:
                raise Exception('出现问题：账号%s钱不够%s' % (accid, money))
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def reduct_money(self, accid, money):
        sql = 'update bank set money=money-%s where accid=%s' % (money, accid)
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            print 'reduct_money: %s' % sql
            if cursor.rowcount != 1:
                raise Exception('出现问题：账号%s减钱%s失败' % (accid, money))
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def add_money(self, accid, money):
        sql = 'update bank set money=money+%s where accid=%s' % (money, accid)
        cursor = self.conn.cursor()
        try:
            rs = cursor.execute(sql)
            print 'add_money: %s' % sql
            if cursor.rowcount != 1:
                raise Exception('出现问题：账号%s加钱%s失败' % (accid, money))
        except Exception as e:
            raise e
        finally:
            cursor.close()


if __name__ == '__main__':
    while True:
        src_accid = raw_input("src_accid: ")
        if src_accid == 'exit':
            break
        des_accid = raw_input("des_accid: ")
        money = raw_input("money: ")

        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123321', db='test', port=3306)
        try:
            transaction = Transaction(conn)
            transaction.transact(src_accid, des_accid, money)
        except Exception as e:
            print str(e)
        finally:
            conn.close()

            # create table bank (accid long, money int);
            # insert into bank values(1, 110);
            # insert into bank values(2, 10);
