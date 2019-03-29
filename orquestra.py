import ibm_cf_connector
import yaml
import sys
import cos_backend

with open('.ibm-cloud_config', 'r') as config_file:
	configu = yaml.safe_load(config_file)

if(len(sys.argv) >= 3):
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
	while(i<n_particions):
		tamany_agafar ="bytes="+str(actual)+"-"+str(seguent)
		if(n_particions-i == 1):
			seguent+=modul
			tamany_agafar ="bytes="+str(actual)+"-"+str(seguent)
		diccionari["size"]=tamany_agafar
		diccionari["particio"]=i+1
		provemFunc.invoke("map_countingWords", diccionari)
		#provemFunc.invoke("map_wordCount", diccionari)
		actual=seguent
		seguent+=aux
		i+=1	
	#provemFunc.invoke("reduce_countingWords", diccionari)
	#provemFunc.invoke("reduce_wordCount", diccionari)
else:
	print("Error: et falten el nombre de particions que voldras pel fitxer o el nom del fitxer o ambdues.")
