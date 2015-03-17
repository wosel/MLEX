#!/bin/bash

dataLen=`cat adult.data | wc -l`
dataLenOut=$((dataLen-1))

head -n $dataLenOut adult.data > adult.data.sanitized;

testLen=`cat adult.test | wc -l`
testLenHead=$((testLen-1))
testLenTail=$((testLen-2))

head -n $testLenHead adult.data > adult.test.tmp;
tail -n $testLenTail adult.test.tmp > adult.test.sanitized;
sed -i .backup 's/.//g' adult.test.sanitized;

rm -f adult.test.tmp adult.test.sanitized.backup

