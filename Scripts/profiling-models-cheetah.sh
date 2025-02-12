#!/usr/bin/env bash

echo 'resnet32'
for i in {1..1}; do
     python compile.py -R 64 -Q Cheetah -C -K LTZ,TruncPr --modulus 59,55,49,45 autograd_resnet_32_dephi --profiling > ./Data/resnet32-Cheetah$i.txt &
done
wait

echo 'minionn'
for i in {1..1}; do
   python compile.py -R 64 -Q Cheetah -C -K LTZ,TruncPr --modulus 59,55,49,45 autograd_minionn --profiling > ./Data/minionn-Cheetah$i.txt &
done
wait
