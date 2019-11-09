# ConfiNet

ConfiNet is a command line application with useful networking tools such as port scanning, locating IP addresses, etc. To try it out, simply build the container, run the container, and you're off and running. 

## Instructions to Run
1. Upgrade *apt* and install Docker if you do not already have it installed on your machine.
```
sudo apt update 
sudo apt install docker.io
```

You might run into issues with connecting to the Docker daemon. You must alter permissions and start the service.
```
sudo groupadd docker
sudo usermod -aG docker $(whoami)
sudo service start docker
```

2. Build the Docker container by running the *build.sh* script located in the *scripts* folder.
```./build.sh```

3. Run the container by running the *run.sh* script located in the *scripts* folder.
```./run.sh```

## Commands

* scan - find open ports provided an IP address
* locate - find out location information given an IP address
* whoami - find out IP address about your machine
* meta - find out meta data about a file(s)
