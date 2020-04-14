import os
import arcpy

#myMap ="D:\mgr\MGR.mxd"
arcpy.env.addOutputsToMap = True
mxd = arcpy.mapping.MapDocument(r"D:\mgr\M33033CD\mxdd.mxd") # dzia?anie na otwartym pliku mxd ("CURRENT")

workspace = r"D:\mgr\M33033CD\BAZA_2.gdb"                    # definiujemy ta baze
arcpy.env.workspace = workspace

df = arcpy.mapping.ListDataFrames (mxd, "*") [0]

arcpy.MakeFeatureLayer_management('Rzeka_strum_L', 'Rzeka_strum_L_layer')

shape = arcpy.mapping.Layer('Rzeka_strum_L_layer')
symbologyLayer =("D:\mgr\Gitmgr\mgr\symbole\Rzeka_strum_L.lyr")
#arcpy.MakeFeatureLayer_management('Rzeka_strum_L', 'Rzeka_strum_L_layer')

for df in arcpy.mapping.ListDataFrames(mxd):
 arcpy.mapping.AddLayer(df, shape, "AUTO_ARRANGE")
 arcpy.ApplySymbologyFromLayer_management (shape, symbologyLayer)

arcpy.RefreshActiveView()
arcpy.RefreshTOC()

#arcpy.ApplySymbologyFromLayer_management(r"D:\mgr\M33033CD\droga\ZL018.shp",r"D:\mgr\Gitmgr\mgr\symbole\Rzeka_strum_L")

mxd.save()

arcpy.mapping.ExportToPDF(mxd,"D:\mgr\M33033CD\probny2.pdf" )


