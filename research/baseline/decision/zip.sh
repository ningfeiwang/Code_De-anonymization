#!/bin/bash 

rm -rf testingzip
rm -rf trainingzip
mkdir testingzip
mkdir trainingzip

# path=$(cd $(dirname $0); pwd)
# files=$(ls $path)
# for filename in $files
# do
# 	echo $filename >> filename.txt
# done
for file_test in ./testing/*
do
	tmp=${file_test%%_*}
	temp=${tmp:11}
	cmd="zip ./testingzip/"${file_test:10}".zip ${file_test} "
	echo $cmd
	eval $cmd
	# break
done

for file_train in ./training/*
do
	tmp=${file_train%%_*}
	temp=${tmp:12}
	cmd="zip ./trainingzip/"${file_train:10}".zip ${file_train}"
	echo $cmd
	eval $cmd
	# break
done