#!/usr/bin/env sh

OUTPUT=./train_set.vec
INFO_FILE=./info.dat
BG_FILE=./bg.txt
NUM=472
WEIGHT=18
HIGHT=18

opencv_createsamples \
    -vec $OUTPUT \
    -info $INFO_FILE \
    -bg $BG_FILE \
    -num $NUM \
    -show \
    -w $WEIGHT \
    -h $HIGHT \
