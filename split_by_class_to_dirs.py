import shutil, os, argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path_to_images", required=True,
	help="path to patch images")
args = vars(ap.parse_args())

original_path = args["path_to_images"]


patch_imageset_path = '/imageset'
path = os.getcwd() + patch_imageset_path
nucleos = path + '/nucleos'
nonucleos = path +'/nonucleos'

#si las carpetas no existen, las creamos
if not os.path.isdir(path):
    try:
        os.mkdir(path)
    except:
        print('cannot create dir {}'.format(path))


if not os.path.isdir(nucleos):
    try:
        os.mkdir(nucleos)
    except:
        print('cannot create dir {}'.format(nucleos))


if not os.path.isdir(nonucleos):
    try:
        os.mkdir(nonucleos)
    except:
        print('cannot create dir {}'.format(nonucleos))

#generar la lista de imagenes
(_, _, image_names) = next(os.walk(original_path))

#separar las imagenes por clase
#para cada imágen en la carpeta
for image_name in image_names:
    #dividimos el nombre según sus componentes
    name = image_name.split("_")
    #recuperamos la clase
    image_class = name[2]
    #si la clase de la imagen es núcleo
    if image_class == '1':
        #la movemos a la carpeta de núcleos
        shutil.move(original_path +"/"+image_name, nucleos)
    #si no es núcleo es nonucleo
    else:
        #la movemos a la carpeta de nonucleos
        shutil.move(original_path +"/"+image_name, nonucleos)
