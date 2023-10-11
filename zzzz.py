import os
ruta = os.path.abspath('media/gallery')

print(os.path.exists(ruta))

print(os.listdir(ruta))

for i in os.listdir(ruta):
    if i.startswith('portada-img'):
        os.remove(f'{ruta}/{i}')