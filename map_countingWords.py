import cos_backend
import json

def main(args):
	file_name= args.get("file_name")
	rango = args.get("size")
	particio=args.get("particio")
	configu = args.get("config")
	cos=cos_backend.cos_backend(configu)
	fitxer=str(cos.get_object('joanuni', file_name, extra_get_args={'Range': rango})).lower().split()
	diccionari2={}
	cont=len(fitxer)
	diccionari2["total_paraules"]=cont
	cos.put_object("joanuni","map_countingWord"+str(particio)+".txt",json.dumps(diccionari2))
	return diccionari
