#!/bin/bash

sudo tc qdisc del dev lo root

# WAN
sudo tc qdisc add dev lo root netem rate 9Mbps delay 36ms
for i in $(seq 1 1 5)
do
    python Scripts/resnet18_infra.py -R 64 -Z 3 -b 100000 > resnet18_infra_wan_$i
done
sudo tc qdisc del dev lo root

# WAN
sudo tc qdisc add dev lo root netem rate 9Mbps delay 36ms
for i in $(seq 1 1 5)
do
    python Scripts/resnet50_infra.py -R 64 -Z 3 -b 100000 > resnet50_infra_wan_$i
done
sudo tc qdisc del dev lo root

