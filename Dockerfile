FROM ubuntu

RUN apt -y update && \
    apt -y install whois python3-pip && \
    pip3 install ip2geotools

# COPY /opt/confinet 

WORKDIR /opt/confinet

ENTRYPOINT ["/bin/bash"]