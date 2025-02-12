#!/usr/bin/env bash

echo 'resnet32'
for i in {1..1}; do
     python compile.py -R 64 -Q Delphi -C -K LTZ,TruncPr,conv2d --modulus 43,43,44,44,44 autograd_resnet_32_dephi > ./Data/resnet32-Delphi$i.txt &
done
wait

echo 'minionn'
for i in {1..1}; do
      python compile.py -R 64 -Q Delphi -C -K LTZ,TruncPr,conv2d --modulus 43,43,44,44,44 autograd_minionn --profiling > ./Data/minionn-Delphi$i.txt &
done
wait
