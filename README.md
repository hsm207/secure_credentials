# Introduction

This repository contains code to accompany my Medium blog post titled [How To Commit Your Cloud Credentials To Version Control Systems]().
It makes use of [sops](https://github.com/mozilla/sops) and AWS KMS (sops works with other cloud providers too).

# Usage

The [Dockerfile](Dockerfile) is meant to help newcomers to sops to quickly get started using it with AWS KMS.

To get started:
1. Create a customer managed key (CMK) in AWS CMK
2. Create an IAM user and assign it the permission to use the CMK for file encryption and decryption
2. Update line 13 in the [Dockerfile](Dockerfile) with the CMK's ARN
3. Update [credentials](credentials) with the credentials of the IAM user created in step 2
4. Execute:
     ```shell script
    docker build -t secure_credentials:dev . && \
    docker run -v $(pwd):/secure_credentials \
                --name secure_credentials \
                -it \
                --rm \
                secure_credentials:dev bash
    ```
   Follow along the blog post to learn how to encrypt and decrypt files using sops. 
