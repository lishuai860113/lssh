set term jpeg
set output "tmp/test.jpg"
set timefmt "%H:%M:%S"
set xdata time
plot "tmp/test.sar" using 1:2 with lines
