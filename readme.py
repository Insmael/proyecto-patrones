para reproducir el experimento,
se deben seguir los pasos del tutorial hasta el paso 1,
en este momento tendremos una carpeta con todos los patches de entrenamiento, llamemosla dir1,
para seguir con el entrenamiento del modelo, se debe correr

python split_by_class_to_dirs.py -p dir1_path

al ejecutar el anterior script, se creará una carpeta llamada imageset,
que contendrá las imágenes (patch) separados por clase en carpetas distintas,
carpeta núcleo y nonucleo.

para la creación de los datos a utilzar por el modelo se corre el siguiente comando

python dataset_build.py -d path_to_imageset_dir

esto generará dos archivos en la carpeta donde se ejecute el comando, dataset.npy y labels.npy.
El siguiente comando asume que estos dos archivos existen en el directorio donde se ejecuta

python make_model.py

que crea el modelo, guardandolo en la carpeta saved_models.
además, en la salida estandar deja escrito la precisión del modelo

por último, si se quiere generar una imagen a partir de un modelo se debe ejecutar

pythonew_image.py - i path_to_original_image -m path_to_model

SE ADVIERTE QUE EL PROCESO DE LA CREACIÓN DE LA IMAGEN TOMA HORAS,
