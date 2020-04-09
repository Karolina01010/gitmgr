import arcpy,math
workspace = r"D:\mgr\M33033CD\BAZA_M33033.gdb"
arcpy.env.workspace = workspace
budynek=r'D:\mgr\M33033CD\BAZA_M33033.gdb\budP'
line=r'D:\mgr\M33033CD\BAZA_M33033.gdb\szosa_droga'
#Output, change path (and fc name if you want)

#Desired distance from polygon centroids to nearest line. Change
desired_distance=30



def bearing_to_radians(bearing):
    return math.radians((450-bearing)%360) # ZWIJANIE WIELU OBROTÓW WJEDEN =   zamiana kata na radiany  (360 +90= 450 ) rusunki  zeszyt  https://stackoverflow.com/questions/9875964/python-converting-radians-to-degrees

#Tworzy punkt srodkowy wielokąta, calculate near distance and angle and join this to polygons

#arcpy.Near_analysis('budynek', 'line')    # Oblicza odległość i kąt  między obiektami wejściowymi a najbliższymi obiektami w innej warstwie lub klasie obiektów.
#arcpy.MakeFeatureLayer_management('budynek','budynek_layer')   #Tworzy warstwę obiektów z wejściowej klasy obiektów lub pliku warstwy.


#Move the polygons
with arcpy.da.UpdateCursor(budynek,['SHAPE@X','SHAPE@Y','NEAR_DIST','NEAR_ANGLE']) as cursor:
    for row in cursor:
        newx=row[0]+(row[2]-desired_distance)*math.sin(bearing_to_radians(row[3])) # oblicznie nowej wspolrzednej  Xnew = X + ( odległos + wartosc przesuniecia) * sin ( azymut kąta)
        newy=row[1]+(row[2]-desired_distance)*math.cos(bearing_to_radians(row[3])) # oblicznie nowej wspolrzednej Ynew = Y + ( odległos + wartosc przesuniecia) * cos ( azymut kąta)
        row[0]=newx
        row[1]=newy
        cursor.updateRow(row)


addLayer = arcpy.mapping.Layer()
arcpy.mapping.Layer(r "I: \ UPDM.gdb \ P_PipeSystem \ P_Meters")
arcpy.mapping.AddLayer (df, addLayer, „BOTTOM”)
