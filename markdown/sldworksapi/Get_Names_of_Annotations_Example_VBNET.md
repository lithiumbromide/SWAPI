---
title: "Get Names of Annotations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Annotations_Example_VBNET.htm"
---

# Get Names of Annotations Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swDrawing As DrawingDoc
        Dim swDrView As View
        Dim annArray() As Object
        Dim obj As Object
        Dim currAnn As Annotation
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cylinder20.SLDDRW"
        swDrawing = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Get drawing views and names of annotations in
        'each drawing view
        swDrView = swDrawing.GetFirstView
        'First drawing view is the sheet, so get next drawing view
        swDrView = swDrView.GetNextView
        While Not swDrView Is Nothing
            Debug.Print("Name of drawing view: " & swDrView.GetName2)
            annArray = swDrView.GetAnnotations
            If Not annArray Is Nothing Then
                For Each obj In annArray
                    currAnn = obj
                    Debug.Print("  Name of annotation: " & currAnn.GetName)
                    currAnn.Select3(True, Nothing)
                Next obj
            End If
            swDrView = swDrView.GetNextView
        End While

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
