import os
import arcpy

sciezka = arcpy.GetParameterAsText(0) # pobrania danych wej?ciowych
lok_baza = arcpy.GetParameterAsText(1)

#arcpy.CreateFileGDB_management("D:\mgr", "Baza100") # tworzymy baze
dane_wyjsc = "D:\mgr\Baza100.gdb"                    # definiujemy ta baze
arcpy.env.workspace = dane_wyjsc
#Selekcja obiektow
inFeatures = ['D:\mgr\SHP_M33035AB\Budynek_P_PAL015.shp',
 'D:\mgr\SHP_M33035AB\Budynek_A_AAL015.shp',
 'D:\mgr\SHP_M33035AB\Magazyn_skl_AAM010.shp',
 'D:\mgr\SHP_M33035AB\Ogrodzenie_LAL070.shp',
 'D:\mgr\SHP_M33035AB\Mur_ogrodze_LAL260.shp',
 'D:\mgr\SHP_M33035AB\Park_A_AAK120.shp',
 'D:\mgr\SHP_M33035AB\Stadion_amf_AAK160.shp',
 'D:\mgr\SHP_M33035AB\Stadion_amf_PAK160.shp']

outLocation = dane_wyjsc
#zapisuje wybrane elementy w bazie (dodawane sa tebele z wartosciami dlugosci i powierzchni obiektu)
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)

# Tworzy warstwe obiektow
arcpy.MakeFeatureLayer_management('Budynek_P_PAL015', 'Budynek_P_layer')
arcpy.MakeFeatureLayer_management('Budynek_A_AAL015', 'Budynek_A_layer')
arcpy.MakeFeatureLayer_management('Magazyn_skl_AAM010', 'Magazyn_skl_layer')
arcpy.MakeFeatureLayer_management('Ogrodzenie_LAL070', 'Ogrodzenie_layer')
arcpy.MakeFeatureLayer_management('Mur_ogrodze_LAL260', 'Mur_ogrodze_layer')
arcpy.MakeFeatureLayer_management('Park_A_AAK120', 'Park_layer')
arcpy.MakeFeatureLayer_management('Stadion_amf_AAK160', 'Stadion_amf_A_layer')
arcpy.MakeFeatureLayer_management('Stadion_amf_PAK160', 'Stadion_amf_P_layer')

#Selekcjonuje obiekty ktore nastepnie sa zamieniane na punktowe
arcpy.SelectLayerByAttribute_management('Stadion_amf_A_layer', "NEW_SELECTION",' "Shape_Area" < 15000 ')
arcpy.FeatureToPoint_management('Stadion_amf_A_layer', 'Stadion_amf_P_layer')

arcpy.SelectLayerByAttribute_management('Budynek_A_layer', "NEW_SELECTION",' "Shape_Area" < 2700 ')
arcpy.FeatureToPoint_management('Budynek_A_layer', 'Budynek_P')

#Selekcja po atrybutach
arcpy.SelectLayerByAttribute_management('Budynek_A_layer', "NEW_SELECTION",' "Shape_Area" > 2700 ')
arcpy.SelectLayerByAttribute_management('Magazyn_skl_layer', "NEW_SELECTION",' "Shape_Area" > 25000 ')
arcpy.SelectLayerByAttribute_management('Ogrodzenie_layer', "NEW_SELECTION",' "Shape_Length" > 500 ')
arcpy.SelectLayerByAttribute_management('Mur_ogrodze_layer', "NEW_SELECTION",' "Shape_Length" > 500 ')
arcpy.SelectLayerByAttribute_management('Park_layer', "NEW_SELECTION",' "Shape_Area" > 15000 ')
arcpy.SelectLayerByAttribute_management('Stadion_amf_A_layer', "NEW_SELECTION",' "Shape_Area" > 15000 ')
#Definiuje uk?ad wspolrzednych
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("ETRS 1989 UTM Zone 33N")

#Zapisuje wyselekcjonowanie elementy do bazy100
arcpy.FeatureClassToFeatureClass_conversion('Budynek_A_layer', dane_wyjsc, 'Budynek_A')
arcpy.FeatureClassToFeatureClass_conversion('Budynek_P_layer', dane_wyjsc, 'Budynek_P')
arcpy.FeatureClassToFeatureClass_conversion('Magazyn_skl_layer', dane_wyjsc, 'Magazyn_skl')
arcpy.FeatureClassToFeatureClass_conversion('Ogrodzenie_layer', dane_wyjsc, 'Ogrodzenie')
arcpy.FeatureClassToFeatureClass_conversion('Mur_ogrodze_layer', dane_wyjsc, 'Mur_ogrodze')
arcpy.FeatureClassToFeatureClass_conversion('Park_layer', dane_wyjsc, 'Park')
arcpy.FeatureClassToFeatureClass_conversion('Stadion_amf_A_layer', dane_wyjsc, 'Stadion_amf_A')
arcpy.FeatureClassToFeatureClass_conversion('Stadion_amf_P_layer', dane_wyjsc, 'Stadion_amf_P')

#Usuwa nie ?ywane warstwy wejsciowe
arcpy.Delete_management('Budynek_P_PAL015')
arcpy.Delete_management('Budynek_A_AAL015')
arcpy.Delete_management('Magazyn_skl_AAM010')
arcpy.Delete_management('Ogrodzenie_LAL070')
arcpy.Delete_management('Mur_ogrodze_LAL260')
arcpy.Delete_management('Park_A_AAK120')
arcpy.Delete_management('Stadion_amf_AAK160')
arcpy.Delete_management('Stadion_amf_PAK160')



