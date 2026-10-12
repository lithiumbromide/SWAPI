---
title: "Get Temporary Axis and Its Reference Face Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Temporary_Axis_and_Its_Reference_Face_Example_VBNET.htm"
---

# Get Temporary Axis and Its Reference Face Example (VB.NET)

This example shows how to get a temporary axis and its reference face.

```
'---------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\box.sldprt.
' 2. Click View > Hide/Show > Temporary Axes.
' 3. Select the temporary axis.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Gets whether the selected entity is a temporary
'    axis.
' 2. Gets the reference face of the temporary axis.
' 3. Examine the Immediate window and graphics area.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'---------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swEntity As Entity
        Dim swRefAxis As RefAxis
        Dim obj As Object
        Dim swFace As Face2

        swModel = swApp.ActiveDoc

        'Get selected entity
        swSelMgr = swModel.SelectionManager
        swFeature = swSelMgr.GetSelectedObject6(1, -1)
        swEntity = swFeature

        If swEntity.GetType = swSelectType_e.swSelDATUMAXES Then
            swRefAxis = swFeature.GetSpecificFeature2
            'Get whether selected entity is a temporary axis
            If swRefAxis.IsTempAxis Then
                Debug.Print("Is temporary reference axis")
                'Get reference face of temporary axis
                obj = swRefAxis.GetTempAxisReferenceFace
                If Not obj Is Nothing Then
                    Debug.Print("  Got reference face of temporary axis")
                    swFace = obj
                    swFace.Highlight(True)
                    Debug.Print("  Highlighted reference face of temporary axis; examine the graphics area")
                Else
                    Debug.Print("Did not get reference face of temporary axis")
                End If
            Else
                Debug.Print("Not a temporary axis")
            End If
        Else
            Debug.Print("Select a temporary axis and run the macro again")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks
End Class
```
