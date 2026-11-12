---
title: "Change Angle to Supplementary Angle Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Angle_to_Supplementary_Angle_Example_VBNET.htm"
---

# Change Angle to Supplementary Angle Example (VB.NET)

This example shows how to change the angle in an angular dimension to its supplementary angle.

```
'-----------------------------------------------------------
' Preconditions: Verify that the drawing exists.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Selects the angular dimension.
' 3. Changes the angle to its supplementary angle.
' 4. Examine the graphics area.
'
' NOTE: Because the drawing is used elsewhere, do not save
' changes.
'-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swDisplayDimension As DisplayDimension
        Dim status As Boolean
        Dim warnings As Integer
        Dim errors As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.slddrw"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Select angular dimension
        status = swModelDocExt.SelectByID2("RD1@Drawing View1", "DIMENSION", 0.115166498498499, 0.167429477477477, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swDisplayDimension = swSelectionMgr.GetSelectedObject6(1, -1)

        'Change angle to supplementary angle
        status = swDisplayDimension.SupplementaryAngle

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
