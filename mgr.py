import os
import arcpy
#1
arcpy.CreateFileGDB_management("D:\mgr", "Baza100") # tworzymy baze
dane_wyjsc = "D:\mgr\Baza100.gdb"                    # definiujemy ta baze
arcpy.env.workspace = dane_wyjsc
#2
#Selekcja obiektow
inFeatures = ['D:\mgr\SHP_M33035AB\Budynek_P_PAL015.shp',
 'D:\mgr\SHP_M33035AB\Budynek_A_AAL015.shp',
 'D:\mgr\SHP_M33035AB\Magazyn_skl_AAM010.shp',
 'D:\mgr\SHP_M33035AB\Ogrodzenie_LAL070.shp',
 'D:\mgr\SHP_M33035AB\Mur_ogrodze_LAL260.shp',
 'D:\mgr\SHP_M33035AB\Park_A_AAK120.shp',
 'D:\mgr\SHP_M33035AB\Zaklad_prze_AAC000.shp',
 'D:\mgr\SHP_M33035AB\Zaklad_prze_PAC000.shp',
 'D:\mgr\SHP_M33035AB\Drzewo_P_PEC030.shp',
 'D:\mgr\SHP_M33035AB\Kanal_row_L_LBH020.shp',
 'D:\mgr\SHP_M33035AB\Rzeka_strum_LBH140.shp',
 'D:\mgr\SHP_M33035AB\Droga_polna_LAP010.shp',
 'D:\mgr\SHP_M33035AB\Szosa_droga_LAP030.shp',
 'D:\mgr\SHP_M33035AB\Jezioro_sta_ABH080.shp',
 'D:\mgr\SHP_M33035AB\Las_A_AEC015.shp',
 'D:\mgr\SHP_M33035AB\Sad_plantac_AEA040.shp',
 'D:\mgr\SHP_M33035AB\Teren_zabud_AAL020.shp',
 'D:\mgr\SHP_M33035AB\Roslinnosc_AEB010.shp',
 'D:\mgr\SHP_M33035AB\Rezerwat_pr_AAL005.shp']

outLocation = dane_wyjsc
#3
#zapisuje wybrane elementy w bazie (dodawane sa tebele z wartosciami dlugosci i powierzchni obiektu)
arcpy.FeatureClassToGeodatabase_conversion(inFeatures, outLocation)

#4
# Tworzy warstwe obiektow
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


#DODATKOWE
#Definiuje uk?ad wspolrzednych
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("ETRS 1989 UTM Zone 33N")

#5
#Selekcjonuje obiekty ktore nastepnie sa zamieniane na punktowe

arcpy.SelectLayerByAttribute_management('Budynek_A_layer', "NEW_SELECTION",' "Shape_Area" < 5400 ')
arcpy.FeatureToPoint_management('Budynek_A_layer', 'Budynek_P_layer')

arcpy.SelectLayerByAttribute_management('Zaklad_prze_A_layer', "NEW_SELECTION",' "Shape_Area" < 22000 ')
arcpy.FeatureToPoint_management('Zaklad_prze_A_layer', 'Zaklad_prze_P_layer')

arcpy.SelectLayerByAttribute_management('Las_A_layer', "NEW_SELECTION",' "Shape_Area" < 10000 ')
arcpy.FeatureToPoint_management('Las_A_layer', 'Drzewo_P_layer')

arcpy.SelectLayerByAttribute_management('Sad_plantac_A_layer', "NEW_SELECTION",' "Shape_Area" < 100000 ')
arcpy.FeatureToPoint_management('Sad_plantac_A_layer', 'Drzewo_P_layer')

#6
#Selekcja po atrybutach
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


#Zapisuje wyselekcjonowanie elementy do bazy100

arcpy.FeatureClassToFeatureClass_conversion('Budynek_P_layer', dane_wyjsc, 'Budynek_P')
arcpy.FeatureClassToFeatureClass_conversion('Budynek_A_layer', dane_wyjsc, 'Budynek_A')
arcpy.FeatureClassToFeatureClass_conversion('Magazyn_skl_A_layer', dane_wyjsc, 'Magazyn_skl_A')
arcpy.FeatureClassToFeatureClass_conversion('Ogrodzenie_L_layer', dane_wyjsc, 'Ogrodzenie_L')
arcpy.FeatureClassToFeatureClass_conversion('Mur_ogrodze_L_layer', dane_wyjsc, 'Mur_ogrodze_L')
arcpy.FeatureClassToFeatureClass_conversion('Park_A_layer', dane_wyjsc, 'Park_A')
arcpy.FeatureClassToFeatureClass_conversion('Zaklad_prze_A_layer', dane_wyjsc, 'Zaklad_prze_A')
arcpy.FeatureClassToFeatureClass_conversion('Zaklad_prze_P_layer', dane_wyjsc, 'Zaklad_prze_P')
arcpy.FeatureClassToFeatureClass_conversion('Drzewo_P_layer', dane_wyjsc, 'Drzewo_P_P')
arcpy.FeatureClassToFeatureClass_conversion('Kanal_row_L_layer', dane_wyjsc, 'Kanal_row_L')
arcpy.FeatureClassToFeatureClass_conversion('Rzeka_strum_L_layer', dane_wyjsc, 'Rzeka_strum_L')
arcpy.FeatureClassToFeatureClass_conversion('Droga_polna_L_layer', dane_wyjsc, 'Droga_polna_L')
arcpy.FeatureClassToFeatureClass_conversion('Szosa_droga_L_layer', dane_wyjsc, 'Szosa_droga_L')
arcpy.FeatureClassToFeatureClass_conversion('Jezioro_sta_A_layer', dane_wyjsc, 'Jezioro_sta_A')
arcpy.FeatureClassToFeatureClass_conversion('Las_A_layer', dane_wyjsc, 'Las_A')
arcpy.FeatureClassToFeatureClass_conversion('Sad_plantac_A_layer', dane_wyjsc, 'Sad_plantac_A')
arcpy.FeatureClassToFeatureClass_conversion('Teren_zabud_A_layer', dane_wyjsc, 'Teren_zabud_A')
arcpy.FeatureClassToFeatureClass_conversion('Roslinnosc_A_layer', dane_wyjsc, 'Roslinnosc_A')
arcpy.FeatureClassToFeatureClass_conversion('Rezerwat_pr_A_layer', dane_wyjsc, 'Rezerwat_pr_A')

#Usuwa nie ?ywane warstwy wejsciowe
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




arcpy.ApplySymbologyFromLayer_management("Budynek_P",r'D:\mgr\symbole\Budynek_P.lyr')

