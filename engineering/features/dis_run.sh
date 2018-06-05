#!/bin/bash 

rm -rf testingdis
rm -rf trainingdis
mkdir testingdis
mkdir trainingdis

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
	cmd="nohup python -m dis "${file_test}" < ./sample_input/"${temp}".txt > ./testingdis/"${file_test:10}".txt 2>&1 &"
	echo $cmd
	eval $cmd
	# break
done

for file_train in ./training/*
do
	tmp=${file_train%%_*}
	temp=${tmp:12}
	cmd="nohup python -m dis "${file_train}" < ./sample_input/"${temp}".txt > ./trainingdis/"${file_train:11}".txt 2>&1 &"
	echo $cmd
	eval $cmd
	# break
done