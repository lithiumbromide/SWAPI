---
title: "Rotate and Copy 3D Sketch About Vector Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_and_Copy_3D_Sketch_About_Vector_Example_VBNET.htm"
---

# Rotate and Copy 3D Sketch About Vector Example (VB.NET)

This example shows how to rotate and copy 3D sketches about a vector.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a part that contains two 3D sketches,
'    3DSketch1 and 3DSketch2.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Copies and rotates the 3DSketch2 sketch around
'    the center point of the 3DSketch1 sketch's arc.
' 2. Rotates the 3DSketch1 sketch around the center
'    point of its arc.
' 3. Examine the Immediate window.
'---------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swModelDocExt As ModelDocExtension
        Dim swSelData As SelectData
        Dim swSketchMgr As SketchManager
        Dim swSketch As Sketch
        Dim boolStatus As Boolean
        Dim varSketchSegments As Object
        Dim i As Integer

        ' If SOLIDWORKS isn't running,
        ' then exit
        If swApp Is Nothing Then Exit Sub

        ' Document with two 3D sketches, named 3DSketch2 and
        ' 3DSketch1, is open and active
        swModel = swApp.ActiveDoc
        If swModel Is Nothing Then
            MsgBox("Failed to open document.")
            Exit Sub
        End If

        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        swSelData = swSelMgr.CreateSelectData
        swSketchMgr = swModel.SketchManager

        ' Select 3DSketch2 sketch
        boolStatus = swModelDocExt.SelectByID2("3DSketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        If boolStatus = False Then
            MsgBox("Failed to select sketch 3DSketch2.")
            Exit Sub
        End If

        ' Open 3DSketch2 sketch in edit mode
        swModel.EditSketch()
        swSketch = swSketchMgr.ActiveSketch
        If swSketch Is Nothing Then
            MsgBox("Failed to get pointer to 3DSketch2 sketch.")
            Exit Sub
        End If

        ' Select all sketch segments in 3DSketch2 sketch
        varSketchSegments = swSketch.GetSketchSegments()
        For i = 0 To UBound(varSketchSegments)
            boolStatus = varSketchSegments(i).select4(True, swSelData)
            If boolStatus = False Then MsgBox("Failed to select sketch segment instance." & i & ".")
        Next i

        ' Copy and rotate 3DSketch2 sketch about center
        ' point of 3DSketch1 sketch's arc
        Debug.Print("Rotating and copying 3DSketch2 sketch about the center point of 3DSketch1's arc? " & swSketchMgr.RotateOrCopy3DAboutVector(True, 1, True, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949))
        swModel.ClearSelection2(True)

        ' Exit 3DSketch2 sketch
        swSketchMgr.InsertSketch(True)

        ' Select 3DSketch1 sketch
        boolStatus = swModelDocExt.SelectByID2("3DSketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        If boolStatus = False Then
            MsgBox("Failed to select sketch 3DSketch1.")
            Exit Sub
        End If

        ' Edit 3DSketch1 sketch
        swModel.EditSketch()
        swSketch = swModel.GetActiveSketch2
        If swSketch Is Nothing Then
            MsgBox("Failed to get pointer to sketch 3DSketch1.")
            Exit Sub
        End If

        ' Select all sketch segments in 3DSketch1 sketch
        varSketchSegments = swSketch.GetSketchSegments()
        For i = 0 To UBound(varSketchSegments)
            boolStatus = varSketchSegments(i).select4(True, swSelData)
            If boolStatus = False Then
                MsgBox("Failed to select sketch segment instance." & i & ".")
                Exit Sub
            End If
        Next i

        ' Rotate 3DSketch1 sketch about the
        ' center point of its arc
        Debug.Print("Rotating 3DSketch1 sketch about the center point of its arc? " & swSketchMgr.RotateOrCopy3DAboutVector(True, 1, True, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949))
        swModel.ClearSelection2(True)
        ' Exit 3DSketch1 sketch
        swSketchMgr.InsertSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
