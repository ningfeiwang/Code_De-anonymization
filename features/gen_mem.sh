#!/bin/bash 


path=$(cd $(dirname $0); pwd)
files=$(ls $path)
for filename in $files
do
	echo $filename >> filename.txt
done
