import subprocess
import os
import zipfile

def comprimir_subdirectorios_con_limpieza(directorio):
	"""
	Comprime cada subdirectorio de un directorio dado en un archivo .zip,
	eliminando cualquier archivo .zip existente en el directorio antes de comprimir.

	Args:
		directorio (str): El directorio padre que contiene los subdirectorios a comprimir.

	Returns:
		None
	"""
	# Eliminar archivos ZIP existentes en el directorio
	for archivo in os.listdir(directorio):
		if archivo.endswith(".zip"):
			ruta_archivo_zip = os.path.join(directorio, archivo)
			os.remove(ruta_archivo_zip)
			print(f"Eliminado archivo ZIP existente: {ruta_archivo_zip}")

	# Comprimir subdirectorios
	for carpeta_raiz, directorios, archivos in os.walk(directorio, topdown=True):
		# Ignorar el nivel raíz, comenzar desde los primeros subdirectorios
		for subdirectorio in directorios:
			ruta_abs_subdirectorio = os.path.join(carpeta_raiz, subdirectorio)
			# Ignorar subdirectorios anidados
			if carpeta_raiz == directorio:
				nombre_archivo_zip = f"{ruta_abs_subdirectorio}.zip"
				with zipfile.ZipFile(nombre_archivo_zip, 'w', zipfile.ZIP_DEFLATED) as archivo_zip:
					for raiz, dirs, files in os.walk(ruta_abs_subdirectorio):
						for archivo in files:
							ruta_abs_archivo = os.path.join(raiz, archivo)
							ruta_relativa_archivo = os.path.relpath(ruta_abs_archivo, ruta_abs_subdirectorio)
							archivo_zip.write(ruta_abs_archivo, ruta_relativa_archivo)
				print(f"Comprimido: {nombre_archivo_zip}")

def run_comando(comando):
	process = subprocess.Popen(comando, stdout=subprocess.PIPE)
	output = process.communicate()[0]

directorio = "data/beta" # Asegúrate de ajustar esta ruta al directorio que deseas comprimir
comprimir_subdirectorios_con_limpieza(directorio)

comentario = input("Introduzca comentario: ")
run_comando(["git", "init"])
run_comando(["git", "add", "."])
run_comando(["git", "commit", "-m", comentario])
run_comando(["git", "push", "origin", "master"])
os.system("pause")