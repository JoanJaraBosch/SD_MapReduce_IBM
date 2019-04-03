import cos_backend
import json

def main(args):
	configu = args.get("config")
	n_particions = args.get("particions")
	file_name = args.get("file_name")
	cos=cos_backend.cos_backend(configu)
	aux={}
	i=0
	while(i<int(n_particions)):
		dades=cos.get_object('joanuni',"map_countingWord"+file_name.replace(".txt","")+str(i+1)+".txt")
		if dades != "No file":
			diccionari2=json.loads(dades.decode('latin-1'))
			cos.delete_object("joanuni","map_countingWord"+file_name.replace(".txt","")+str(i+1)+".txt")
			for item in diccionari2.keys():
				if item in aux:
					aux[item]=diccionari2[item]+aux[item]
				else:
					aux[item]=diccionari2[item]
			i+=1
	cos.put_object("joanuni","reduce_countingWord"+file_name.replace(".txt","")+".txt", json.dumps(aux))
	return {"result":"finish"}
