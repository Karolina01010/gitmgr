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

mxd.save()



import arcpy

fc = arcpy.mapping.Layer('D:\mgr\Baza100.gdb/Rzeka_strum_L')

with arcpy.da.UpdateCursor(fc,["SHAPE@"]) as cursor:
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