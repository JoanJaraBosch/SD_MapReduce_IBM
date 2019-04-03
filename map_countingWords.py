import cos_backend
import json
import re

def main(args):
	file_name= args.get("file_name")
	rango = args.get("size")
	particio=args.get("particio")
	configu = args.get("config")
	cos=cos_backend.cos_backend(configu)
	line=cos.get_object('joanuni', file_name, extra_get_args={'Range': rango}).decode('latin-1').lower()
	fitxer = re.sub(r'[-,;.:?¿!¡\'\(\)\[\]\"*+-_<>#$€&^%|]', " ", line).split()
	diccionari2={}
	cont=len(fitxer)
	diccionari2["total_paraules"]=cont
	cos.put_object("joanuni","map_countingWord"+file_name.replace(".txt","")+str(particio)+".txt",json.dumps(diccionari2))
	return {"result":"finish"}
