---
title: "Get Name of Drawing Zone Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Name_of_Drawing_Zone_Example_VB.htm"
---

# Get Name of Drawing Zone Example (VBA)

This example shows how to get the name of a drawing zone for the specified x and y coordinates.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that public_documents\samples\tutorial\api\assem20.slddrw exists.
' 2. Open the Immediate Window.
'
' Postconditions.
' 1. Opens the specified drawing.
' 2. Creates a new sheet named Test with four zones.
' 3. Gets the name of the drawing zone for the specified
'    x and y coordinates.
' 4. Examine the Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swDraw As SldWorks.DrawingDoc
Dim swSheet As SldWorks.Sheet
Dim swModel As SldWorks.ModelDoc2
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim x As Double
Dim y As Double
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem20.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swDraw = swModel
```

```
    Set swSheet = swDraw.GetCurrentSheet
    swDraw.ActivateSheet (swSheet.GetName)
```

```
    ' Create sheet Test with four zones
    status = swDraw.NewSheet4("Test", swDwgPaperSizes_e.swDwgPaperAsize, swDwgTemplates_e.swDwgTemplateAsize, 1, 1, True, "", 0, 0, "", 0.5, 0.5, 0.5, 0.5, 2, 2)
```

```
    swModel.ForceRebuild3 True
```

```
    Set swSheet = swDraw.GetCurrentSheet
    swDraw.ActivateSheet (swSheet.GetName)
```

```
    ' Set x and y coordinates on the sheet
    ' whose drawing zone name to get
    x = 0.201705822198041
    y = 2.42677238302502E-02
```

```
    ' Get the name of the drawing zone for x and y
    Dim drawingZoneName As String
    drawingZoneName = swSheet.GetDrawingZone(x, y)
    Debug.Print "Drawing zone name for specified x and y coordinates: " & drawingZoneName
```

```
End Sub
```
