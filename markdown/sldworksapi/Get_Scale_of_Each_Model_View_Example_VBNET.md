---
title: "Get Scale Factor of Each Model View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Scale_of_Each_Model_View_Example_VBNET.htm"
---

# Get Scale Factor of Each Model View Example (VB.NET)

This example shows how to get the scale factor of each model view in a part document.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Click Window > Viewport > Four View.
' 3. Click a model view and spin the middle-mouse
'    button forward or back.
' 4. Open the Immediate Window.
'
' Postconditions:
' 1. Gets the number of model views in the part document.
' 2. Gets the scale factor of each model view.
' 3. Examine the Immediate Window.
'-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim SwModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swModView As ModelView
        Dim swModViews As Object
        Dim index As Integer
        Dim Count As Integer

        SwModel = swApp.ActiveDoc
        swModelDocExt = SwModel.Extension

        ' Get model views
        swModViews = swModelDocExt.GetModelViews

        ' Get number of model views
        Count = swModelDocExt.GetModelViewCount
        Debug.Print("Number of model views: " & Count)

        ' Get the scale factor of each model view
        For index = LBound(swModViews) To UBound(swModViews)
            swModView = swModViews(index)
            Debug.Print("Scale of this model view is: " & swModView.Scale2)
        Next index

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
