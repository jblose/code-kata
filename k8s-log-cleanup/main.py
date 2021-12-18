from kubernetes import client, config
import os
from os import listdir


dataDir = "/home/jblose"

config.load_kube_config()
v1 = client.CoreV1Api()
# Use default namespace
ret = v1.list_namespaced_pod(namespace="default")

listPods = []
# Gets List of Active Pods running on node
for i in ret.items:
    listPods.insert(0, i.metadata.name)

listPods.sort()
podDirs = listdir(dataDir)

for x in podDirs:
    if not listPods.__contains__(x):
        fullDelPath = dataDir + os.path.sep + x
        print("D: " + fullDelPath)
        os.rmdir(fullDelPath)
    else:
        fullDelPath = dataDir + os.path.sep + x
        print("K: " + fullDelPath)
