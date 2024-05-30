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

FILES_TO_COPY=("virtbc.py" "virtbc")

# Copy the files
echo "Copying files from $SOURCE_DIR to $DEST_DIR:"
for FILE in $FILES_TO_COPY; do
  echo "Copying $FILE to $DEST_DIR"
  cp "$SOURCE_DIR/$FILE" "$DEST_DIR" && echo "Copied $FILE to $DEST_DIR" || echo "Failed to copy $FILE"
done

echo "All files setup successfully."

if ! python "$SOURCE_DIR/virtbc.py" --setup; then
  if ! python3 "$SOURCE_DIR/virtbc.py" --setup; then
    echo "Setup failed.."
  fi
fi
