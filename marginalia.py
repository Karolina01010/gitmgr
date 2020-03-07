import os
import arcpy

#myMap ="D:\mgr\MGR.mxd"
mxd = arcpy.mapping.MapDocument(r"D:\mgr\mxdd.mxd") # dzia?anie na otwartym pliku mxd ("CURRENT")
workspace = r"D:\mgr\Baza100.gdb"                    # definiujemy ta baze

walk = arcpy.da.Walk(workspace, datatype="Layer")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        arcpy.mapping.AddLayer(os.path.join(dirpath, filename))



df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
walk = arcpy.da.Walk(workspace, datatype = "Layer")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        arcpy.mapping.AddLayer(df, arcpy.mapping.Layer(os.path.join(dirpath, filename)))
        print filename,'\n'
mxd.save()

fcs = []
for fds in arcpy.ListDatasets('','feature') + ['']:
        for fc in arcpy.ListFeatureClasses('','',fds):
            fcs.append(os.path.join(fds, fc))
return fcs

#addLayer = arcpy.mapping.Layer(r"D:\mgr\Baza100.gdb\Rzeka_strum_L")
#addLayer = arcpy.mapping.Layer(r"D:\mgr\Baza100.gdb\Rzeka_strum_L")

#arcpy.mapping.AddLayer(df,Layer)

#mxd.saveACopy(r"D:\mgr\FINALPROJECT.mxd")
#df.scale = 100000

#arcpy.mapping.ExportToPDF(mxd,"D:\mgr\gotowe")
#arcpy.mapping.AddLayer(


#arcpy.ApplySymbologyFromLayer_management("Rzeka_strum_L",r'D:\mgr\Gitmgr\mgr\symbole\Rzeka_L.lyr')
#arcpy.ApplySymbologyFromLayer_management("Budynek_P",r'D:\mgr\symbole\Budynek_P.lyr')
#arcpy.ApplySymbologyFromLayer_management("Budynek_A",r'D:\mgr\symbole\Budynek_A.lyr')


#lyrGr = arcpy.mapping.Layer("D:\mgr\symbole\Budynek_P.lyr")
#newlyrGr = arcpy.mapping.ListLayers(df)[0]

mxd = arcpy.mapping.MapDocument("CURRENT")

# Hook into the data frame where you want to add the layer
df  = arcpy.mapping.ListDataFrames(mxd)[0]

# Create a Layer object
lyr = arcpy.management.MakeFeatureLayer(r"Path\To\GDB\FeatureClass", "NameForLayer").getOutput(0)

# Add the layer object to the map
arcpy.mapping.AddLayer(df, lyr)




