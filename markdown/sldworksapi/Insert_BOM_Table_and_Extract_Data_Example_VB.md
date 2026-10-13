---
title: "Insert BOM Table and Extract Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_Extract_Data_Example_VB.htm"
---

# Insert BOM Table and Extract Data Example (VBA)

This example shows how to insert a BOM table and extract data from it.

```
'-------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document to open
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Selects a drawing view.
' 3. Inserts a BOM table at the point where the drawing
'    was selected.
' 4. Examine the drawing and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not
' save changes.
'-------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim swSelMgr As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim swBomTable As SldWorks.BomTableAnnotation
Dim swTable As SldWorks.TableAnnotation
Dim vPickPt As Variant
Dim nNumCol As Long
Dim nNumRow As Long
Dim sRowStr As String
Dim i As Long
Dim j As Long
Dim bRet As Boolean
Dim fileName As String
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open drawing document and select drawing view
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\driveworksxpress\mobile gantry.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swDrawing = swModel
    Set swModelDocExt = swModel.Extension
    bRet = swDrawing.ActivateView("Drawing View4")
    bRet = swModelDocExt.SelectByID2("Drawing View4", "DRAWINGVIEW", 0.130207615492954, 0.11628112033195, 0, False, 0, Nothing, 0)
```

```
    'Insert BOM table
    Set swSelMgr = swModel.SelectionManager
    Set swView = swSelMgr.GetSelectedObject6(1, -1)
    vPickPt = swSelMgr.GetSelectionPoint2(1, -1)
    Set swBomTable = swView.InsertBomTable2(False, vPickPt(0), vPickPt(1), swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, swBomType_e.swBomType_Indented, "", "")
    Set swTable = swBomTable
    nNumCol = swTable.ColumnCount
    nNumRow = swTable.RowCount
```

```
    'List BOM contents
    For i = 0 To nNumRow - 1
        sRowStr = ""
        For j = 0 To nNumCol - 1
            sRowStr = sRowStr & swTable.Text2(i, j, True) & ","
        Next j
        Debug.Print Left(sRowStr, Len(sRowStr) - 1)
    Next i
```

```
End Sub
```
