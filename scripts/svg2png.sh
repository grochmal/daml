#!/bin/sh

FPATH="$1"
FILE=`basename "$FPATH"`
FDIR=`dirname "$FPATH"`
BASE=`basename "$FILE" .svg`
EXT="${FILE##*.}"
NEWF="$FDIR/$BASE.png"

if test "z$EXT" != "zsvg" -o ! -r "$FPATH"; then
    echo "Usage $0 <image.svg>"
    echo
else
    echo "$FPATH -> $NEWF"
    inkscape "$FPATH" -e "$NEWF" --without-gui
    optipng -strip all "$NEWF"
    du -sh "$NEWF"
fi
