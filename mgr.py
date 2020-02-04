import os
import arcpy

sciezka = arcpy.GetParameterAsText(0) # pobrania danych wej?ciowych
lok_baza = arcpy.GetParameterAsText(1)

#arcpy.CreateFileGDB_management("D:\mgr", "Baza100") # tworzymy baze
dane_wyjsc = "D:\mgr\Baza100.gdb"                       # definiujemy ta baze
#baza_sciezka = os.path.join(sciezka, "Baza.gdb") # ?


arcpy.env.workspace = "D:\mgr\SHP_M33035AB"

pomnik =  "Pomnik_P_PAL130.shp"
pas_drzew = "Pas_drzew_z_LEA020.shp"
zakl_prze = "Zaklad_prze_AAC000.shp"
jezioro_staw = "Jezioro_sta_ABH080.shp"
rzeka = "Rzeka_strum_LBH140.shp"



#for fc in arcpy.ListFeatureClasses():
    #arcpy.AddField_management(fc, "Lenght", "DOUBLE")
    #with arcpy.da.UpdateCursor(fc, "Lenght") as cursor:
     #   for row in cursor:
      #  dlugosc = row[0]
     #   cursor.updateRow(row)


arcpy.MakeFeatureLayer_management(rzeka, 'rzeka_layer')


#pole_wektor = ["Length"]
#arcpy.AddField_management("rzeka_layer", pole_wektor[0], "DOUBLE")

#with arcpy.da.UpdateCursor('rzeka_layer', ["SHAPE@LENGTH", "Length"]) as cursor:
    #for row in cursor:
        #row[1] = row[0]
        #cursor.updateRow(row)


arcpy.SelectLayerByAttribute_management('rzeka_layer', "NEW_SELECTION",' "Length8" > 220 ')

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("ETRS 1989 UTM Zone 33N")

#arcpy.FeatureClassToFeatureClass_conversion('rzeka_layer', dane_wyjsc, 'Rzeka_strum_L')









