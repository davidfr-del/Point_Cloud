import os
import glob 

absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
actual_directory=fileDirectory.replace('\\','/')

ground_truth=[]
mylist= []
rango=[]


os.chdir(f"{actual_directory}")
for x in glob.glob("Lux*"):
    rango.append(int(x.replace('Luxemburgo','')))

min_tile=min(rango)
max_tile=max(rango)

print(f"Seleccione el tile deseado entre {min_tile} y {max_tile}")

for x in range(max_tile):
    tile_number=x+1

    os.chdir(f"{actual_directory}/Luxemburgo{tile_number}/data")
    for dimensions_file in glob.glob("attributes*.geojson"):
        dimensions_file
    


    prueba2_file = open(f"{actual_directory}/Luxemburgo{tile_number}/data/{dimensions_file}", "r")

    highpower= prueba2_file.read()

    prueba2_file.close()


    # Replace the target string
    highpower = highpower.replace('"properties": { }', '"properties": {"cls": 1 }')

    # Write the file out again
    with open(f"{actual_directory}/Luxemburgo{tile_number}/data/{dimensions_file}", 'w') as file:
        file.write(highpower)