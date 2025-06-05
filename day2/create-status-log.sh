#!/bin/bash
dir=$(date '+%Y-%m-%d_%H-%M-%S')
mkdir "$dir"
cd "$dir" || exit 1
echo -e "User: $(whoami)\nUptime: $(uptime)\n" > log.txt

