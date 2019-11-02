FROM alpine:latest 

WORKDIR ./
COPY myapp/* ./

RUN mkdir queue && mkdir processed && mkdir output
RUN apk update
RUN apk add --no-cache python3
RUN apk add --no-cache handbrake --repository="http://dl-cdn.alpinelinux.org/alpine/edge/testing"  

ENTRYPOINT ["python3", "handbrake.py"]
