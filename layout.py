import os
import arcpy


mxd = arcpy.mapping.MapDocument(r"D:\mgr\MGR.mxd")
arcpy.env.workspace = "D:\mgr\Baza100.gdb"
marginalnia_A = "D:\mgr\Gitmgr\mgr\marginalia\L_Area.shp"
marginalnia_P = "D:\mgr\Gitmgr\mgr\marginalia\L_Point.shp"
marginalnia_L = "D:\mgr\Gitmgr\mgr\marginalia\L_Line.shp"

arcpy.MakeFeatureLayer_management('Budynek_P_PAL015', r'D:\mgr\symbole\Budynek_P.lyr')



