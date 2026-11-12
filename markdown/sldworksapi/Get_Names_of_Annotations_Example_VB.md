---
title: "Get Names of Annotations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Annotations_Example_VB.htm"
---

# Get Names of Annotations Example (VBA)

This example shows show to:

- get the names of all of the annotations in a drawing.
- select all of the annotations in a drawing.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Iterates the drawing views and gets and selects
'    each annotation in each drawing view.
' 3. Examine the Immediate window and drawing.
'--------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swDrawing As SldWorks.DrawingDoc
Dim swDrView As SldWorks.View
Dim annArray As Variant
Dim obj As Variant
Dim currAnn As SldWorks.Annotation
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
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20.SLDDRW"
    Set swDrawing = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

    'Get drawing views and names of annotations in
    'each drawing view
    Set swDrView = swDrawing.GetFirstView
    'First drawing view is the sheet, so get first drawing view
    Set swDrView = swDrView.GetNextView
```

```
    While Not swDrView Is Nothing
        Debug.Print "Name of drawing view: " & swDrView.GetName2
        annArray = swDrView.GetAnnotations
        If Not IsEmpty(annArray) Then
            For Each obj In annArray
                Set currAnn = obj
                Debug.Print "  Name of annotation: " & currAnn.GetName
                currAnn.Select3 True, Nothing
            Next obj
        End If
        Set swDrView = swDrView.GetNextView
```

```
    Wend
```

```
End Sub
```
