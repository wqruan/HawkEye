#!/usr/bin/env bash

echo 'densenet'
for i in {1..5}; do
    python compile.py -R 60 -Q CryptFlow2 -C -K LTZ,TruncPr autograd_densenet --profiling > ./Data/densenet$i.txt &
done
wait

echo 'moblienet'
for i in {1..5}; do
    python compile.py -R 60 -Q CryptFlow2 -C -K LTZ,TruncPr autograd_mobilenetv3 --profiling > ./Data/mobilenet$i.txt &
done
wait

echo 'resnet'
for i in {1..5}; do
    python compile.py -R 60 -Q CryptFlow2 -C -K LTZ,TruncPr autograd_resnet --profiling > ./Data/resnet$i.txt &
done
wait

echo 'shufflenet'
for i in {1..5}; do
    python compile.py -R 60 -Q CryptFlow2 -C -K LTZ,TruncPr autograd_shufflenetv2 --profiling > ./Data/shufflenet$i.txt &
done
wait

echo 'mpcformer'
for i in {1..5}; do
    python compile.py -R 64 -Q MPCFormer -C -K exp_fx,EQZ,FPDiv,Reciprocal autograd_MPCFormer --profiling > ./Data/mpcformer$i.txt &
done
wait