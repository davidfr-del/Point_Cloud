import os
import glob 

absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
actual_directory=fileDirectory.replace('\\','/')

ground_truth=[]
mylist= []
rango=[]


os.chdir(f"{actual_directory}")
for x in glob.glob("data/atributos/*"):
    rango.append(x)


for x in range(len(rango)):

    os.chdir(f"{actual_directory}/data/atributos")
    for dimensions_file in glob.glob("attributes*.geojson"):
        dimensions_file
    


        prueba2_file = open(f"{dimensions_file}", "r")

        highpower= prueba2_file.read()

        prueba2_file.close()


        # Replace the target string
        highpower = highpower.replace('"properties": { }', '"properties": {"cls": 1 }')

        # Write the file out again
        with open(f"{dimensions_file}", 'w') as file:
            file.write(highpower)