#!/usr/bin/env bash

echo "Building Project..."
python3 setup.py sdist bdist_wheel

if [ $? -gt 0 ]; then
     echo "Failed to build project see additional output above."
else
    echo "Project Built Successfully!"
fi