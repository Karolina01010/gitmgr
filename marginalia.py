import os
import arcpy

#myMap ="D:\mgr\MGR.mxd"
arcpy.env.addOutputsToMap = True
mxd = arcpy.mapping.MapDocument(r"D:\mgr\M33033CD\Probny.mxd") # dzia?anie na otwartym pliku mxd ("CURRENT")
workspace = r"D:\mgr\M33033CD\BAZA_M33033_2.gdb"                    # definiujemy ta baze
arcpy.env.workspace = workspace

df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
df.scale = 100000

# dodaje wszystkie warstwy z basy do layout
walk = arcpy.da.Walk(workspace, datatype="FeatureClass")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        arcpy.mapping.AddLayer(df, arcpy.mapping.Layer(os.path.join(dirpath, filename)))
mxd.save()

arcpy.mapping.a

arcpy.ApplySymbologyFromLayer("Budynek_P","D:\mgr\Gitmgr\mgr\symbole\Budynek_P")

budynek=r'D:\mgr\M33033CD\BAZA_M33033.gdb\budP'
line=r'D:\mgr\M33033CD\BAZA_M33033.gdb\szosa_droga'

#ODSUWA PUNKTU OD LINII
def bearing_to_radians(bearing):
    return math.radians((450-bearing)%360) # ZWIJANIE WIELU OBROT?W WJEDEN =   zamiana kata na radiany  (360 +90= 450 ) rusunki  zeszyt  https://stackoverflow.com/questions/9875964/python-converting-radians-to-degrees

#Tworzy punkt srodkowy wielok?ta, calculate near distance and angle and join this to polygons

#arcpy.Near_analysis('budynek', 'line')    # Oblicza odleg?o?? i k?t  mi?dzy obiektami wej?ciowymi a najbli?szymi obiektami w innej warstwie lub klasie obiekt?w.
#arcpy.MakeFeatureLayer_management('budynek','budynek_layer')   #Tworzy warstw? obiekt?w z wej?ciowej klasy obiekt?w lub pliku warstwy.


#Move the polygons
with arcpy.da.UpdateCursor(budynek,['SHAPE@X','SHAPE@Y','NEAR_DIST','NEAR_ANGLE']) as cursor:
    for row in cursor:
        newx=row[0]+(row[2]-desired_distance)*math.sin(bearing_to_radians(row[3])) # oblicznie nowej wspolrzednej  Xnew = X + ( odleg?os + wartosc przesuniecia) * sin ( azymut k?ta)
        newy=row[1]+(row[2]-desired_distance)*math.cos(bearing_to_radians(row[3])) # oblicznie nowej wspolrzednej Ynew = Y + ( odleg?os + wartosc przesuniecia) * cos ( azymut k?ta)
        row[0]=newx
        row[1]=newy
        cursor.updateRow(row)

#ODSUWA POWIERZCHNIE OD LINII

import arcpy,math

polygon_fc=r'D:\mgr\M33033CD\BAZA_M33033.gdb\bud'
line_fc=r'D:\mgr\M33033CD\BAZA_M33033.gdb\szosa_droga'
#Output, change path (and fc name if you want)
output_polygon_fc=r'C:\TEST.gdb\Sample_points_buffer_near'
#Desired distance from polygon centroids to nearest line. Change
desired_distance=30

temp_points=r'in_memory\points'

def bearing_to_radians(bearing):
    return math.radians((450-bearing)%360)

#Tworzy punkt srodkowy wielok?ta, calculate near distance and angle and join this to polygons
arcpy.FeatureToPoint_management(in_features=polygon_fc, out_feature_class=temp_points)
arcpy.Near_analysis(in_features=temp_points, near_features=line_fc,location=True, angle=True, method='PLANAR')
arcpy.MakeFeatureLayer_management(in_features=polygon_fc, out_layer='polygon_lyr')
arcpy.AddJoin_management(in_layer_or_view='polygon_lyr', in_field='OBJECTID', join_table=temp_points,
                        join_field='OBJECTID')
arcpy.CopyFeatures_management(in_features='polygon_lyr', out_feature_class=output_polygon_fc)

#Move the polygons
with arcpy.da.UpdateCursor(output_polygon_fc,['SHAPE@X','SHAPE@Y','NEAR_DIST','NEAR_ANGLE']) as cursor:
    for row in cursor:
        newx=row[0]+(row[2]-desired_distance)*math.sin(bearing_to_radians(row[3]))
        newy=row[1]+(row[2]-desired_distance)*math.cos(bearing_to_radians(row[3]))
        row[0]=newx
        row[1]=newy
        cursor.updateRow(row)

# ODSUWANIE POWIERZCHNI OD LINI
# https://gis.stackexchange.com/questions/230889/automatically-moving-overlapping-features-using-arcgis-desktop/231036#231036

budynek=r'D:\mgr\M33033CD\BAZA_M33033.gdb\budA'
line=r'D:\mgr\M33033CD\BAZA_M33033.gdb\szosa_droga'
#Output, change path (and fc name if you want)
nowypoligon=r'D:\mgr\M33033CD\BAZA_M33033.gdb\Sample_points_buffer_near'
#Desired distance from polygon centroids to nearest line. Change
desired_distance=30

temp_points=r'in_memory\points'

def bearing_to_radians(bearing):
    return math.radians((450-bearing)%360)

#Tworzy punkt srodkowy wielok?ta, calculate near distance and angle and join this to polygons
arcpy.FeatureToPoint_management('budynek','temp_points')   #Tworzy klas? obiekt?w zawieraj?c? punkty wygenerowane z reprezentatywnych lokalizacji obiekt?w wej?ciowych.
arcpy.Near_analysis('temp_points', 'line')    # Oblicza odleg?o?? i k?t  mi?dzy obiektami wej?ciowymi a najbli?szymi obiektami w innej warstwie lub klasie obiekt?w.
arcpy.MakeFeatureLayer_management('budynek','polygon_lyr')   #Tworzy warstw? obiekt?w z wej?ciowej klasy obiekt?w lub pliku warstwy.
arcpy.AddJoin_management('polygon_lyr','OBJECTID', 'temp_points', 'OBJECTID')  #??czy warstw? z inn? warstw? lub tabel? na podstawie wsp?lnego pola (dodaje do nowej warstwy  Budynek A informacje o odleg?osci do najblizszej drogi "NEAR_DIST"  z warstwy punktowej )
arcpy.CopyFeatures_management('polygon_lyr','nowypoligon') #Kopiuje obiekty z wej?ciowej klasy obiekt?w lub warstwy do nowej klasy obiekt?w.

#Move the polygons
with arcpy.da.UpdateCursor(nowypoligon,['SHAPE@X','SHAPE@Y','NEAR_DIST','NEAR_ANGLE']) as cursor:
    for row in cursor:
        newx=row[0]+(row[2]-desired_distance)*math.sin(bearing_to_radians(row[3]))
        newy=row[1]+(row[2]-desired_distance)*math.cos(bearing_to_radians(row[3]))
        row[0]=newx
        row[1]=newy
        cursor.updateRow(row)

mxd.save()