FROM python:3.8-buster

RUN pip install boto3==1.12.5

RUN apt update && \
    apt -y install vim ntp

# install sops
RUN wget -O sops.deb https://github.com/mozilla/sops/releases/download/v3.5.0/sops_3.5.0_amd64.deb && \
    dpkg -i sops.deb

# tell sops where to find the customer managed key (CMK) to encrypt/decrypt files
ENV SOPS_KMS_ARN ARN_OF_THE_CMK

# make sure your credentials allow you to use SOPS_KMS_ARN to encrypt/decrypt files
COPY ./credentials /root/.aws/

WORKDIR /secure_credentials
