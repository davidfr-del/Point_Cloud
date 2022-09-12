import os
import glob 

absolutepath = os.path.abspath(__file__)
fileDirectory = os.path.dirname(absolutepath)
actual_directory=fileDirectory.replace('\\','/')

ground_truth=[]
highpower=[]
rango=[]
total_tp=0
total_fn=0
total_fp=0


os.chdir(f"{actual_directory}/clasificados")
for x in glob.glob("Lux*"):
    rango.append(int(x.replace('Luxemburgo','')))

min_tile=min(rango)
max_tile=max(rango)



print(f"Seleccione el tile deseado entre {min_tile} y {max_tile}")
for x in range(78):
    tile_number=x+1
    

    os.chdir(f"{actual_directory}/clasificados/Luxemburgo{tile_number}/data")
    for dimensions_file in glob.glob("dimensions*.txt"):
        dimensions_file
        
    prueba1_file = open(f"{actual_directory}/clasificados/Luxemburgo{tile_number}/data/{dimensions_file}", "r")

    ground_truth= prueba1_file.readlines()

    prueba1_file.close()


    prueba2_file = open(f"{actual_directory}/pruebas/Luxemburgo{tile_number}/data/{dimensions_file}", "r")

    highpower= prueba2_file.readlines()

    prueba2_file.close()

    tp_file= open(f"{actual_directory}/clasificados/Luxemburgo{tile_number}/data/tp.txt", "w")

    fp_file= open(f"{actual_directory}/clasificados/Luxemburgo{tile_number}/data/fp.txt", "w")

    fn_file= open(f"{actual_directory}/clasificados/Luxemburgo{tile_number}/data/fn.txt", "w")


    count_gt=-1
    count_hg=-1
    count_2=-1

    count_tp=0
    count_fn=-1
    count_fp=-1
    
    

    for line in ground_truth:
        count_gt+=1
        if(count_gt>=2):
            for line2 in highpower:
                count_2+=1
                if(count_2>=2):
                    if(line==line2):
                        count_tp+=1
                        tp_file.write(line)  
                        break
                    
    tp_file.close()

    tp_file= open(f"{actual_directory}/clasificados/Luxemburgo{tile_number}/data/tp.txt", "r")

    tp= tp_file.readlines()

    tp_file.close()


    for line3 in ground_truth:
        if not (tp.__contains__(line3)):
            count_fn+=1
            fn_file.write(line3)


    for line4 in highpower:
        count_hg+=1
        if not (tp.__contains__(line4)):
            count_fp+=1
            fp_file.write(line4)
                
    tp_file.close()
    
    total_tp+=count_tp
    total_fp+=count_fp
    total_fn+=count_fn
    
    print(f'Luxemburgo{tile_number}')
    print('Puntos ground truth: '+str(count_gt))
    print('Puntos highpower: '+str(count_hg))
    print('TP: '+str(count_tp))
    print('FP:'+str(count_fp))
    print('FN: '+str(count_fn))
    print('total TP: '+str(total_tp))
    print('total FP:'+str(total_fp))
    print('total FN: '+str(total_fn))
