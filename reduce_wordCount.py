import cos_backend
import json

def main(args):
	configu = args.get("config")
	n_particions = args.get("particions")
	cos=cos_backend.cos_backend(configu)
	aux={}
	i=0
	while(i<int(n_particions)):
		diccionari=json.loads(cos.get_object('joanuni',file_name,""))
		if(i==0):
			aux=diccionari
		else:
			
		cos.delete_object("joanuni", )
		i+=1
	return {"total_paraules" : str(len(fitxer))}
