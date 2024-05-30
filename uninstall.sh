#!/bin/bash

# Define the files that were copied from the previous script
COPIED_FILES=(
    "virtbc"
    "virtbc.py"
)

# Define the destination directory
DEST_DIR="/usr/local/bin"

# Check if each file exists in the destination directory and delete if present
for FILE in "${COPIED_FILES[@]}"; do
    if [ -f "$DEST_DIR/$FILE" ]; then
        echo "Deleting $FILE from $DEST_DIR"
        rm "$DEST_DIR/$FILE" && echo "Deleted $FILE from $DEST_DIR" || echo "Failed to delete $FILE"
    else
        echo "File $FILE not found in $DEST_DIR"
    fi
done

CONFIG_DIR="$HOME/.config/virtbc"

# Check if the directory exists and delete if present
if [ -d "$CONFIG_DIR" ]; then
    echo "Deleting $CONFIG_DIR"
    rm -rf "$CONFIG_DIR" && echo "Deleted $CONFIG_DIR" || echo "Failed to delete $CONFIG_DIR"
else
    echo "Directory $CONFIG_DIR not found"
fi

# Find the .bashrc file in the home directory
BASHRC_FILE="$HOME/.bashrc"

if [ -f "$BASHRC_FILE" ]; then
    if grep -q '^#virtbc implementation' "$BASHRC_FILE"; then
        sed -i '/^$/,$ { /^$/ { N; /\n#virtbc implementation.*$/ { N; d } } }' "$BASHRC_FILE" && echo "Removed virtbc implementation from $BASHRC_FILE" || echo "Failed to remove virtbc implementation from $BASHRC_FILE"
    else
        echo "No virtbc implementation found in $BASHRC_FILE"
    fi
else
    echo "File $BASHRC_FILE not found"
fi

echo "Successfully uninstalled!"