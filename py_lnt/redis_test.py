#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime 
import redis
 
pool = redis.ConnectionPool(host='192.168.99.100', port=6379)
 
r = redis.Redis(connection_pool=pool)

def wr_perf(workload):
    for i in range(0, workload):
        r.set("foo" + str(i), 'Bar' + str(i))



def main():
    load_count = 10000
    start_t = datetime.now()
    wr_perf(load_count)
    end_t = datetime.now()
    print("write {} taking {}".format(str(load_count), str(end_t - start_t)))


if __name__ == "__main__":
    main()
