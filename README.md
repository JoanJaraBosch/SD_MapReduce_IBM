# SD_MapReduce_IBM
Repository to do the mapreduce in ibmcloud.

## How Does it Works?

Executing the Makefile we create 4 actions (map_wordCount, reduce_wordCount, map_countingWord, reduce_countingWord) in our ibm_cloud.
Executing the orquestra.py will invoke the maps (as maps as you put it as a parameter). Then the maps will count words or count strings
and their accurrences. It will generate "x" files in our ibm_cloud. Finally, the orquestra will wait the maps to finish. Then, the
orquestra will invoke the reduce, that will merge the files and delete it making 2 files in our ibm_cloud and 2 files in our pc. The
information of the final files is the total of strings and a dictionary of strings and their accurrences.

## Installation

* First of all, we have to modify all the files to change "joanuni" to your ObjectStorage name.
* Secondly, you have to modify the .ibm_config file puting your keys.
* Then, you have to execute the Makefile (in linux).
* Finally, you have to execute python3 orquestra.py "file_name_cloud" "num_of_partitions"
```
python3 orquestra.py donQuijote.txt 10
```
