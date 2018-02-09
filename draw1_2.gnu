set xlabel 'CBR'
set ylabel 'LossRate'
set term png

# draw loss rate
set output "pic/result1_2_loss_rate.png"

set style line 1 lc rgb '#0060ad' lt 1 lw 2 pi -1 ps 1.0
set style line 2 lc rgb '#dd181f' lt 9 lw 2 pi -1 ps 1.0
set style line 3 lc rgb '#29c524' lt 6 lw 2 pi -1 ps 1.0
set style line 4 lc rgb '#7D72F9' lt 7 lw 2 pi -1 ps 1.0
set style line 5 lc rgb '#000000' lt 8 lw 2 pi -1 ps 1.0

file1 = "data/result1_2_N.dat"
file2 = "data/result1_2_R.dat"
file3 = "data/result1_2_V.dat"
#print file
set title 'Loss Rate'
f1 = "Reno N1 to N4"
f2 = "NewReno N1 to N4"
f3 = "Vegas N1 to N4"
plot file1 using 1:2 title f1 ls 1  with lines,\
     file2 using 1:2 title f2 ls 2 with lines,\
     file3 using 1:2 title f3 ls 3 with lines
# draw bandwidth
set title 'Bandwidth'
set ylabel 'Bandwidth'
set output "pic/result1_2_bandwidth.png"

plot file1 using 1:5  title f1 ls 1 with lines,\
     file2 using 1:5  title f2 ls 2  with lines,\
     file3 using 1:5  title f3 ls 3 with lines

 
