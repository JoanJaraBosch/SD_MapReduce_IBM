import cos_backend

def main(args):
	file_name= args.get("file_name")
	rango = args.get("size")
	configu = args.get("config")
	particio = args.get("particio")
	cos=cos_backend.cos_backend(configu)
	fitxer=str(cos.get_object('joanuni',file_name,rango)).replace("\\n"," ").replace("."," ").replace(","," ").replace("-"," ").replace("'","").replace("\"","").replace("\\"," ").replace("\\t"," ").replace(";"," ").replace("_"," ").replace("-"," ").replace("!"," ").replace("("," ").replace(")"," ").replace("#"," ").replace("@"," ").replace("["," ").replace("]"," ").replace(":"," ").replace("{"," ").replace("}"," ").replace("?"," ").replace("|"," ").replace("="," ").replace("*"," ").replace("/"," ").lower().split()
	cos.put_object("joanuni","map_countingWords"+str(particio)+".txt",str(len(fitxer)))
	return {"total_paraules" : str(len(fitxer))}
