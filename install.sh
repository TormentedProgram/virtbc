#!/bin/bash

# Get the directory where this bash script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Define the source directory containing the scripts to move
SOURCE_DIR="$SCRIPT_DIR/scripts"

# Define the destination directory
DEST_DIR="/usr/local/bin"

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: Source directory $SOURCE_DIR does not exist."
  exit 1
fi

# Find the first two files in the source directory
FILES_TO_COPY=$(ls "$SOURCE_DIR" 2>/dev/null | head -n 2)

# Check if there are at least two files to copy
if [ $(echo "$FILES_TO_COPY" | wc -l) -lt 2 ]; then
  echo "Error: Not enough files to copy in $SOURCE_DIR."
  exit 1
fi

# Copy the files
echo "Copying files from $SOURCE_DIR to $DEST_DIR:"
for FILE in $FILES_TO_COPY; do
  echo "Copying $FILE to $DEST_DIR"
  cp "$SOURCE_DIR/$FILE" "$DEST_DIR" && echo "Copied $FILE to $DEST_DIR" || echo "Failed to copy $FILE"
done

# Check if all files were copied successfully
if [ $(ls "$DEST_DIR" 2>/dev/null | wc -l) -ge 2 ]; then
  echo "All files setup successfully."
else
  echo "Error: Some files could not be copied."
fi

python3 $SOURCE_DIR/virtbc.py --setup
