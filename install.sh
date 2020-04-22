#!/usr/bin/env bash

NETHER_PATH=$HOME/.nether
rm -rf $NETHER_PATH
mkdir $NETHER_PATH
printf "export PATH=\"$PATH:${HOME}/.nether/bin\"" > $NETHER_PATH/env
cp -r ./src $NETHER_PATH/bin
mv $NETHER_PATH/bin/nether.py $NETHER_PATH/bin/nether
printf "To configure the current shell run:\n\e[1msource $NETHER_PATH/env\e[m\n"
