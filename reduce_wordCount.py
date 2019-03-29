import cos_backend
import json

def main(args):
	configu = args.get("config")
	n_particions = args.get("particions")
	total= args.get("total")
	cos=cos_backend.cos_backend(configu)
	rang="bytes=0-"+str(total)
	aux={}
	i=0
	while(i<int(n_particions)):
		dades=cos.get_object('joanuni',"map_wordCount"+str(i+1)+".txt",rang)
		if dades != "No file":
			diccionari=json.loads(dades)
			cos.delete_object("joanuni","map_wordCount"+str(i+1)+".txt")
			print(diccionari)
			for item in diccionari.keys():
				if item in aux:
					aux[item]=diccionari[item]+aux[item]
				else:
					aux[item]=diccionari[item]
			i+=1
	cos.put_object("joanuni","reduce_wordCount.txt", json.dumps(aux))
	return {"total_paraules" : ""}
