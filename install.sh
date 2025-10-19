#!/bin/bash

echo "Installing BubbleLan..."

# creating symbolic link
INSTALL_DIR="/usr/local/bin"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d "$INSTALL_DIR" ]; then
    echo "Creating $INSTALL_DIR..."
    sudo mkdir -p "$INSTALL_DIR"
fi

echo "Creating symbolic link..."
sudo ln -sf "$SCRIPT_DIR/bubblelan" "$INSTALL_DIR/bubblelan"

if [ $? -eq 0 ]; then
    echo "BubbleLan installed successfully!"
    echo ""
    echo "You can now use 'bubblelan' command anywhere:"
    echo "  bubblelan                 # Start REPL"
    echo "  bubblelan script.bub      # Run a .bub file"
    echo ""
    echo "Try it: bubblelan examples/hello.bub"
else
    echo "Installation failed. You may need sudo permissions."
    exit 1
fi
