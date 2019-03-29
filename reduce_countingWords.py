import cos_backend
import json

def main(args):
	configu = args.get("config")
	n_particions = args.get("particions")
	cos=cos_backend.cos_backend(configu)
	aux=0
	i=0
	while(i<int(n_particions)):
		dades =cos.get_object('joanuni',"map_countingWords"+str(i+1)+".txt","")
		if dades != "No file":	
			diccionari=json.loads(dades)
			aux+=diccionari["total_paraules"]
			cos.delete_object("joanuni", "map_countingWords"+str(i+1)+".txt")
			i+=1
	diccionari={}
	diccionari["total_paraules"]=aux
	cos.put_object("joanuni","reduce_countingWords.txt", json.dumps({"loko":1234}))
	return diccionari
