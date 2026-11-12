---
title: "Rotate and Copy 3D Sketch About Vector Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_and_Copy_3D_Sketch_About_Vector_Example_VB.htm"
---

# Rotate and Copy 3D Sketch About Vector Example (VBA)

This example shows how to rotate and copy 3D sketches about a vector.

```vb
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
Option Explicit

Sub main()

    Dim SwApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelData As SldWorks.SelectData
    Dim swSketchMgr As SldWorks.SketchManager
    Dim swSketch As SldWorks.Sketch
    Dim boolStatus As Boolean
    Dim varSketchSegments As Variant
    Dim i As Integer

    Set SwApp = Application.SldWorks
    ' If SOLIDWORKS Design is not running, then exit macro
    If SwApp Is Nothing Then Exit Sub

    ' Document with two 3D sketches, named 3DSketch2 and
    ' 3DSketch1, is open and active
    Set swModel = SwApp.ActiveDoc
    If swModel Is Nothing Then
        MsgBox "Failed to open document."
        Exit Sub
    End If

    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swSketchMgr = swModel.SketchManager

    ' Select 3DSketch2 sketch
    boolStatus = swModelDocExt.SelectByID2("3DSketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    If boolStatus = False Then
        MsgBox "Failed to select 3DSketch2 sketch."
        Exit Sub
    End If

    ' Open 3DSketch2 sketch in edit mode
    swModel.EditSketch
    Set swSketch = swSketchMgr.ActiveSketch
    If swSketch Is Nothing Then
        MsgBox "Failed to get pointer to 3DSketch2 sketch."
        Exit Sub
    End If

    ' Select all sketch segments in 3DSketch2 sketch
    varSketchSegments = swSketch.GetSketchSegments()
    For i = 0 To UBound(varSketchSegments)
        boolStatus = varSketchSegments(i).select4(True, swSelData)
        If boolStatus = False Then MsgBox "Failed to select sketch segment instance." & i & "."
    Next i

    ' Copy and rotate 3DSketch2 sketch about center
    ' point of 3DSketch1 sketch's arc
    Debug.Print "Rotating and copying 3DSketch2 sketch about the center point of 3DSketch1's arc? " & swSketchMgr.RotateOrCopy3DAboutVector(True, 1, True, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949)
    swModel.ClearSelection2 True
    ' Exit 3DSketch2 sketch
    swSketchMgr.InsertSketch True

    ' Select 3DSketch1 sketch
    boolStatus = swModelDocExt.SelectByID2("3DSketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    If boolStatus = False Then
        MsgBox "Failed to select 3DSketch1 sketch."
        Exit Sub
    End If

    ' Edit 3DSketch1 sketch
    swModel.EditSketch
    Set swSketch = swModel.GetActiveSketch2
    If swSketch Is Nothing Then
        MsgBox "Failed to get pointer to 3DSketch1 sketch."
        Exit Sub
    End If

    ' Select all sketch segments in 3DSketch1 sketch
    varSketchSegments = swSketch.GetSketchSegments()
    For i = 0 To UBound(varSketchSegments)
        boolStatus = varSketchSegments(i).select4(True, swSelData)
        If boolStatus = False Then
            MsgBox "Failed to select sketch segment instance." & i & "."
            Exit Sub
        End If
    Next i

    ' Rotate 3DSketch1 sketch about the
    ' center point of its own arc
    Debug.Print "Rotating 3DSketch1 sketch about the center point of its arc? " & swSketchMgr.RotateOrCopy3DAboutVector(False, 1, True, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949)
    swModel.ClearSelection2 True

    ' Exit 3DSketch1 sketch
    swSketchMgr.InsertSketch True

End Sub
```
