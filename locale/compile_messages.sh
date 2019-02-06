#!/bin/bash

cd uk_UA/LC_MESSAGES/ && msgfmt messages.po -o messages.mo && cd ../../ 
echo $PWD
cd en/LC_MESSAGES/ && msgfmt messages.po -o messages.mo &&  cd ../../
echo $PWD
cd az_AZ/LC_MESSAGES/ && msgfmt messages.po -o messages.mo &&  cd ../../
echo $PWD

