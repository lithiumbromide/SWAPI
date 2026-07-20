---
title: "Select Silhouette Edge Attached to Note Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Silhouette_Edge_Attached_to_Note_Example_VBNET.htm"
---

# Select Silhouette Edge Attached to Note Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swDrawing As DrawingDoc
    Dim swView As View
    Dim swSilhouetteEdge As SilhouetteEdge
    Dim swNote As Note
    Dim swAnnotation As Annotation
    Dim status As Boolean
    Dim errors As Integer
    Dim warnings As Integer
    Dim fileName As String
    Dim params As Object
    Dim obj As Object

    Sub Main()

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2025\samples\tutorial\api\cylinder20.SLDDRW"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swDrawing = swModel
        status = swDrawing.ActivateView("Drawing View1")
        swView = swDrawing.ActiveDrawingView

        ' Get note and any attached entities
        swNote = swView.GetFirstNote2
        swAnnotation = swNote.GetAnnotation
        params = swAnnotation.GetAttachedEntities3
        ' Select the silhouette edge to which the note is attached
        For Each obj In params
            swSilhouetteEdge = obj
            status = swSilhouetteEdge.Select2(False, Nothing)
            If status Then
                Debug.Print("Silhouette edge selected.")
            End If
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
