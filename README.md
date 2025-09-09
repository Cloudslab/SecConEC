# This is a draft of the README file for the project.

## Usage
1. Clone the repository.
2. Build component images using the provided Dockerfiles. `./containers/COMPONENT_NAME/Dockerfile` E.g.,
    ```
    ./containers/master/run-master.sh 
    [!] Hostname or enable overlay is required.
    Usage: ./containers/master/run-master.sh [-h hostname] [-r RemoteLogger hostname] [-t enable TLS or not] [-c in container or not] [-o enable overlay or not]
    ```
3. Use `run-COMPONENT_NAME.sh` scripts to start the components. `./containers/COMPONENT_NAME/run-COMPONENT_NAME.sh`

## Experiments
See "5.1. Experiment setup and sample applications" in the paper for details on the experiments conducted.
