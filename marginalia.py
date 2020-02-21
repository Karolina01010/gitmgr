import os
import arcpy

#myMap ="D:\mgr\MGR.mxd"
mxd = arcpy.mapping.MapDocument(r"D:\mgr\mxdd.mxd") # dzia?anie na otwartym pliku mxd ("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
df.scale = 50000

addLayer = arcpy.mapping.Layer(r"D:\mgr\symbole\Budynek_P.lyr")
arcpy.mapping.AddLayer(df, addLayer)
mxd.saveACopy(r"D:\mgr\FINALPROJECT.mxd")


#arcpy.mapping.AddLayer(

#arcpy.ApplySymbologyFromLayer_management("Budynek_P",r'D:\mgr\symbole\Budynek_P.lyr')
#arcpy.ApplySymbologyFromLayer_management("Budynek_A",r'D:\mgr\symbole\Budynek_A.lyr')


#lyrGr = arcpy.mapping.Layer("D:\mgr\symbole\Budynek_P.lyr")
#newlyrGr = arcpy.mapping.ListLayers(df)[0]






