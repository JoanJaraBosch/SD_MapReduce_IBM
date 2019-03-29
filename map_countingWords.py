import cos_backend
import json

def main(args):
	file_name= args.get("file_name")
	diccionari={}
	rango = args.get("size")
	configu = args.get("config")
	particio = args.get("particio")
	cos=cos_backend.cos_backend(configu)
	fitxer=str(cos.get_object('joanuni',file_name,rango)).replace("\\n"," ").replace("."," ").replace(","," ").replace("-"," ").replace("'","").replace("\"","").replace("\\"," ").replace("\\t"," ").replace(";"," ").replace("_"," ").replace("-"," ").replace("!"," ").replace("("," ").replace(")"," ").replace("#"," ").replace("@"," ").replace("["," ").replace("]"," ").replace(":"," ").replace("{"," ").replace("}"," ").replace("?"," ").replace("|"," ").replace("="," ").replace("*"," ").replace("/"," ").lower().split()
	diccionari["total_paraules"]=len(fitxer)
	cos.put_object("joanuni","map_countingWords"+str(particio)+".txt",json.dumps(diccionari))
	return diccionari
