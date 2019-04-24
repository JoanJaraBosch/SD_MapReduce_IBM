#Eliminem accions i els zips
ibmcloud fn action delete map_countingWords
ibmcloud fn action delete map_wordCount
ibmcloud fn action delete reduce_countingWords
ibmcloud fn action delete reduce_wordCount
rm *.zip
#Creem zips
cp map_countingWords.py __main__.py
zip -r map_counting.zip __main__.py cos_backend.py
cp map_wordCount.py __main__.py
zip -r map_word.zip __main__.py cos_backend.py
cp reduce_countingWords.py __main__.py
zip -r reduce_counting.zip __main__.py cos_backend.py
cp reduce_wordCount.py __main__.py
zip -r reduce_word.zip __main__.py cos_backend.py
#Amb els zips creats fem les accions
ibmcloud fn action create map_countingWords -t 150000 -m 2048 --kind python:3.6 map_counting.zip
ibmcloud fn action create map_wordCount -t 150000 -m 2048 --kind python:3.6 map_word.zip
ibmcloud fn action create reduce_countingWords -t 150000 -m 2048 --kind python:3.6 reduce_counting.zip
ibmcloud fn action create reduce_wordCount -t 150000 -m 2048 --kind python:3.6 reduce_word.zip

