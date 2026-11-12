---
title: "Get Centerlines in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Centerlines_in_Drawing_Example_VB.htm"
---

# Get Centerlines in Drawing Example (VBA)

This example shows how to get all of the centerlines in all of the drawing views in a drawing.

```
'------------------------------------
' Preconditions:
' 1. Verify that the drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing.
' 2. Inserts a centerline annotation.
' 3. Prints the path and file name of the drawing document
'    to the Immediate window.
' 4. Iterates the sheet and drawing view, prints their names, and
'    prints the name of the centerline annotation to
'    the Immediate window.
' 5. Examine the Immediate window.
'
' NOTE: Because this drawing document is used elsewhere,
' do not save any changes.
'------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swDrawing As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim swCenterLine As SldWorks.Centerline
    Dim swAnnotation As SldWorks.Annotation
    Dim status  As Boolean
    Dim errors As Long
    Dim warnings As Long
    Dim fileName As String
```

```
    Set swApp = CreateObject("SldWorks.Application")
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20.SLDDRW"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swDrawing = swModel
    Set swModelDocExt = swModel.Extension
```

```
    status = swDrawing.ActivateView("Drawing View1")
    status = swModelDocExt.SelectByID2("cylinder20-9@Drawing View1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 0.513454307125032, 0.454946591641617, 250.013794595267, False, 0, Nothing, 0)
```

```
    Set swCenterLine = swDrawing.InsertCenterLine2()
    swModel.ClearSelection2 True
```

```
    Set swView = swDrawing.GetFirstView
    Debug.Print "File = " & swModel.GetPathName
```

```
    Do While Not swView Is Nothing
        Debug.Print "  View = " + swView.GetName2
        Set swCenterLine = swView.GetFirstCenterLine
        Do While Not swCenterLine Is Nothing
            Set swAnnotation = swCenterLine.GetAnnotation
            Debug.Print "    Name       = " & swAnnotation.GetName
            Set swCenterLine = swCenterLine.GetNext
        Loop
        Set swView = swView.GetNextView
    Loop
```

```
End Sub
```
