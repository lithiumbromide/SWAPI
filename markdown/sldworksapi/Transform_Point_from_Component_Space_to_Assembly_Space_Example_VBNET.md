---
title: "Transform Point from Component Space to Assembly Space Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Transform_Point_from_Component_Space_to_Assembly_Space_Example_VBNET.htm"
---

# Transform Point from Component Space to Assembly Space Example (VB.NET)

This example shows how to transform a point from component space to assembly space.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Selects a component.
' 3. Transforms the component's origin to a point in
'    assembly space.
' 4. Examine the Immediate window.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swMathUtil As MathUtility
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swComp As Component2
        Dim swXform As MathTransform
        Dim nPt(2) As Double
        Dim vPt As Object
        Dim swPt As MathPoint
        Dim bRet As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        ' Open assembly
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\smartcomponents\stepped_shaft.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        bRet = swModelDocExt.SelectByID2("stepped_shaft-1@stepped_shaft", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

        swMathUtil = swApp.GetMathUtility
        swSelMgr = swModel.SelectionManager
        swComp = swSelMgr.GetSelectedObjectsComponent(1)
        swXform = swComp.Transform2

        ' Point at component origin
        nPt(0) = 0.0#
        nPt(1) = 0.0#
        nPt(2) = 0.0#
        vPt = nPt
        swPt = swMathUtil.CreatePoint(vPt)
        swPt = swPt.MultiplyTransform(swXform)
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("  Component = " & swComp.Name2 & " [" & swComp.GetPathName & "]")
        Debug.Print("    Point in component = (" & nPt(0) * 1000.0# & ", " & nPt(1) * 1000.0# & ", " & nPt(2) * 1000.0# & ") mm")
        Debug.Print("    Point in assembly = (" & swPt.ArrayData(0) * 1000.0# & ", " & swPt.ArrayData(1) * 1000.0# & ", " & swPt.ArrayData(2) * 1000.0# & ") mm")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
