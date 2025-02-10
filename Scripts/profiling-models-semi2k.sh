echo 'vgg-16'
for i in {1..1}; do
     python compile.py -R 64 -Q SEMI2K -C -K LTZ,TruncPr autograd_vgg_train_sgd_cifar10 --profiling > ./Data/vgg-16-SEMI2K$i.txt &
done
wait

echo 'resnet-50'
for i in {1..1}; do
      python compile.py -R 64 -Q SEMI2K -C -K LTZ,TruncPr autograd_resnet_training --profiling > ./Data/resnet-50-SEMI2K$i.txt &
done
wait