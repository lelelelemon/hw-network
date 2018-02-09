import sys

VARIANTS = ['S', 'R']
Queues = ['DropTail', 'RED']
def calThroughput(tcp_type, queue_type, stage):
    trace = "trace/part2_1_" + tcp_type + "_" + queue_type+ ".trace"
    dat = "data/part2_1_" + tcp_type + "_" + queue_type + ".dat"
    f = open(dat, 'w+')
    t1 = 0
    total_recieved_bytes_0 = 0
    total_recieved_bytes_1 = 0
    with open(trace) as f:
        for line in f:
            records = line.split(' ')
            eve_type = records[0]
            t = records[1]
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
            if t - t1 <= stage:
                pass
            else:
                tp_0 = float(total_recieved_bytes_0) * 8 /stage/ 1000000
                tp_1 = float(total_recieved_bytes_1) * 8 /stage/ 1000000
                con = str(t1) + ' ' + str(tp_0) + str(tp_1) + '\n'
                f.write(con)
                t += stage
                total_recieved_bytes_0 = 0
                total_recieved_bytes_1 = 0
            f.close    
def main():
    print "s"
    
if __name__ == '__main__':
    main()