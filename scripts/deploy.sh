#!/usr/bin/env bash

echo "Starting Deploy"

python3 -m twine upload --repository testpypi dist/*

if [ $? -gt 0 ]; then
     echo "Failed to deploy project see additional output above."
else
    echo "Project deployed successfully!"
fi