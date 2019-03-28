import cos_backend

def main(args):
	file_name= args.get("file_name")
	rango = args.get("size")
	particio=args.get("particio")
	configu = args.get("config")
	cos=cos_backend.cos_backend(configu)
	fitxer=str(cos.get_object('joanuni', file_name, rango)).replace("\\n"," ").replace("."," ").replace(","," ").replace("-"," ").replace("'","").replace("\"","").replace("\\"," ").replace("\\t"," ").replace(";"," ").replace("_"," ").replace("-"," ").replace("!"," ").replace("("," ").replace(")"," ").replace("#"," ").replace("@"," ").replace("["," ").replace("]"," ").replace(":"," ").replace("{"," ").replace("}"," ").replace("?"," ").replace("|"," ").replace("="," ").replace("*"," ").replace("/"," ").lower().split()
	diccionari={}
	
	for paraula in fitxer:
		if paraula not in diccionari.keys():
			diccionari[paraula]=1
		else:
			diccionari[paraula]+=1
	
	print(diccionari)	
	cos.put_object("joanuni","map_wordCount"+str(particio)+".txt",str(diccionari))
	return diccionari
