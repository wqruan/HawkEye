#!/usr/bin/env bash

echo 'alexnet'
python compile.py -R 64 -Q ABY3 -C -K LTZ,TruncPr autograd_alexnet_train_sgd --profiling > ./Data/alexnet_train_sgd_aby3.txt &
python compile.py -R 64 -Q ABY3 -C -K LTZ,TruncPr autograd_alexnet_train_adam --profiling > ./Data/alexnet_train_adam_aby3.txt &
python compile.py -R 64 -Q ABY -C -K LTZ,TruncPr autograd_alexnet_train_sgd --profiling > ./Data/alexnet_train_sgd_aby.txt &
python compile.py -R 64 -Q ABY -C -K LTZ,TruncPr autograd_alexnet_train_adam --profiling > ./Data/alexnet_train_adam_aby.txt &
wait

echo 'lenet'
python compile.py -R 64 -Q ABY3 -C -K LTZ,TruncPr autograd_lenet_train_sgd --profiling > ./Data/autograd_lenet_train_sgd_aby3.txt &
python compile.py -R 64 -Q ABY3 -C -K LTZ,TruncPr autograd_lenet_train_adam --profiling > ./Data/autograd_lenet_train_adam_aby3.txt &
python compile.py -R 64 -Q ABY -C -K LTZ,TruncPr autograd_lenet_train_sgd --profiling > ./Data/autograd_lenet_train_sgd_aby.txt &
python compile.py -R 64 -Q ABY -C -K LTZ,TruncPr autograd_lenet_train_adam --profiling > ./Data/autograd_lenet_train_adam_aby.txt &
wait

echo 'vgg'
python compile.py -R 64 -Q ABY3 -C -K LTZ,TruncPr autograd_vgg_train_sgd --profiling > ./Data/autograd_vgg_train_sgd_aby3.txt &
python compile.py -R 64 -Q ABY3 -C -K LTZ,TruncPr autograd_vgg_train_adam --profiling > ./Data/autograd_vgg_train_adam_aby3.txt &
python compile.py -R 64 -Q ABY -C -K LTZ,TruncPr autograd_vgg_train_sgd --profiling > ./Data/autograd_vgg_train_sgd_aby.txt &
python compile.py -R 64 -Q ABY -C -K LTZ,TruncPr autograd_vgg_train_adam --profiling > ./Data/autograd_vgg_train_adam_aby.txt &
wait