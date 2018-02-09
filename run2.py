import sys
import time
import os

Queues = ['DropTail', 'RED']
def calThroughput(queue_type, stage):
    trace = "trace/part2_2_" + queue_type+ ".trace"
    dat = "data/part2_2_" + queue_type + ".dat"
    f_w = open(dat, 'w')
    t1 = 0
    total_recieved_bytes_0 = 0
    total_recieved_bytes_1 = 0
    total_recieved_bytes_2 = 0
    with open(trace) as f:
        for line in f:
            records = line.split(' ')
            eve_type = records[0]
            t = float(records[1])
            f_n = records[2]
            t_n = records[3]
            pkt_type = records[4]
            pkt_size = int(records[5])
            f_id = records[7]
            f_addr = records[8]
            t_addr = records[9]
            s_n = records[10]
            if f_id == '1' and eve_type == 'r' and t_n == '3':
                total_recieved_bytes_0 += 1
            if f_id == '2' and eve_type == 'r' and t_n == '5':
                total_recieved_bytes_1 += 1
            if f_id == '3' and eve_type == 'r' and t_n == '7':
                total_recieved_bytes_2 += 1
            if t - t1 <= stage:
                pass
            else:
                tp_0 = float(total_recieved_bytes_0) * 8 /stage/ 1000000
                tp_1 = float(total_recieved_bytes_1) * 8 /stage/ 1000000
                tp_2 = float(total_recieved_bytes_2) * 8 /stage/ 1000000
                con = str(t1) + ' ' + str(tp_0) + ' ' + str(tp_1) + ' ' +  str(tp_2) + '\n'
                f_w.write(con)
                t1 += stage
                total_recieved_bytes_0 = 0
                total_recieved_bytes_1 = 0
            f_w.close  
def calLatency(queue_type, stage):
    trace = "trace/part2_2_" + queue_type+ ".trace"
    dat = "data/part2_2_" + queue_type + "_l.dat"
    f_w = open(dat, 'w')
    sends1 = {}
    sends2 = {}
    sends3 = {}
    acks1 = {}
    acks2 = {}
    acks3 = {}
    t1 = 0.0
    total_l = 0
    total_pkt = 0
    avg_l = 0
    with open(trace) as f:
        for line in f:
            records = line.split(' ')
            eve_type = records[0]
            t = float(records[1])
            f_n = records[2]
            t_n = records[3]
            pkt_type = records[4]
            pkt_size = int(records[5])
            f_id = records[7]
            f_addr = records[8]
            t_addr = records[9]
            s_n = records[10]
            if f_id == '1':
                if eve_type == '-' and f_n == '0':
                    sends1.update({s_n: t})
                if eve_type == 'r' and t_n == '3':
                    acks1.update({s_n: t})
            if f_id == '2':
                if eve_type == '-' and f_n == '4':
                    sends2.update({s_n: t})
                if eve_type == 'r' and t_n == '5':
                    acks2.update({s_n: t})
            if f_id == '3':
                if eve_type == '-' and f_n == '4':
                    sends3.update({s_n: t})
                if eve_type == 'r' and t_n == '5':
                    acks3.update({s_n: t})                    
                    
            if t -  t1 <= stage:
                pass
            else:
                ack_s_n1 = set(acks1.viewkeys()).intersection(sends1.viewkeys())
                ack_s_n2 = set(acks2.viewkeys()).intersection(sends2.viewkeys())
                ack_s_n3 = set(acks3.viewkeys()).intersection(sends3.viewkeys())
                for s in ack_s_n1:
                    # calculate the latency time
                    latency = acks1[s] - sends1[s]
                    if latency > 0:
                        #print latency
                        total_l += latency
                        total_pkt += 1
                for s in ack_s_n2:
                    # calculate the latency time
                    latency = acks2[s] - sends2[s]
                    if latency > 0:
                        total_l += latency
                        total_pkt += 1
                for s in ack_s_n3:
                    # calculate the latency time
                    latency = acks3[s] - sends3[s]
                    if latency > 0:
                        total_l += latency
                        total_pkt += 1
                        
                if total_pkt == 0:
                    avg_l = 0
                else:
                    avg_l = float(total_l) / total_pkt * 1000
                con = str(t1) + ' ' + str(avg_l) + ' ' + '\n'
                f_w.write(con)
                t1 += stage
                total_l = 0
                total_pkt = 0
                acks = {}
                sends = {}
    f_w.close
def main():
    for queue_type in Queues:
        os.system('ns part2-2.ns ' + queue_type)
        time.sleep(4)
        print 'finished'
        calThroughput(queue_type, 1)
        calLatency(queue_type, 1)
    
if __name__ == '__main__':
    main()