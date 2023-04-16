#!/usr/bin/env bash

pushd quickstart
hugo
popd

pushd k8s
./deploy.sh
popd

pushd quickstart
./deploy.sh
popd