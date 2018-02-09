set xlabel 'CBR'
set ylabel 'LossRate'
set term png

# draw loss rate
set output sprintf("pic/result1_1_%s_loss_rate.png", ARG1)
file = sprintf("data/result1_1_%s.dat", ARG1)
print file
set title ARG2
plot file using 1:2 smooth csplines title "Flow-1to4" with lines,\
     file using 1:3 smooth csplines title "Flow-5to6" with lines,\
     file using 1:4 smooth csplines title "Flow-2to3" with lines

# draw bandwidth
set title ARG2
set ylabel 'Bandwidth'
set output sprintf("pic/result1_1_%s_bandwidth.png", ARG1)
plot file using 1:5 smooth csplines title "Flow-1to4" with lines,\
     file using 1:6 smooth csplines title "Flow-5to6" with lines,\
     file using 1:7 smooth csplines title "Flow-2to3" with lines

 
