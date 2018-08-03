#!/bin/bash


# Check that 'inotifywait' is installed

if ! hash inotifywait 2>/dev/null
then
    echo "The 'inotifywait' command is not installed."
    echo
    echo "Ubuntu users run 'sudo apt-get install inotify-tools'"
    exit 1
fi

if ! hash sass 2>/dev/null
then
    echo "The 'sass' compiler is not installed."
    echo
    echo "Ubuntu users run 'sudo apt-get install ruby-sass'"
    echo "Mac OS X users run 'sudo port install rb19-sass'"
    exit 1
fi


SCRIPT_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


# Command loop
while true;
do
    # Run commands
    echo "Running sass compiler"
    sass --no-cache --scss --update --style nested --sourcemap=none $SCRIPT_FOLDER

    # Block until file system changed under current working directory
    echo "Completed. Waiting for changes."
    inotifywait -qq -e create,delete,modify,move -r $SCRIPT_FOLDER
done
