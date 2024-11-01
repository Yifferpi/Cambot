#! /bin/sh

# Find the current directory
DIR=$(dirname $(realpath $0))

# Load the environment variables from .env file and run
eval $(cat $DIR/.env) $DIR/bot.py