set xlabel 'Time (s)'
set ylabel 'Throughput'
set term png

# draw loss rate
set output "pic/result2_1_throughput.png"

set style line 1 lc rgb '#0060ad' lt 1 lw 2 pi -1 ps 1.0
set style line 2 lc rgb '#dd181f' lt 9 lw 2 pi -1 ps 1.0
set style line 3 lc rgb '#29c524' lt 6 lw 2 pi -1 ps 1.0
set style line 4 lc rgb '#7D72F9' lt 7 lw 2 pi -1 ps 1.0
set style line 5 lc rgb '#000000' lt 8 lw 2 pi -1 ps 1.0

file1 = "data/part2_1_R_DropTail.dat"
file2 = "data/part2_1_R_RED.dat"
file3 = "data/part2_1_S_DropTail.dat"
file4 = "data/part2_1_S_RED.dat"

#print file
set title 'Throughtput-Reno'
f1 = "Reno DropTail"
f2 = "Reno RED"
f3 = "Sack DropTail"
f4 = "Sack RED"
t1 = 'TCP-DropTail'
t2 = 'CBR-DropTail'
t3 = 'TCP-RED'
t4 = 'CBR-RED'
set output sprintf("pic/part2_1_%s.png", "Reno")
plot file1 using 1:2 title t1 ls 1  with lines,\
     file1 using 1:3 title t2 ls 2 with lines,\
     file2 using 1:2 title t3 ls 3 with lines,\
     file2 using 1:3 title t4 ls 4 with lines
set title 'Throughput-SACK'

set output sprintf("pic/part2_1_%s.png", "SACK")
plot file3 using 1:2 title t1 ls 1 with lines,\
     file3 using 1:3 title t2 ls 2 with lines,\
     file4 using 1:2 title t3 ls 3 with lines,\
     file4 using 1:3 title t4 ls 4 with lines

 
