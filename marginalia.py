import os
import arcpy

#myMap ="D:\mgr\MGR.mxd"
arcpy.env.addOutputsToMap = True
mxd = arcpy.mapping.MapDocument(r"D:\mgr\M33033CD\DROGI.mxd") # dzia?anie na otwartym pliku mxd ("CURRENT")
workspace = r"D:\mgr\M33033CD\BAZA_M33033.gdb"                    # definiujemy ta baze
arcpy.env.workspace = workspace

#GENERALIZACJA DROG
arcpy.Dissolve_management("ZL_101","D:\mgr\M33033CD\droga\ZL101.shp","","","","UNSPLIT_LINES") # Agreguje warstw? w oparciu o okre?lone atrybuty.
arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL101.shp",20)     #integralno?ci wsp?lnych granic element?w znjaduj?cej sie w odleglosci 15
arcpy.MakeFeatureLayer_management("D:\mgr\M33033CD\droga\ZL101.shp",'ZL101')                      # tworzy warstwe w layers
arcpy.ApplySymbologyFromLayer_management('ZL101',"D:\mgr\Gitmgr\mgr\symbole\Szosa_101.lyr")       # nadaje symbole
arcpy.Delete_management('ZL_101')

df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
df.scale = 100000

walk = arcpy.da.Walk(workspace, datatype="FeatureClass")
for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        arcpy.mapping.AddLayer(df, arcpy.mapping.Layer(os.path.join(dirpath, filename)))
        print filename
mxd.save()

# zapisuje w shp
arcpy.Dissolve_management("ZL_101","D:\mgr\M33033CD\droga\ZL101.shp") # Agreguje warstw? w oparciu o okre?lone atrybuty.
arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL101.shp",50)     #integralno?ci wsp?lnych granic element?w znjaduj?cej sie w odleglosci 15
#arcpy.MakeFeatureLayer_management('Budynek_A_AAL015', 'Budynek_A_layer') - najprawdopodobnije nie potrzebne
arcpy.ApplySymbologyFromLayer_management("ZL_101","D:\mgr\Gitmgr\mgr\symbole\Szosa_101.lyr")



arcpy.ApplySymbologyFromLayer_management("Rzeka_strum_L",r'D:\mgr\Gitmgr\mgr\symbole\Rzeka_L.lyr')
arcpy.ApplySymbologyFromLayer_management("Budynek_P","D:\mgr\Gitmgr\mgr\symbole\Budynek_P.lyr")
arcpy.ApplySymbologyFromLayer_management("Budynek_PP","D:\mgr\Gitmgr\mgr\symbole\Budynek_P.lyr")

arcpy.ApplySymbologyFromLayer_management("ZL_018","D:\mgr\Gitmgr\mgr\symbole\Szosa_018.lyr")

arcpy.ApplySymbologyFromLayer_management("ZL_103","D:\mgr\Gitmgr\mgr\symbole\Szosa_103.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_104","D:\mgr\Gitmgr\mgr\symbole\Szosa_104.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_105","D:\mgr\Gitmgr\mgr\symbole\Szosa_105.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_106","D:\mgr\Gitmgr\mgr\symbole\Szosa_106.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_107","D:\mgr\Gitmgr\mgr\symbole\Szosa_107.lyr")
arcpy.ApplySymbologyFromLayer_management("ZL_108","D:\mgr\Gitmgr\mgr\symbole\Szosa_108.lyr")
mxd.save()

# zapisuje w shp
arcpy.Dissolve_management("ZL_101","D:\mgr\mgrA") # Agreguje warstw? w oparciu o okre?lone atrybuty.
arcpy.Integrate_management("Szosa_droga_L",15)     #integralno?ci wsp?lnych granic element?w znjaduj?cej sie w odleglosci 15
#arcpy.MakeFeatureLayer_management('Budynek_A_AAL015', 'Budynek_A_layer') - najprawdopodobnije nie potrzebne

arcpy.Dissolve_management("ZL_103","D:\mgr\Droga\ZL_103A.shp") # Agreguje warstw? w oparciu o okre?lone atrybuty.
arcpy.Integrate_management("ZL_103A",15)
arcpy.ApplySymbologyFromLayer_management("ZL_103A","D:\mgr\Gitmgr\mgr\symbole\Szosa_103.lyr")

arcpy.Integrate_management("ZL_104",20)
arcpy.Dissolve_management("ZL_104","D:\mgr\Droga\ZL_104.shp")  # w odwrtonej kolejnosci ze wzgledu na to ze linie sie ?acza i wychodzi przerwa w odwrotnej kolejnosci ze wzhledu na b?edne ?aczenie serpentyn an drodze

arcpy.Dissolve_management("ZL_101","D:\mgr\M33033CD\droga\droga101.shp","","","","UNSPLIT_LINES")

arcpy.Dissolve_management("ZL_103","D:\mgr\103")
arcpy.Integrate_management("Szosa_droga_L",15)

arcpy.ResolveRoadConflicts_cartography("101;105","Id","D:\mgr\mgr.gdb")


arcpy.Dissolve_management("droga_101","D:\mgr\M33033CD\droga\ZL_101.shp","","","","UNSPLIT_LINES")


arcpy.ResolveBuildingConflicts("bud","HGT","mgrA")

mxd.save()

# FILTRACJA

#arcpy.Buffer_analysis("Budnek_P", "buffer",80)

#arcpy.cartography.SimplifyLine("rzeka","rzeka1","POINT_REMOVE",10)

feature = r"D:\mgr\M33033CD\BAZA_M33033.gdb\bud"

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



import arcpy

line_lyr = "szosa_droga"
pt_lyr =  "bud"
interval = 50


insertCursor = arcpy.da.InsertCursor("bud", ["SHAPE@XY"]) # this is the pre-existing pt feature class

with arcpy.da.SearchCursor(line_lyr, ['OID@','SHAPE@','FID']) as searchCursor: # this is the line feature on which the points will be based
    for row in searchCursor:
        lengthLine = round(row[1].length) # grab the length of the line feature, i'm using round() here to avoid weird rounding errors that prevent the numberOfPositions from being determined
        if int(lengthLine % interval) == 0:
            numberOfPositions = int(lengthLine // interval) - 1
        else:
            numberOfPositions = int(lengthLine // interval)

        if numberOfPositions > 0: # > 0 b/c we don't want to add a point to a line feature that is less than our interval
            for i in range(numberOfPositions): # using range, allows us to not have to worry about
                distance = (i + 1) * interval
                xPoint = row[1].positionAlongLine(distance).firstPoint.X
                yPoint = row[1].positionAlongLine(distance).firstPoint.Y
                xy = (xPoint, yPoint)
                insertCursor.insertRow([xy])


ResolveRoadConflicts_cartography
arcpy.ResolveBuildingConflicts

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



import arcpy,math

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

