# Kubernetes Cluster Validation
** Install python requirements **

    source build/build.sh
 
 ** Enable Python Environment **

    source ~/kubevalenv/bin/activate

** Update configuration **
File to update:

    kubeval/conf/settings.yml

 1. Path for the Kubernetes cluster configuration file - to access the cluster-APIs.
 2. Path for the PDF file (Software description of the kubernetes cluster)
 3. Results path and filename (if required)

** Run Validator **

    cd kubeval
    ./k8svalidate

