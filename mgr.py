import os
import arcpy

arcpy.CreateFileGDB_management("D:\mgr\M33033CD", "BAZA_23") # tworzymy baze
dane_wyjsc = "D:\mgr\M33033CD\BAZA_23.gdb"                    # definiujemy ta baze
arcpy.env.workspace = dane_wyjsc

#Definiuje uk?ad wspolrzednych
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("ETRS 1989 UTM Zone 33N")

#Selekcja obiektow
inFeatures = ['D:\mgr\SHP_33033CD\Budynek_P_PAL015.shp',
 'D:\mgr\SHP_33033CD\Budynek_A_AAL015.shp',
 'D:\mgr\SHP_33033CD\Magazyn_skl_AAM010.shp',
 'D:\mgr\SHP_33033CD\Ogrodzenie_LAL070.shp',
 'D:\mgr\SHP_33033CD\Mur_ogrodze_LAL260.shp',
 'D:\mgr\SHP_33033CD\Park_A_AAK120.shp',
 'D:\mgr\SHP_33033CD\Zaklad_prze_AAC000.shp',
 'D:\mgr\SHP_33033CD\Zaklad_prze_PAC000.shp',
 'D:\mgr\SHP_33033CD\Drzewo_P_PEC030.shp',
 'D:\mgr\SHP_33033CD\Kanal_row_L_LBH020.shp',
 'D:\mgr\SHP_33033CD\Rzeka_strum_LBH140.shp',
 'D:\mgr\SHP_33033CD\Droga_polna_LAP010.shp',
 'D:\mgr\SHP_33033CD\Szosa_droga_LAP030.shp',
 'D:\mgr\SHP_33033CD\Jezioro_sta_ABH080.shp',
 'D:\mgr\SHP_33033CD\Las_A_AEC015.shp',
 'D:\mgr\SHP_33033CD\Sad_plantac_AEA040.shp',
 'D:\mgr\SHP_33033CD\Teren_zabud_AAL020.shp',
 'D:\mgr\SHP_33033CD\Roslinnosc_AEB010.shp',
 'D:\mgr\SHP_33033CD\Rezerwat_pr_AAL005.shp']
outLocation = dane_wyjsc

#zapisuje wybrane elementy w bazie (dodawane sa tebele z wartosciami dlugosci i powierzchni obiektu)
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)

def MakeFeatureLayer():
    arcpy.MakeFeatureLayer_management('Budynek_P_PAL015', 'Budynek_P_layer')
    arcpy.MakeFeatureLayer_management('Budynek_A_AAL015', 'Budynek_A_layer')
    arcpy.MakeFeatureLayer_management('Magazyn_skl_AAM010', 'Magazyn_skl_A_layer')
    arcpy.MakeFeatureLayer_management('Ogrodzenie_LAL070', 'Ogrodzenie_L_layer')
    arcpy.MakeFeatureLayer_management('Mur_ogrodze_LAL260', 'Mur_ogrodze_L_layer')
    arcpy.MakeFeatureLayer_management('Park_A_AAK120', 'Park_A_layer')
    arcpy.MakeFeatureLayer_management('Zaklad_prze_AAC000', 'Zaklad_prze_A_layer')
    arcpy.MakeFeatureLayer_management('Zaklad_prze_PAC000', 'Zaklad_prze_P_layer')
    arcpy.MakeFeatureLayer_management('Drzewo_P_PEC030', 'Drzewo_P_layer')
    arcpy.MakeFeatureLayer_management('Kanal_row_L_LBH020', 'Kanal_row_L_layer')
    arcpy.MakeFeatureLayer_management('Rzeka_strum_LBH140', 'Rzeka_strum_L_layer')
    arcpy.MakeFeatureLayer_management('Droga_polna_LAP010', 'Droga_polna_L_layer')
    arcpy.MakeFeatureLayer_management('Szosa_droga_LAP030', 'Szosa_droga_L_layer')
    arcpy.MakeFeatureLayer_management('Jezioro_sta_ABH080', 'Jezioro_sta_A_layer')
    arcpy.MakeFeatureLayer_management('Las_A_AEC015', 'Las_A_layer')
    arcpy.MakeFeatureLayer_management('Sad_plantac_AEA040', 'Sad_plantac_A_layer')
    arcpy.MakeFeatureLayer_management('Teren_zabud_AAL020', 'Teren_zabud_A_layer')
    arcpy.MakeFeatureLayer_management('Roslinnosc_AEB010', 'Roslinnosc_A_layer')
    arcpy.MakeFeatureLayer_management('Rezerwat_pr_AAL005', 'Rezerwat_pr_A_layer')
MakeFeatureLayer()

#Selekcjonuje obiekty ktore nastepnie sa zamieniane na punktowe

def FeatureToPoint():
    arcpy.SelectLayerByAttribute_management('Budynek_A_layer', "NEW_SELECTION",' "Shape_Area" < 5400 ')

    arcpy.FeatureToPoint_management('Budynek_A_layer', 'Budynek_PP')

    arcpy.SelectLayerByAttribute_management('Zaklad_prze_A_layer', "NEW_SELECTION",' "Shape_Area" < 22000 ')
    arcpy.FeatureToPoint_management('Zaklad_prze_A_layer', 'Zaklad_prze_PP')

    arcpy.SelectLayerByAttribute_management('Las_A_layer', "NEW_SELECTION",' "Shape_Area" < 10000 ')
    arcpy.FeatureToPoint_management('Las_A_layer', 'Drzewo_PP')

    arcpy.SelectLayerByAttribute_management('Sad_plantac_A_layer', "ADD_TO_SELECTION",' "Shape_Area" < 110000 ')
    arcpy.FeatureToPoint_management('Sad_plantac_A_layer', 'Drzewo_PP')
FeatureToPoint()

#Selekcja po atrybutach

def SelekcjaPoAtrybutach():
    arcpy.SelectLayerByAttribute_management('Budynek_A_layer', "NEW_SELECTION",' "Shape_Area" > 5400 ')
    arcpy.SelectLayerByAttribute_management('Magazyn_skl_A_layer', "NEW_SELECTION",' "Shape_Area" > 10000 ')

    arcpy.SelectLayerByAttribute_management('Park_A_layer', "NEW_SELECTION",' "Shape_Area" > 30000 ')
    arcpy.SelectLayerByAttribute_management('Jezioro_sta_A_layer', "NEW_SELECTION",' "Shape_Area" > 22000 ')
    arcpy.SelectLayerByAttribute_management('Zaklad_prze_A_layer', "NEW_SELECTION",' "Shape_Area" > 22000 ')
    arcpy.SelectLayerByAttribute_management('Las_A_layer', "NEW_SELECTION",' "Shape_Area" > 10000 ')
    arcpy.SelectLayerByAttribute_management('Sad_plantac_A_layer', "NEW_SELECTION",' "Shape_Area" > 100000 ')
    arcpy.SelectLayerByAttribute_management('Roslinnosc_A_layer', "NEW_SELECTION",' "Shape_Area" > 2000000 ')

    arcpy.SelectLayerByAttribute_management('Ogrodzenie_L_layer', "NEW_SELECTION",' "Shape_Length" > 500 ')
    arcpy.SelectLayerByAttribute_management('Mur_ogrodze_L_layer', "NEW_SELECTION",' "Shape_Length" > 500 ')
    arcpy.SelectLayerByAttribute_management('Kanal_row_L_layer', "NEW_SELECTION",' "Shape_Length" > 1000 ')
    arcpy.SelectLayerByAttribute_management('Droga_polna_L_layer', "NEW_SELECTION",' "Shape_Length" > 1000 ')

    arcpy.SelectLayerByAttribute_management('Rzeka_strum_L_layer', "NEW_SELECTION", '"HAT" = \'      500\' ')
    arcpy.SelectLayerByAttribute_management('Rzeka_strum_L_layer', "ADD_TO_SELECTION",' "Shape_Length" > 500 ')
    arcpy.SelectLayerByAttribute_management('Rzeka_strum_L_layer', "ADD_TO_SELECTION", '"HAT" = \'      501\' ')
SelekcjaPoAtrybutach()

#Zapisuje wyselekcjonowanie elementy do bazy100
def FeatureClassToFeatureClass():
    arcpy.FeatureClassToFeatureClass_conversion('Budynek_A_layer', dane_wyjsc, 'Budynek_A_select')
    arcpy.FeatureClassToFeatureClass_conversion('Magazyn_skl_A_layer', dane_wyjsc, 'Magazyn_skl_A')
    arcpy.FeatureClassToFeatureClass_conversion('Ogrodzenie_L_layer', dane_wyjsc, 'Ogrodzenie_L')
    arcpy.FeatureClassToFeatureClass_conversion('Mur_ogrodze_L_layer', dane_wyjsc, 'Mur_ogrodze_L')
    arcpy.FeatureClassToFeatureClass_conversion('Park_A_layer', dane_wyjsc, 'Park_A')
    arcpy.FeatureClassToFeatureClass_conversion('Zaklad_prze_A_layer', dane_wyjsc, 'Zaklad_prze_A')
    arcpy.FeatureClassToFeatureClass_conversion('Zaklad_prze_P_layer', dane_wyjsc, 'Zaklad_prze_P')

    arcpy.FeatureClassToFeatureClass_conversion('Kanal_row_L_layer', dane_wyjsc, 'Kanal_row_L')
    arcpy.FeatureClassToFeatureClass_conversion('Rzeka_strum_L_layer', dane_wyjsc, 'Rzeka_strum_L')
    arcpy.FeatureClassToFeatureClass_conversion('Droga_polna_L_layer', dane_wyjsc, 'Droga_polna_L')

    arcpy.FeatureClassToFeatureClass_conversion('Jezioro_sta_A_layer', dane_wyjsc, 'Jezioro_sta_A')
    arcpy.FeatureClassToFeatureClass_conversion('Las_A_layer', dane_wyjsc, 'Las_A')
    arcpy.FeatureClassToFeatureClass_conversion('Sad_plantac_A_layer', dane_wyjsc, 'Sad_plantac_A')
    arcpy.FeatureClassToFeatureClass_conversion('Teren_zabud_A_layer', dane_wyjsc, 'Teren_zabud_A')
    arcpy.FeatureClassToFeatureClass_conversion('Roslinnosc_A_layer', dane_wyjsc, 'Roslinnosc_A')
    arcpy.FeatureClassToFeatureClass_conversion('Rezerwat_pr_A_layer', dane_wyjsc, 'Rezerwat_pr_A')
    arcpy.FeatureClassToFeatureClass_conversion('Drzewo_P_layer', dane_wyjsc, 'Drzewo_P')
FeatureClassToFeatureClass()

#klasyfikacja budynkow
def KlasyfikacjaBudynkow():
    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"EXS" = \'7\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Ruiny_P1")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"BFC" = \'27\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Stacja_kol_P1")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"HWT"=\'3\'  AND "BFC"=\'7\' AND "EXS"=\'28\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Kaplica_P1")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"BFC" = \'54\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Stacja_benz_P1")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"BFC" = \'601\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Przystanek1")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"LMC" = \'1\' AND  "BFC" <> \'999\'')  # selekcja obiektow o zanacznieu orientacyjnym LMC =1 funkcja na ko?cu ze wzgledu na to ze obiekty religijne maja LMC =1
    arcpy.CopyFeatures_management('Budynek_P_layer',"Budynek_ZO1")
    arcpy.DeleteFeatures_management('Budynek_P_layer')
KlasyfikacjaBudynkow()

budynek_P = 'Budynek_P_layer'
droga = 'Szosa_droga_L_layer'
budynek_A = 'Budynek_A_select'

def bearing_to_radians(bearing):
        return math.radians((450-bearing)%360)

# ODSUWANIE POWIERZCHNI OD LINI
def Pow_od_lini():
    desired_distance1 = 68
    temp_points=r'in_memory\points'
    #Tworzy punkt srodkowy wielok?ta, calculate near distance and angle and join this to polygons
    arcpy.FeatureToPoint_management(budynek_A,'temp_points')   #Tworzy klas? obiekt?w zawieraj?c? punkty wygenerowane z reprezentatywnych lokalizacji obiekt?w wej?ciowych.
    arcpy.Near_analysis('temp_points', droga,"","NO_LOCATION","ANGLE","PLANAR")   # Oblicza odleg?o?? i k?t  mi?dzy obiektami wej?ciowymi a najbli?szymi obiektami w innej warstwie lub klasie obiekt?w.
    arcpy.MakeFeatureLayer_management(budynek_A,'polygon_lyr')   #Tworzy warstw? obiekt?w z wej?ciowej klasy obiekt?w lub pliku warstwy.
    arcpy.AddJoin_management('polygon_lyr','OBJECTID', 'temp_points', 'OBJECTID')  #??czy warstw? z inn? warstw? lub tabel? na podstawie wsp?lnego pola (dodaje do nowej warstwy  Budynek A informacje o odleg?osci do najblizszej drogi "NEAR_DIST"  z warstwy punktowej )
    #arcpy.CopyFeatures_management('polygon_lyr',budynek) #Kopiuje obiekty z wej?ciowej klasy obiekt?w lub warstwy do nowej klasy obiekt?w.
    arcpy.FeatureClassToFeatureClass_conversion('polygon_lyr', dane_wyjsc, 'Budynek_A')
    #Move the polygons
    with arcpy.da.UpdateCursor('Budynek_A',['SHAPE@X','SHAPE@Y','temp_points_NEAR_DIST','temp_points_NEAR_ANGLE']) as cursor:
        for row in cursor:
            xnew=row[0]-(row[2]-desired_distance1)*math.sin(bearing_to_radians(row[3]))
            ynew=row[1]-(row[2]-desired_distance1)*math.cos(bearing_to_radians(row[3]))
            row[0]=xnew
            row[1]=ynew
            cursor.updateRow(row)
    #arcpy.Delete_management('temp_points')
Pow_od_lini()

#odsuniecie budynkow od dorgi
def OdsuniecieBudynkow():

    arcpy.Near_analysis(budynek_P,droga,"","NO_LOCATION","ANGLE","PLANAR")    # Oblicza odleg?o?? i k?t  mi?dzy obiektami wej?ciowymi a najbli?szymi obiektami w innej warstwie lub klasie obiekt?w.

    desired_distance = 78  #odleglosc dobrego widzenia + polowa przekatnej

    #Move the point
    with arcpy.da.UpdateCursor(budynek_P,['SHAPE@X','SHAPE@Y','NEAR_DIST','NEAR_ANGLE']) as cursor:
        for row in cursor:
            newx=row[0]+(row[2]-desired_distance)*math.sin(bearing_to_radians(row[3]))
            newy=row[1]+(row[2]-desired_distance)*math.cos(bearing_to_radians(row[3]))
            row[0]=newx
            row[1]=newy
            cursor.updateRow(row)
OdsuniecieBudynkow()

# usuwanie budynkow zbyt blisko siebie
def NearAnalysisBudynki():

    #coblicza odleglosc miedzy budynkami
    arcpy.Near_analysis(budynek_P,budynek_P)

    # powtarza dla wszystkich funkcji, kt?re znajduj? si? w odleg?o?ci 50
    cur = arcpy.UpdateCursor(budynek_P, '"NEAR_DIST" < 58') # polowa przekoatnej 90x60
    row1 = cur.next()  # zwraca nast?pny wiersz wej?ciowy
    while row1:
        cur.deleteRow(row1)  #ten punkt znajduje si? w odleg?o?ci  mniej niz 40 od s?siada, wi?c usuwa go
        arcpy.Near_analysis(budynek_P,budynek_P) # jeszcze raz oblicza i aktualizuje odleg?oglosci aby nie usunac punktu bliskiego ktory juz nie istenieje

        del row1, cur   # teraz ponownie uruchom t? procedur? w nowym zestawie danych
        cur = arcpy.UpdateCursor(budynek_P, '"NEAR_DIST" < 58')
        arcpy.Near_analysis(budynek_P,budynek_P) # jeszcze raz oblicza i aktualizuje odleg?oglosci aby nie usunac punktu bliskiego ktory juz nie istenieje
        row1 = cur.next()
        NearAnalysisBudynki

        arcpy.FeatureClassToFeatureClass_conversion('Budynek_P_layer', dane_wyjsc, 'Budynek_P')
#wywo?uje procedur? rekurencyjn?. B?dzie dzia?a? stopniowo szybciej, poniewa? za ka?dym razem b?dzie przechodzi? przez mniejsz? liczb? punkt?w
NearAnalysisBudynki()


# Podzia? drogi na klasy
def KlasyfikacjaDrog():
    arcpy.SelectLayerByAttribute_management('Szosa_droga_L_layer', "NEW_SELECTION", '"TUC"=\'2\' AND "RTT"=\'16\'')
    arcpy.CopyFeatures_management('Szosa_droga_L_layer',"ZL_101")

    arcpy.SelectLayerByAttribute_management('Szosa_droga_L_layer', "NEW_SELECTION", '"RTT"=\'501\' AND "TUC"<>\'501\'')
    arcpy.CopyFeatures_management('Szosa_droga_L_layer',"ZL_103")

    arcpy.SelectLayerByAttribute_management('Szosa_droga_L_layer', "NEW_SELECTION", '"RTT"<>\'16\' AND "RTT"<>\'501\' AND "RST"=\'1\' AND "WD1">=7.4 AND "TUC"<>\'501\'')
    arcpy.CopyFeatures_management('Szosa_droga_L_layer',"ZL_104")

    arcpy.SelectLayerByAttribute_management('Szosa_droga_L_layer', "NEW_SELECTION", '"RTT"<>\'16\' AND "RTT"<>\'501\' AND "RST"=\'1\' AND "WD1"<7.4 AND "WD1">=5.5 AND "TUC"<>\'501\'')
    arcpy.CopyFeatures_management('Szosa_droga_L_layer',"ZL_105")

    arcpy.SelectLayerByAttribute_management('Szosa_droga_L_layer', "NEW_SELECTION", '"RTT"<>\'16\' AND "RTT"<>\'501\' AND "RST"=\'1\' AND "WD1"<5.5 AND "WD1">=3 AND "TUC"<>\'501\'')
    arcpy.CopyFeatures_management('Szosa_droga_L_layer',"ZL_106")

    arcpy.SelectLayerByAttribute_management('Szosa_droga_L_layer', "NEW_SELECTION", '(("RST"=\'1\' AND "WD1"<3) OR "RST"=\'2\') AND "TUC"<>\'501\'')
    arcpy.CopyFeatures_management('Szosa_droga_L_layer',"ZL_107")

    arcpy.SelectLayerByAttribute_management('Szosa_droga_L_layer', "NEW_SELECTION", '"RST"=\'6\' ')
    arcpy.CopyFeatures_management('Szosa_droga_L_layer',"ZL_108")

    arcpy.SelectLayerByAttribute_management('Szosa_droga_L_layer', "NEW_SELECTION", '"TUC"=\'501\' ')
    arcpy.CopyFeatures_management('Szosa_droga_L_layer',"ZL_018")
KlasyfikacjaDrog()

#generalizacja drogi
def Generalizacja_drog():
    arcpy.Dissolve_management("ZL_101","D:\mgr\M33033CD\droga\ZL101.shp") # Agreguje warstw? w oparciu o okre?lone atrybuty.
    arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL101.shp",20)     #integralno?ci wsp?lnych granic element?w znjaduj?cej sie w odleglosci 15

    arcpy.Dissolve_management("ZL_103","D:\mgr\M33033CD\droga\ZL103.shp")
    arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL103.shp",20)

    arcpy.Dissolve_management("ZL_104","D:\mgr\M33033CD\droga\ZL104.shp")
    arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL104.shp",20)

    arcpy.Dissolve_management("ZL_105","D:\mgr\M33033CD\droga\ZL105.shp")
    arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL105.shp",20)

    arcpy.Dissolve_management("ZL_106","D:\mgr\M33033CD\droga\ZL106.shp")
    arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL106.shp",20)

    arcpy.Dissolve_management("ZL_107","D:\mgr\M33033CD\droga\ZL107.shp")
    arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL107.shp",20)

    arcpy.Dissolve_management("ZL_108","D:\mgr\M33033CD\droga\ZL108.shp")
    arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL108.shp",20)

    arcpy.Dissolve_management("ZL_018","D:\mgr\M33033CD\droga\ZL018.shp")
    arcpy.Integrate_management("D:\mgr\M33033CD\droga\ZL018.shp",20)
Generalizacja_drog()

def Wygladzenie_lini_pow():
    arcpy.Dissolve_management("Rzeka_strum_L","D:\mgr\M33033CD\Rzeka.shp") # polaczenie w jedno aby kolejna funkcja dzialala
    arcpy.SimplifyLine_cartography("D:\mgr\M33033CD\Rzeka.shp","D:\mgr\M33033CD\Rzeka_L.shp","BEND_SIMPLIFY",200)

    arcpy.SimplifyPolygon_cartography("Las_A","D:\mgr\M33033CD\Las.shp","BEND_SIMPLIFY",200)

Wygladzenie_lini_pow()

#zapisuje wybrane elementy w bazie (dodawane sa tebele z wartosciami dlugosci i powierzchni obiektu)
def DodanieDoBazywarstwzshp():
    inFeaturesdrogi = ['D:\mgr\M33033CD\droga\ZL101.shp',
    'D:\mgr\M33033CD\droga\ZL103.shp',
    'D:\mgr\M33033CD\droga\ZL104.shp',
    'D:\mgr\M33033CD\droga\ZL105.shp',
    'D:\mgr\M33033CD\droga\ZL106.shp',
    'D:\mgr\M33033CD\droga\ZL107.shp',
    'D:\mgr\M33033CD\droga\ZL108.shp',
    'D:\mgr\M33033CD\droga\ZL018.shp',
    'D:\mgr\M33033CD\Rzeka_L.shp',
    'D:\mgr\M33033CD\Las.shp'
    ]
    arcpy.FeatureClassToGeodatabase_conversion(inFeaturesdrogi, outLocation)
DodanieDoBazywarstwzsh()
arcpy.Delete_management('Szosa_droga_L')




#Usuwa nie ?ywane warstwy wejsciowe

def UsuwanieWarstw():
    arcpy.Delete_management('Budynek_P_PAL015')
    arcpy.Delete_management('Budynek_A_AAL015')
    arcpy.Delete_management('Magazyn_skl_AAM010')
    arcpy.Delete_management('Ogrodzenie_LAL070')
    arcpy.Delete_management('Mur_ogrodze_LAL260')
    arcpy.Delete_management('Park_A_AAK120')
    arcpy.Delete_management('Zaklad_prze_AAC000')
    arcpy.Delete_management('Zaklad_prze_PAC000')
    arcpy.Delete_management('Drzewo_P_PEC030')
    arcpy.Delete_management('Kanal_row_L_LBH020')
    arcpy.Delete_management('Rzeka_strum_LBH140')
    arcpy.Delete_management('Droga_polna_LAP010')
    arcpy.Delete_management('Szosa_droga_LAP030')
    arcpy.Delete_management('Jezioro_sta_ABH080')
    arcpy.Delete_management('Las_A_AEC015')
    arcpy.Delete_management('Sad_plantac_AEA040')
    arcpy.Delete_management('Teren_zabud_AAL020')
    arcpy.Delete_management('Roslinnosc_AEB010')
    arcpy.Delete_management('Rezerwat_pr_AAL005')
    arcpy.Delete_management('ZL_101')
    arcpy.Delete_management('ZL_103')
    arcpy.Delete_management('ZL_104')
    arcpy.Delete_management('ZL_105')
    arcpy.Delete_management('ZL_106')
    arcpy.Delete_management('ZL_107')
    arcpy.Delete_management('ZL_108')
    arcpy.Delete_management('ZL_018')
    arcpy.Delete_management('Rzeka_strum_L')
    arcpy.Delete_management('Las_A')

UsuwanieWarstw()



