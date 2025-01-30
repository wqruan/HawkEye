# Hawkeye

This README file provides instructions for reproducing the experimental results in the paper "HawkEye: Statically and Accurately Profiling the Communication Cost of Models in Multi-party Learning" (Usenix Security 2025).

We thank all anonymous reviewers for their insightful comments, which have significantly contributed to the improvement of this artifact.

System Requirements: Unless specified differently, the evaluations in this README file can be conducted on a machine with 4 cores and 64 GB of RAM.


## Build the envirenment
```
virtualenv venv --python 3.8
source ../venv/bin/activate
pip install -r requirements.txt
mkdir Data
```


## Accuracy of HawkEye (Table 2, Table 3)

After runningthe following script, `Data/modelname-i.txt` would contain the profiling results from HawkEye in Table 2 and Table 3.

```
chmod +x Scripts/profiling-models.sh
./Scripts/profiling-models.sh
```

## Efficiency of HawkEye (Table 4)

After running the following script, the time of total profiling and block tree analysis for five secure model inference processes would be shown in the terminal

```
chmod +x Scripts/profiling-models.sh
Scripts/profiling-models.sh
python Scripts/profiling-models.py
```



## Performance of security model (Figure 5)

After running the following script, the `./protol_profiling.png` will show the model communication profiling results on MPL frameworks with different security models
```
chmod +x Scripts/profiling-sec-model.sh
Scripts/profiling-sec-model.sh
python Scripts/profiling-sec-model.py
```

## Choice of optimizers (Table 5)

After running the following script, `Data/modelname_train_sgd.txt` would contain the communication cost profiling results of secure model training process with SGD, `Data/modelname_train_adam.txt` would contain the communication cost profiling results of secure model training process with Adam.
```
chmod +x Scripts/profiling-opt.sh
Scripts/profiling-opt.sh
```

## Accuracy of HawkEye (Table 7, Table 8)

After runningthe following script, `Data/modelname-Delphi1.txt` and `Data/modelname-Cheetah1.txt` would contain the profiling results from HawkEye in Table 7 and Table 8.

```
chmod +x Scripts/profiling-models-delphi.sh
./Scripts/profiling-models-delphi.sh
```

## Practical application of HawkEye (Table 9)

After runningthe following script, `resnet18_infra_wan_i.txt` and `resnet50_infra_wan_i.txt` would contain the profiling results from HawkEye in Table 9.

```
chmod +x Scripts/profiling-models-cheetah.sh
./Scripts/profiling-models-cheetah.sh
```

## 
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

```
chmod +x Scripts/resnet-opt.sh
chmod +x Scripts/ring.sh
Scripts/resnet-opt.sh
python Scripts/resnet_view.py
```
The command "Scripts/resnet-opt.sh" may take more than one day. You can run 'nohup Scripts/resnet-opt.sh &' rather than 'Scripts/resnet-opt.sh' to run the experiment in.the background.
