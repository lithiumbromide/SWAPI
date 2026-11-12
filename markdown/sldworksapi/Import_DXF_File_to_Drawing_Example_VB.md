---
title: "Import DXF File to Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Import_DXF_File_to_Drawing_Example_VB.htm"
---

# Import DXF File to Drawing Example (VBA)

This example shows how to import a DXF file to a drawing.

```
'--------------------------------------
' Preconditions: Verify that the specified DXF file exists.
'
' Postconditions:
' 1. Imports the specified file into SOLIDWORKS.
' 2. Examine the drawing.
'---------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim filename As String
    Dim boolstatus As Boolean
    Dim longerrors As Long
```

```
    filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\importexport\rainbow.DXF"
```

```
    Set swApp = Application.SldWorks
```

```
' Get the specified DXF/DWG import data
    Dim importData As SldWorks.ImportDxfDwgData
    Set importData = swApp.GetImportFileData(filename)
```

```
' To let SOLIDWORKS Design determine an appropriate input file unit, do not set the LengthUnit property
'    importData.LengthUnit("") = SwConst.swLengthUnit_e.swMETER
'    importData.LengthUnit("") = SwConst.swLengthUnit_e.swFEET
'    importData.LengthUnit("Model") = SwConst.swLengthUnit_e.swFEET
'    importData.LengthUnit("Sheet2") = SwConst.swLengthUnit_e.swMETER
```

```
' To let SOLIDWORKS Design determine an appropriate output paper size, do not set the PaperSize values
'    boolstatus = importData.SetPaperSize("", SwConst.swDwgPaperSizes_e.swDwgPaperA3size, 0#, 0#)
'    boolstatus = importData.SetPaperSize("", SwConst.swDwgPaperSizes_e.swDwgPaperEsize, 0#, 0#)
'    boolstatus = importData.SetPaperSize("", SwConst.swDwgPaperSizes_e.swDwgPapersUserDefined, 0.5, 0.8)
'    boolstatus = importData.SetPaperSize("Model", SwConst.swDwgPaperSizes_e.swDwgPaperA3size, 0.5, 0.8)
'    boolstatus = importData.SetPaperSize("Sheet2", SwConst.swDwgPaperSizes_e.swDwgPapersUserDefined, 0.16, 0.14)
```

```
' To let SOLIDWORKS Design determine an appropriate sheet scale, do not set the SheetScale values
'    boolstatus = importData.SetSheetScale("", 1#, 12#)
'    boolstatus = importData.SetSheetScale("Model", 1#, 3#)
'    boolstatus = importData.SetSheetScale("Sheet2", 1#, 1#)
```

```
' To let SOLIDWORKS Design determine an appropriate sheet name, do not set the SheetName property
'    importData.SheetName("Model") = "S1"
'    importData.SheetName("Sheet2") = "S2"
```

```
' Load the specified DXF/DWG file
    Dim newDoc As SldWorks.ModelDoc2
    Set newDoc = swApp.LoadFile4(filename, "", importData, longerrors)
```

```
End Sub
```
