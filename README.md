# Hawkeye

This README file provides instructions for reproducing the experimental results in the paper "HawkEye: Statically and Accurately Profiling the Communication Cost of Models in Multi-party Learning" (Usenix Security 2025).

We thank all anonymous reviewers for their insightful comments, which have significantly contributed to the improvement of this artifact.

System Requirements: Unless specified differently, the evaluations in this README file can be conducted on a machine with 4 cores and 64 GB of RAM.


## Package structure
This repository has the following components:  
- **Compiler**: The main implementation of HawkEye's static communication cost profiling method and autograd library.
- **Programs**: The model files (Programs/Source) and compiled bytecodes.
- **Scripts**: The scripts used to reproduce the experimental results in the paper.
- **Other folders**: The external components from [MP-SPDZ](https://github.com/data61/MP-SPDZ), which are necessary to reproduce the experimental results in Table 5. More information about these folders can be found in the [official documentation of MP-SPDZ](https://mp-spdz.readthedocs.io/en/latest/).

## Build the environment
```
virtualenv venv --python 3.8
source venv/bin/activate
pip install -r requirements.txt
mkdir Data
cd Programs
mkdir Profiling-data
cd ../
```


## Accuracy of HawkEye 
(Table 1, Table 2, Table 6, Table 7, Table 8, Table 9, Figure 6, and Figure 7)

### Table 1, Table 2, Figure 6, and Figure 7
After running the following script, `Data/modelname-i.txt` would contain the profiling results from HawkEye in Table 1, Table 2, Figure 6, and Figure 7.

```
chmod +x Scripts/profiling-models.sh
./Scripts/profiling-models.sh
```
The above commands might take about one hour. The profiling results from CrypTen can be obtained by the following steps: (1) Downloading the codes stored in  https://github.com/wqruan/MPCFormer-HawkEye. (2) Following the instructions in README-HawkEye.md of source codes.


### Table 6, Table 7 and Table 8
After running the following script, `Data/modelname-Delphi1.txt` and `Data/modelname-Cheetah1.txt` would contain the profiling results from HawkEye in Table 6, Table 7, and Table 8.

```
chmod +x Scripts/profiling-models-delphi.sh
./Scripts/profiling-models-delphi.sh
chmod +x Scripts/profiling-models-cheetah.sh
./Scripts/profiling-models-cheetah.sh
```
It takes about five minutes. The profiling results from Delphi can be obtained by the following steps: (1) Downloading the codes stored in https://github.com/yNotAVAILABLEa/Delphi-HawkEye. (2) Following the instructions in README-HawkEye.md of source codes.

### Table 9
After running the following script, `Data/modelname-SEMI2K1.txt` will contain the profiling results from HawkEye in Table 9.

```
chmod +x Scripts/profiling-models-semi2k.sh
./Scripts/profiling-models-semi2k.sh
```
It takes about ten minutes. Note that we manually construct many models with a single layer to obtain the profiling results from SecretFlow-SEMI2K. The reproduction of the process would require a large amount of time. Therefore, we omit it in this documentation.

## Efficiency of HawkEye 
(Table 3)

After running the following script, the time of total profiling and block tree analysis for five secure model inference processes will be shown in the terminal.

```
chmod +x Scripts/profiling-models.sh
Scripts/profiling-models.sh
python Scripts/profiling-models.py
```
The above commands might take about one hour.  The following steps can obtain the running time of CrypTen: (1) Downloading the codes stored in https://github.com/wqruan/MPCFormer-HawkEye. (2) Following the instructions in README-HawkEye.md of source codes.


## Impact of security models
(Figure 8)

After running the following script, the `./protol_profiling.png` will show the model communication profiling results on MPL frameworks with different security models
```
chmod +x Scripts/profiling-sec-model.sh
Scripts/profiling-sec-model.sh
python Scripts/profiling-sec-model.py
```
The above commands might take about one hour.


## Choice of optimizers 
(Table 4)

After running the following script, `Data/modelname_train_sgd.txt` would contain the communication cost profiling results of the secure model training process with SGD, `Data/modelname_train_adam.txt` would contain the communication cost profiling results of the secure model training process with Adam.
```
chmod +x Scripts/profiling-opt.sh
Scripts/profiling-opt.sh
```
The above commands might take about half an hour.


## Computational graph optimization
(Table 5)



### Prepare environment
```
sudo apt-get install automake build-essential cmake git libboost-dev libboost-thread-dev libntl-dev libsodium-dev libssl-dev libtool m4  texinfo yasm
make -j 8 tldr
make -j 8 replicated-ring-party.x
make -j 8 Fake-Offline.x
chmod +x Scripts/setup-ssl.sh 
chmod +x Scripts/setup-online.sh
Scripts/setup-ssl.sh 3
Scripts/setup-online.sh 3 64
```

### Run experiments
After running the following script, you can run '' to parse the running results. After running 'python Scripts/resnet_view.py,' the terminal would show the experimental results in Table 5.
```
chmod +x Scripts/resnet-opt.sh
chmod +x Scripts/ring.sh
Scripts/resnet-opt.sh
```
The command "Scripts/resnet-opt.sh" may take more than one day. You can run 'nohup Scripts/resnet-opt.sh &' rather than 'Scripts/resnet-opt.sh' to run the experiment in the background.

### retrieve results

```
python Scripts/resnet_view.py
```
