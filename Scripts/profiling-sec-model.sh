echo 'Falcon'
python compile.py -R 64 -Q Falcon -C -K LTZ,TruncPr,Pow2,Reciprocal autograd_MPCFormer --profiling &
python compile.py -R 64 -Q Falcon -C -K LTZ,TruncPr,Pow2,Reciprocal autograd_resnet --profiling &
wait

echo 'ABY3'
python compile.py -R 64 -Q ABY3 -C -K LTZ,TruncPr autograd_resnet --profiling &
python compile.py -R 64 -Q ABY3 -C -K LTZ,TruncPr autograd_MPCFormer --profiling &
wait

echo 'SPDZ'
python compile.py -R 64 -Q SPDZ  autograd_resnet --profiling &
python compile.py -R 64 -Q SPDZ  autograd_MPCFormer --profiling &
wait

echo 'ABY'
python compile.py -R 64 -Q ABY -C -K LTZ,TruncPr autograd_resnet --profiling &
python compile.py -R 64 -Q ABY -C -K LTZ,TruncPr autograd_MPCFormer --profiling &
wait