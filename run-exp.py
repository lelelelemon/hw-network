import sys
import os
import time

CBRS = [1,2,3,4,5,6,7,8,9,10]

def getLossRate(ty, cbr_rate, ex, f0='1', f1='2', f2='6',f1_type='tcp', st = 2.0, su = 0, et = 6.0, eu = 8.0):
	ts = ty.split(' ')
	tr_file = "trace/" + ex +  "_" + ts[0] + "_" + ts[1] + "_" + str(cbr_rate) + ".trace"
	start_tcp = st
	end_tcp_0  = et
	end_tcp_1 =  et
	start_udp = su
	end_udp = eu
	total_sent_0 = 0
	total_received_0 = 0
	total_sent_1 = 0
	total_received_1 = 0
	total_sent_cbr = 0
	total_received_cbr = 0
	total_received_bytes_0 = 0
	total_received_bytes_1 = 0
	total_received_bytes_cbr = 0
	with open(tr_file) as f:
		for line in f:
			record = line.split(' ')
			eve_type = record[0]
			eve_time = float(record[1])
			source = record[2]
			sink = record[3]
			pkt_type = record[4]
			pkt_size = int(record[5])
			flow_id = record[7]
			source_add = record[8]
			sink_add = record[9]
			seq_num = record[10]
			if flow_id == f0: 
				if eve_type == '-' and source == '0':
					total_sent_0 += 1
				if eve_type == 'r' and sink == '0' and pkt_type == 'ack':
					total_received_0 += 1
				if eve_type == 'r' and sink == '3':
					total_received_bytes_0 += pkt_size
					end_tcp_0 = eve_time			
			if flow_id == f1:
				if f1_type == 'tcp':
					if eve_type == '-' and source == '4':
						total_sent_1 += 1
					if eve_type == 'r' and sink == '4' and pkt_type == 'ack':
						total_received_1 += 1
					if eve_type == 'r' and sink == '5':
						total_received_bytes_1 += pkt_size
						end_tcp_1 = eve_time
				if f1_type == 'cbr':
	                                if eve_type == '-' and source == '4':
        	                                total_sent_1 += 1
                	                if eve_type == 'r' and sink == '5' and pkt_type == 'cbr':
                        	                total_received_1 += 1
                                	        total_received_bytes_1 += pkt_size
						#print 'pakcet size', pkt_size, total_received_bytes_1

			if flow_id == f2:
				if eve_type == '-' and source == '1':
					total_sent_cbr += 1
				if eve_type == 'r' and sink == '2' and pkt_type == 'cbr':
					total_received_cbr += 1
					total_received_bytes_cbr += pkt_size
	loss_rate_0 = 0
	loss_rate_1 = 1
	loss_rate_cbr = 0
	if total_sent_0 == 0:
		loss_rate_0 = 0
	else:
		loss_rate_0 = float (total_sent_0 - total_received_0)/ total_sent_0 * 100	
				
	if total_sent_1 == 0:
                loss_rate_1 = 0
        else:
                loss_rate_1 = float (total_sent_1 - total_received_1)/ total_sent_1 * 100
	if total_sent_cbr == 0:
		loss_rate_cbr = 0
	else:
		loss_rate_cbr = float (total_sent_cbr - total_received_cbr)/total_sent_cbr * 100
	bandwidth_0 = float(total_received_bytes_0 * 8) / (end_tcp_0 - start_tcp) / 1000000
	bandwidth_1 = float(total_received_bytes_1 * 8) / (end_tcp_1 - start_tcp) / 1000000
	bandwidth_cbr = float(total_received_bytes_cbr * 8) / (end_udp - start_udp) / 1000000
	print cbr_rate, loss_rate_0, loss_rate_1, loss_rate_cbr, bandwidth_0, bandwidth_1, bandwidth_cbr
	return [cbr_rate, loss_rate_0, loss_rate_1, loss_rate_cbr, bandwidth_0, bandwidth_1, bandwidth_cbr]
def exp1_1():
	tys = ['R R' , 'N R', 'V V', 'N V']
	titles = ['Reno\/Reno', 'NewReno\/Reno', 'Vegas\/Vegas', 'NewReno\/Vegas']
	cbr_rates = CBRS
	for ty in tys:
		print ty
		ts = ty.split(' ')
		title = titles[tys.index(ty)]
		f = open('data/result1_1_'+ ts[0] +'_' + ts[1] + '.dat','w+')
		f.write(ty + "\n")
		for cbr_rate in cbr_rates:
			os.system('ns part1-1.ns ' + ty + ' ' + str(cbr_rate))	
			time.sleep(3)
			#print ty, cbr_rate
			d = getLossRate(ty, cbr_rate, 'part1_1')
			f.write(' '.join(str(e) for e in d))
			f.write('\n')
		f.close	
	for ty in tys:
		ts = ty.split(' ')
		title = titles[tys.index(ty)]		
		cmd = 'gnuplot -c draw.gnu' + ' ' + ts[0] + '_' + ts[1]  + ' ' +  title 
		#print cmd
		#os.system(cmd)
def exp1_2():
	tys = ['R R', 'N R', 'V V']
	titles = ['Reno', 'NewReno', 'Vegas']
	cbr_rates = CBRS
	for ty in tys:
                print ty
                ts = ty.split(' ')
		title = titles[tys.index(ty)]
                f = open('data/result1_2_'+ ts[0] + '.dat','w+')	
                f.write(ty + "\n")
		for cbr_rate in cbr_rates:
                        os.system('ns part1-2.ns ' + ty + ' ' + str(cbr_rate))
                        time.sleep(3)
                        #print ty, cbr_rate
                        d = getLossRate(ty, cbr_rate, 'part1_2')
			f.write(' '.join(str(e) for e in d))
                        f.write('\n')
		f.close
		time.sleep(2)
		#os.system('gnuplot -c draw1_2.gnu' + ' ' + ts[0] + ' ' +  title )
def exp2_1():
        tys = ['R drop', 'R red', 'S drop', 'S red']
        cbr_rates = CBRS
        for ty in tys:
                print ty
		loss = ty.split(' ')[1]
                for cbr_rate in cbr_rates:
                        os.system('ns part2-1-' + loss + '.ns ' + ty + ' ' + str(cbr_rate))
                        time.sleep(3)
                        #print ty, cbr_rate
                        getLossRate(ty, cbr_rate, 'part2_1', '13', '15', '0', 'cbr', 0, 10, 20, 20)

def exp2_2():
	print '2_2'
def main():
	a = sys.argv[1]
	if a == '1_1':
		exp1_1()
	if a == '1_2':
		exp1_2()
	if a == '2_1':
		exp2_1()
	if a == '2_2':
		exp2_2()
if __name__ == '__main__':
	main()
