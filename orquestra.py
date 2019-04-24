import ibm_cf_connector
import yaml
import sys
import cos_backend
from time import time
import json

with open('.ibm-cloud_config', 'r') as config_file:
	configu = yaml.safe_load(config_file)

if(len(sys.argv) >= 3):
	print("Escolleix si vols fer el wordCount o el countingWords: (wordCount(1)/countingWords(2))")
	opcio = int(input())
	if(opcio==1 or opcio==2):
		file_name=sys.argv[1]
		n_particions = int(sys.argv[2])
		cos=cos_backend.cos_backend(configu['ibm_cos'])
		tamany_fitxer=int(cos.head_object('joanuni',file_name))
		provemFunc = ibm_cf_connector.CloudFunctions(configu['ibm_cf'])
		diccionari={}
		diccionari["config"]= configu['ibm_cos']
		diccionari["file_name"]= file_name
		diccionari["particions"]=n_particions
		actual=0
		aux=int(tamany_fitxer/n_particions)
		seguent=aux
		modul = tamany_fitxer%n_particions
		i=0
		fitxer=0
		instanteInicial = time()
		while(i<n_particions):
			tamany_agafar ="bytes="+str(actual)+"-"+str(seguent)
			if(n_particions-i == 1):
				seguent+=modul
				tamany_agafar ="bytes="+str(actual)+"-"+str(seguent)
			diccionari["size"]=tamany_agafar
			diccionari["particio"]=i+1
			if(opcio==2):
				provemFunc.invoke("map_countingWords", diccionari)
			else:
				provemFunc.invoke("map_wordCount", diccionari)
			actual=seguent
			seguent+=aux
			i+=1	
		if(opcio==2):
			provemFunc.invoke("reduce_countingWords", diccionari)
		else:
			provemFunc.invoke("reduce_wordCount", diccionari)
		i=0
		while(i==0):
			if(opcio==2):
				dades1=cos.get_object("joanuni","reduce_countingWord"+file_name.replace(".txt","")+".txt")
				if(dades1 != "No file"):
					i+=1
					with open('reduce_countingWord'+file_name.replace(".txt","")+'.txt', 'w') as reduce_counting:
						reduce_counting.write(dades1.decode('unicode-escape'))
					elapsedtime=time()-instanteInicial
					print("Ha tardat %.10f segons en fer el MapReduce del countingWords." % elapsedtime)
			else:
				dades2=cos.get_object("joanuni","reduce_wordCount"+file_name.replace(".txt","")+".txt")
				if(dades2 != "No file"):
					i+=1
					with open('reduce_wordCount'+file_name.replace(".txt","")+'.txt', 'w') as reduce_wordCount:
						reduce_wordCount.write(dades2.decode('unicode-escape'))
					elapsedtime=time()-instanteInicial
					print("Ha tardat %.10f segons en fer el MapReduce del wordCount." % elapsedtime)
			
else:
	print("Error: et falten el nombre de particions que voldras pel fitxer o el nom del fitxer o ambdues.")
