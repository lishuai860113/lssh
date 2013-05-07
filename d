#!/bin/bash
#这个脚本会一直输出时间,很easy.但是对于我是很有用的.呵呵

for (( ; ; ))
do
clear
stty icanon
date | awk '{print $4}'
stty -icanon
stty -echo
stty min 0
stty time 10
read  i
if [ "$i" == "q" ] 
then
stty icanon
stty echo
stty min 1
stty time 0
exit 0 
fi
done

