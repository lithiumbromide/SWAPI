---
title: "Get Coordinate System Transform Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Coordinate_System_Transform_Example_VB.htm"
---

# Get Coordinate System Transform Example (VBA)

This example shows how to get the default coordinate system transform for the selected feature.

```vb
'------------------------------------------
'
' Preconditions: Model document is open and a feature is selected.
'
' Postconditions: None
'
'-------------------------------------------
Option Explicit
Public Enum swUserPreferenceStringValue_e
    swFileSaveAsCoordinateSystem = 16
End Enum
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swDocExt                As SldWorks.ModelDocExtension
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swFeat                  As SldWorks.feature
    Dim swXform                 As SldWorks.MathTransform
    Dim sAxisName               As String
    Dim bRet                    As Boolean
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)

    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Current coordinate system = " & swModel.GetUserPreferenceStringValue(swFileSaveAsCoordinateSystem)
    Debug.Print ""

    sAxisName = swFeat.Name
    Set swXform = swDocExt.GetCoordinateSystemTransformByName(sAxisName)
    Debug.Print "  " & sAxisName
    Debug.Print "    Origin                    = (" & -1# * swXform.ArrayData(9) * 1000# & ", " & -1# * swXform.ArrayData(10) * 1000# & ", " & -1# * swXform.ArrayData(11) * 1000# & ") mm"
    Debug.Print "    Rotational sub-matrix 1   = (" & swXform.ArrayData(0) & ", " & swXform.ArrayData(1) & ", " & swXform.ArrayData(2) & ")"
    Debug.Print "    Rotational sub-matrix 2   = (" & swXform.ArrayData(3) & ", " & swXform.ArrayData(4) & ", " & swXform.ArrayData(5) & ")"
    Debug.Print "    Rotational sub-matrix 3   = (" & swXform.ArrayData(6) & ", " & swXform.ArrayData(7) & ", " & swXform.ArrayData(8) & ")"
    Debug.Print "    Translation vector       = (" & swXform.ArrayData(9) * 1000# & ", " & swXform.ArrayData(10) * 1000# & ", " & swXform.ArrayData(11) * 1000# & ") mm"
    Debug.Print "    Scale                     = " & swXform.ArrayData(12)
End Sub
'------------------------------------------
```
