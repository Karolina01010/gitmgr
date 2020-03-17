import os
import arcpy

#myMap ="D:\mgr\MGR.mxd"
arcpy.env.addOutputsToMap = True
mxd = arcpy.mapping.MapDocument(r"D:\mgr\Gitmgr\mgr\mxdd.mxd") # dzia?anie na otwartym pliku mxd ("CURRENT")
workspace = r"D:\mgr\Baza100.gdb"                    # definiujemy ta baze
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
df.scale = 100000

walk = arcpy.da.Walk(workspace, datatype="FeatureClass")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        arcpy.mapping.AddLayer(df, arcpy.mapping.Layer(os.path.join(dirpath, filename)))
        print filename
mxd.save()

arcpy.ApplySymbologyFromLayer_management("Rzeka_strum_L",r'D:\mgr\Gitmgr\mgr\symbole\Rzeka_L.lyr')
arcpy.ApplySymbologyFromLayer_management("Budynek_P_layer","D:\mgr\Gitmgr\mgr\symbole\Budynek_P.lyr")

mxd.save()

# FILTRACJA

#arcpy.Buffer_analysis("Budnek_P", "buffer",80)

#arcpy.cartography.SimplifyLine("rzeka","rzeka1","POINT_REMOVE",10)




fc = arcpy.mapping.Layer('D:\mgr\mgr.gdb\bud')

for i in range (1,next):
    Objid = "s" +str(1)


with arcpy.da.UpdateCursor(fc,["NEAR_FID"]) as cursor:
    for row in cursor:
        #loop through parts
        for part in row[0]:
            count = 0
            # loop through verticies
            for pnt in part:
                count = count + 1
                if count >= 3:
                    arr = row[0].getPart(0)
                    arr.remove(1)
                    newLine = arcpy.Polyline(arr)
                    row[0] = newLine
                    cursor.updateRow(row)

#arcpy.PointDistance_analysis("bud","bud","dystans",80)
import os
import arcpy

in_fc = r"D:\mgr\mgr.gdb\Export_Output_4"
nearest_dict = dict()
with arcpy.da.UpdateCursor(in_fc, ["OID@", "NEAR_FID"]) as rows:
    for row in rows:
        if row[1] <= 40:

            cursor.deleteRow(row[1])
            reset(row)
        else:
            # if the key does not exist then create a new list with near id
            # and add it to the dictionary
            nearest_dict[input_id] = [nearest_id]

print(nearest_dict)

import arcpy, sys

feature = r"D:\mgr\mgr.gdb\bud"

def nearRoutine():
    #calculate the distances using the current dataset
    arcpy.Near_analysis(feature, feature)

    # powtarza dla wszystkich funkcji, kt?re znajduj? si? w odleg?o?ci 40
    cur = arcpy.UpdateCursor(feature, '"NEAR_DIST" < 40')
    row1 = cur.next()  # zwraca nast?pny wiersz wej?ciowy
    while row1:
        cur.deleteRow(row1)  #ten punkt znajduje si? w odleg?o?ci  mniej niz 40 od s?siada, wi?c usuwa go


        del row1, cur   # teraz ponownie uruchom t? procedur? w nowym zestawie danych
        cur = arcpy.UpdateCursor(feature, '"NEAR_DIST" < 40')
        row1 = cur.next()
        nearRoutine

#wywo?uje procedur? rekurencyjn?. B?dzie dzia?a? stopniowo szybciej, poniewa? za ka?dym razem b?dzie przechodzi? przez mniejsz? liczb? punkt?w
nearRoutine()