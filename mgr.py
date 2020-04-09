import os
import arcpy
#1
arcpy.CreateFileGDB_management("D:\mgr\M33033CD", "BAZA_2") # tworzymy baze
dane_wyjsc = "D:\mgr\M33033CD\BAZA_2.gdb"                    # definiujemy ta baze
arcpy.env.workspace = dane_wyjsc

#DODATKOWE
#Definiuje uk?ad wspolrzednych
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("ETRS 1989 UTM Zone 33N")

#2
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
#3
#zapisuje wybrane elementy w bazie (dodawane sa tebele z wartosciami dlugosci i powierzchni obiektu)
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)

#4
# Tworzy warstwe obiektow
#arcpy.CalculateField_management('Budynek_P_layer',"GMRotation",'!RCD!',"PYTHON") # oclicza w kat obrotu punktu (string ->double)

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



#5
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
#6
#Selekcja po atrybutach

def SelekcjaPoAtrybutach():
    arcpy.SelectLayerByAttribute_management('Budynek_A_layer', "NEW_SELECTION",' "Shape_Area" > 5400 ')
    arcpy.FeatureClassToFeatureClass_conversion('Budynek_A_layer', dane_wyjsc, 'Budynek_A')
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

#7
#Zapisuje wyselekcjonowanie elementy do bazy100

def FeatureClassToFeatureClass():
    arcpy.FeatureClassToFeatureClass_conversion('Budynek_A_layer', dane_wyjsc, 'Budynek_A')
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

#8
#Selekcja obiektow do stowrzenia nowych klas

def KlasyfikacjaBudynkow():
    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"BFC" = \'27\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Stacja_kol_P")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"BFC" = \'50\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Kosciol_swiatynia_P")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"BFC" = \'54\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Stacja_benz_P")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"BFC" = \'601\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Przystanek")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.SelectLayerByAttribute_management('Budynek_P_layer', "NEW_SELECTION", '"BFC" = \'7\' ')
    arcpy.CopyFeatures_management('Budynek_P_layer',"Obiekt_kut_P")
    arcpy.DeleteFeatures_management('Budynek_P_layer')

    arcpy.FeatureClassToFeatureClass_conversion('Budynek_P_layer', dane_wyjsc, 'Budynek_P')

KlasyfikacjaBudynkow()

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
#zapisuje wybrane elementy w bazie (dodawane sa tebele z wartosciami dlugosci i powierzchni obiektu)

def DodanieDoBazyDrog():
    inFeaturesdrogi = ['D:\mgr\M33033CD\droga\ZL101.shp',
    'D:\mgr\M33033CD\droga\ZL103.shp',
    'D:\mgr\M33033CD\droga\ZL104.shp',
    'D:\mgr\M33033CD\droga\ZL105.shp',
    'D:\mgr\M33033CD\droga\ZL106.shp',
    'D:\mgr\M33033CD\droga\ZL107.shp',
    'D:\mgr\M33033CD\droga\ZL108.shp',
    'D:\mgr\M33033CD\droga\ZL018.shp']
    arcpy.FeatureClassToGeodatabase_conversion(inFeaturesdrogi, outLocation)

DodanieDoBazyDrog()
#arcpy.Delete_management('Szosa_droga_L')


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

UsuwanieWarstw()

feature = 'Budynek_P'

def NearAnalysisBudynki():
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
        NearAnalysisBudynki

#wywo?uje procedur? rekurencyjn?. B?dzie dzia?a? stopniowo szybciej, poniewa? za ka?dym razem b?dzie przechodzi? przez mniejsz? liczb? punkt?w
NearAnalysisBudynki()





