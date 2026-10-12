---
title: "Rotate Move Face Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Move_Face_Feature_Example_VBNET.htm"
---

# Rotate Move Face Feature Example (VB.NET)

This example shows how to rotate (draft) a Move Face feature by changing the XYZ origin and rotation angles.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document that contains a Move Face feature named Move Face1.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Rotates (drafts) the Move Face feature.
 ' 2. Examine the Immediate window.
 '----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Math

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swFeat As Feature
        Dim swMoveFaceFeatData As MoveFaceFeatureData
        Dim varPara As Object
        Dim newPara(5) As Double
        Dim newVarPara As Object
        Dim boolstatus As Boolean
        Dim PI As Double
        Dim i As Long

        ' Set PI
        PI = 4 * Atan(1)

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager
        swModelDocExt = swModel.Extension

        ' Select, get, and access Move Face feature
        boolstatus = swModelDocExt.SelectByID2("Move Face1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        swMoveFaceFeatData = swFeat.GetDefinition
        swMoveFaceFeatData.AccessSelections(swModel, Nothing)

        ' Get current XYZ location and rotation angles of Move Face feature
        Debug.Print("Before rotating Move Face feature...")
        ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
        Debug.Print("  Draft angle of Move Face feature: " & swMoveFaceFeatData.Angle * 57.3 & " degrees")
        Debug.Print("  XYZ origin (first 3) and rotation angles (last 3)")
        varPara = swMoveFaceFeatData.TriadRotationParameters
        For i = LBound(varPara) To UBound(varPara)
            Debug.Print("    " & (varPara(i)))
        Next i

        ' New XYZ location and rotation angle values
        newPara(0) = 0.0#
        newPara(1) = 0.0#
        newPara(2) = 0.0#
        newPara(3) = 2 * PI / 180 ' Convert radians to degrees
        newPara(4) = 2 * PI / 180 ' Convert radians to degrees
        newPara(5) = 0.0#
        newVarPara = newPara

        ' Rotate the MoveFace feature
        swMoveFaceFeatData.TriadRotationParameters = newVarPara
        Debug.Print(" ")
        Debug.Print("After rotating Move Face feature...")
        Debug.Print("  Draft angle of Move Face feature: " & swMoveFaceFeatData.Angle * 57.3 & " degrees")
        Debug.Print("  XYZ origin (first 3) and rotation angles (last 3)")
        newVarPara = swMoveFaceFeatData.TriadRotationParameters
        For i = LBound(newVarPara) To UBound(newVarPara)
            Debug.Print("    " & (newVarPara(i)))
        Next i

        ' Modify the Move Face feature
        swFeat.ModifyDefinition(swMoveFaceFeatData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
