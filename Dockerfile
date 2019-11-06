FROM alpine:latest

WORKDIR ./

RUN mkdir queue && mkdir processed && mkdir output
RUN apk update
RUN apk add --no-cache python3
RUN apk add --no-cache handbrake --repository="http://dl-cdn.alpinelinux.org/alpine/edge/testing"
COPY myapp/* ./


ENTRYPOINT ["python3", "handbrake.py"]
