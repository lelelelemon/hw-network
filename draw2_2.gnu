set xlabel 'Time (s)'
set ylabel 'Bandwidth'
set term png

# draw loss rate
set output "pic/result2_2_throughput.png"

set style line 1 lc rgb '#0060ad' lt 1 lw 2 pi -1 ps 1.0
set style line 2 lc rgb '#dd181f' lt 9 lw 2 pi -1 ps 1.0
set style line 3 lc rgb '#29c524' lt 6 lw 2 pi -1 ps 1.0
set style line 4 lc rgb '#7D72F9' lt 7 lw 2 pi -1 ps 1.0
set style line 5 lc rgb '#000000' lt 8 lw 2 pi -1 ps 1.0
set style line 6 lc rgb '#090200' lt 8 lw 2 pi -1 ps 1.0

file1 = "data/part2_2_DropTail.dat"
file2 = "data/part2_2_RED.dat"
file3 = "data/part2_2_DropTail_l.dat"
file4 = "data/part2_2_RED_l.dat"

#print file
set title 'Bandwidth'
f1 = "N1-N4 DropTail"
f2 = "N5-N6 DropTail"
f3 = "N7-N8 DropTail"
f4 = "N1-N4 RED"
f5 = "N5-N6 RED"
f6 = "N7-N8 RED"
plot file1 using 1:2 title f1 ls 1 with lines,\
     file1 using 1:3 title f2 ls 2 with lines,\
     file1 using 1:4 title f3 ls 3 with lines,\
     file2 using 1:2 title f4 ls 4 with lines,\
     file2 using 1:3 title f5 ls 5 with lines,\
     file2 using 1:4 title f6 ls 6 with lines
# draw bandwidth
set title 'Latency'
set ylabel 'Latency'
set output "pic/result2_2_latency.png"


plot file3 using 1:2 title f1 ls 1 with lines,\
     file3 using 1:3 title f2 ls 2 with lines,\
     file3 using 1:4 title f3 ls 3 with lines,\
     file4 using 1:2 title f4 ls 4 with lines,\
     file4 using 1:3 title f5 ls 5 with lines,\
     file4 using 1:4 title f6 ls 6 with lines
 
