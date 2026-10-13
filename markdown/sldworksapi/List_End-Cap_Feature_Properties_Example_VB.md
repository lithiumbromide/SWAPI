---
title: "List End-Cap Feature Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/List_End-Cap_Feature_Properties_Example_VB.htm"
---

# List End-Cap Feature Properties Example (VBA)

This example shows how to list an end-cap feature's properties and select and then deselect the face used to create the end-cap feature.

```vb
'------------------------------------
'
' Preconditions: Model document is open and an end-cap feature is selected.
'
' Postcondtions: None
'
'------------------------------------
Option Explicit
Public Enum swSketchSegments_e
    swSketchLINE = 0
    swSketchARC = 1
    swSketchELLIPSE = 2
    swSketchSPLINE = 3
    swSketchTEXT = 4
    swSketchPARABOLA = 5
End Enum
Public Enum swSolidworksWeldmentEndCondOptions_e
    swEndConditionNone = 0
    swEndConditionMiter = 1
    swEndConditionButt1 = 2
    swEndConditionButt2 = 3
    swEndConditionTrim = 4
    swEndConditionUseDefault = 5
End Enum
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swFeat                  As SldWorks.feature
    Dim swEndCap                As SldWorks.EndCapFeatureData
    Dim swFace                  As SldWorks.face2
    Dim swEnt                   As SldWorks.Entity
    Dim i                       As Long
    Dim bRet                    As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swEndCap = swFeat.GetDefinition

    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name
    Debug.Print "    ChamferDistance                = " & swEndCap.ChamferDistance * 1000# & " mm"
    Debug.Print "    OffsetDistance                 = " & swEndCap.OffsetDistance * 1000# & " mm"
    Debug.Print "    Thickness                      = " & swEndCap.Thickness * 1000# & " mm"
    Debug.Print "    ThicknessRatioForOffset        = " & swEndCap.ThicknessRatioForOffset
    Debug.Print "    UseChamferCorners              = " & swEndCap.UseChamferCorners
    Debug.Print "    UseThicknessRatioForOffset     = " & swEndCap.UseThicknessRatioForOffset

    bRet = swEndCap.AccessSelections(swModel, Nothing): Debug.Assert bRet

    Set swFace = swEndCap.Face
    Set swEnt = swFace

    bRet = swEnt.Select4(False, Nothing): Debug.Assert bRet
    Stop

    swEndCap.ReleaseSelectionAccess
End Sub
```
