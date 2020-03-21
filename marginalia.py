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

arcpy.ApplySymbologyFromLayer_management("ZL_018","D:\mgr\Gitmgr\mgr\symbole\Szosa_018.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_101","D:\mgr\Gitmgr\mgr\symbole\Szosa_101.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_103","D:\mgr\Gitmgr\mgr\symbole\Szosa_103.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_104","D:\mgr\Gitmgr\mgr\symbole\Szosa_104.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_105","D:\mgr\Gitmgr\mgr\symbole\Szosa_105.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_106","D:\mgr\Gitmgr\mgr\symbole\Szosa_106.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_107","D:\mgr\Gitmgr\mgr\symbole\Szosa_107.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_108","D:\mgr\Gitmgr\mgr\symbole\Szosa_108.lyr")

mxd.save()

# FILTRACJA

#arcpy.Buffer_analysis("Budnek_P", "buffer",80)

#arcpy.cartography.SimplifyLine("rzeka","rzeka1","POINT_REMOVE",10)

feature = r"D:\mgr\mgr.gdb\bud"

def nearRoutine():
    #coblicza odleglosc
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