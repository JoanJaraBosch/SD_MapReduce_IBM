import cos_backend

def main(args):
	configu = args.get("config")
	n_particions = args.get("particions")
	total= args.get("total")
	cos=cos_backend.cos_backend(configu)
	rang="bytes=0-"+str(total)
	aux=0
	i=0
	while(i<int(n_particions)):
		diccionari=int(cos.get_object('joanuni',"map_countingWords"+str(i+1)+".txt",rang))
		aux+=diccionari
		cos.delete_object("joanuni", "map_countingWords"+str(i+1)+".txt")
		i+=1
	cos.put_object("joanuni","reduce_countingWords.txt", dades)
	return {"total_paraules" : aux}
