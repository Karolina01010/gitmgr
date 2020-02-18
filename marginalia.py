import os
import arcpy
mxdd ="D:\mgr\MGR.mxd"
dane_wyjsc = "D:\mgr\Baza100.gdb"
for dane_wyjsc in cursor:
    mxd = arcpy.mapping.MapDocument(mxdd)

arcpy.env.workspace = "D:\mgr\Baza100.gdb"
marginalnia_A = "D:\mgr\Gitmgr\mgr\marginalia\L_Area.shp"
marginalnia_P = "D:\mgr\Gitmgr\mgr\marginalia\L_Point.shp"
marginalnia_L = "D:\mgr\Gitmgr\mgr\marginalia\L_Line.shp"

arcpy.MakeFeatureLayer_management('Budynek_P_PAL015', r'D:\mgr\symbole\Budynek_P.lyr')



