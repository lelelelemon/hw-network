set xlabel 'CBR'
set ylabel 'LossRate'
set term png

set style line 1 lt 2 lc rgb "red" lw 3
set style line 2 lt 2 lc rgb "orange" lw 2
set style line 3 lt 2 lc rgb "yellow" lw 3
set style line 4 lt 2 lc rgb "green" lw 2

# draw loss rate
set output sprintf("pic/result1_1_%s_loss_rate.png", ARG1)
file = sprintf("data/result1_1_%s.dat", ARG1)
print file
set title ARG2
f1 = sprintf("%s N1 to N4", ARG3)
f2 = sprintf("%s N5 to N6", ARG4)
plot file using 1:2  title f1 ls 1 with line, \
     file using 1:3  title f2 ls 2 with lines
#     file using 1:4 smooth csplines title "Flow-2to3" with lines

# draw bandwidth
set title ARG2
set ylabel 'Bandwidth'
set output sprintf("pic/result1_1_%s_bandwidth.png", ARG1)
plot file using 1:5  title f1 ls 1 with  lines,\
     file using 1:6  title f2 ls 2 with  lines
#     file using 1:7 smooth csplines title "Flow-2to3" with lines

 
