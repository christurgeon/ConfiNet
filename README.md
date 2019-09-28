# ConfiNet

ConfiNet is a command line application with useful networking tools such as port scanning, locating IP addresses, etc. It provides a wrapper to tools such as *whois*. To try it out, simply build the container, run the container, and you're off and running. 

# Instructions to Run
1. Upgrade *apt* and install Docker if you do not already have it installed on your machine.
```
sudo apt update 
sudo apt install docker.io
```

You might run into issues with connecting to the Docker daemon. You must alter permissionsand start the service.
```
sudo groupadd docker
sudo usermod -aG docker $(whoami)
sudo service start docker
```

2. Build the Docker container by running the *build.sh* script located in the *scripts* folder.
```./build.sh```

3. Run the container by running the *run.sh* script located in the *scripts* folder.
```./run.sh```