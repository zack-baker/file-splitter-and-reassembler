#!/bin/bash

for (( i=0; i<=$2; i++));
do
	cat "$1_$i" >> "$1_assembled";
	
done

