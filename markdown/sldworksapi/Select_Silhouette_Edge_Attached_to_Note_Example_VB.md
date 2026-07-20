---
title: "Select Silhouette Edge Attached to Note Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Silhouette_Edge_Attached_to_Note_Example_VB.htm"
---

# Select Silhouette Edge Attached to Note Example (VBA)

This example shows how to select a silhouette edge attached to a note in a
drawing.

```
'-------------------------------------------
' Preconditions:
' 1. Verify that the drawing to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing.
' 2. Activates Drawing View1.
' 3. Gets the note in Drawing View1
'    and the silhouette edge to which
'    the note is attached.
' 4. Examine the Immediate window and graphics area.
'---------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swView As SldWorks.View
Dim swSilhouetteEdge As SldWorks.SilhouetteEdge
Dim swNote As SldWorks.Note
Dim swAnnotation As SldWorks.Annotation
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim params As Variant
Dim obj As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\tutorial\api\cylinder20.SLDDRW"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swDrawing = swModel
    status = swDrawing.ActivateView("Drawing View1")
    Set swView = swDrawing.ActiveDrawingView
```

```
    ' Get note and any attached entities
    Set swNote = swView.GetFirstNote2
    Set swAnnotation = swNote.GetAnnotation
    params = swAnnotation.GetAttachedEntities3
    ' Select the silhouette edge to which the note is attached
    For Each obj In params
        Set swSilhouetteEdge = obj
        status = swSilhouetteEdge.Select2(False, Nothing)
        If status Then
            Debug.Print ("Silhouette edge selected.")
        End If
    Next
```

```
End Sub
```
