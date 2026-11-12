---
title: "Import DXF File into Part Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Import_DXF_File_into_Part_Sketch_Example_VB.htm"
---

# Import DXF File into Part Sketch Example (VBA)

This example shows how to import a DXF file to a part sketch.

```
'-------------------------------------------------
' Preconditions:
' 1. Verify that the specified DXF file exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Imports the specified file into SOLIDWORKS Design.
' 2. Examine the Immediate window and graphics area.
'-------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim filename As String
    Dim longerrors As Long
    Dim retVal As Boolean
    filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\importexport\rainbow.DXF"
```

```
    Set swApp = Application.SldWorks
    Dim importData As SldWorks.ImportDxfDwgData
    Set importData = swApp.GetImportFileData(filename)
```

```
    ' Import method
    importData.ImportMethod("") = SwConst.swImportDxfDwg_ImportMethod_e.swImportDxfDwg_ImportToPartSketch
```

```
   ' Load the specified DXF/DWG file
    Dim newDoc As SldWorks.ModelDoc2
    Set newDoc = swApp.LoadFile4(filename, "", importData, longerrors)
```

```
   ' Gets
    Debug.Print "Part Sketch Gets:"
    Debug.Print "  Add constraints:   " & importData.AddSketchConstraints("")
    Debug.Print "  Merge points:      " & importData.GetMergePoints("")
    Debug.Print "  Merge distance:    " & (importData.GetMergeDistance("") * 1000#) & " mm"
    Debug.Print "  Import dimensions: " & importData.ImportDimensions("")
    Debug.Print "  Import hatch:      " & importData.ImportHatch("")
```

```
    'Sets    Debug.Print "Part Sketch Sets:"
    importData.AddSketchConstraints("") = True
    Debug.Print "  Add constraints:   " & importData.AddSketchConstraints("")
    retVal = importData.SetMergePoints("", True, 0.000002)
    Debug.Print "  Merge points:      " & retVal
    Debug.Print "  Merge distance:    " & (importData.GetMergeDistance("") * 1000#) & " mm"
    importData.ImportDimensions("") = True
    Debug.Print "  Import dimensions: " & importData.ImportDimensions("")
    importData.ImportHatch("") = False
    Debug.Print "  Import hatch:      " & importData.ImportHatch("")
```

```
End Sub
```
