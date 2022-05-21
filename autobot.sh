#!/bin/sh

cd app && docker build -t deltacrayo/y42 --build-arg build_date="$(date +%s)" . && cd ../ops/ && kubectl apply -f deploy.yaml

