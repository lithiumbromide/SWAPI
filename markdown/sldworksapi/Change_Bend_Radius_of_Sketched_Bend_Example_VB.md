---
title: "Change Bend Radius of Sketched Bend Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Bend_Radius_of_Sketched_Bend_Example_VB.htm"
---

# Change Bend Radius of Sketched Bend Example (VBA)

This example shows how to change the bend radius of a sketched bend.

```vb
'--------------------------------------------
 ' Preconditions:
 ' 1. Open a model document containing a sketched bend.
 ' 2. Sketched bend is selected.
 '
 ' Postconditions: Increases the size of bend radius
 ' of the selected sketched bend is increased by 1.5 times.
'---------------------------------------------
Option Explicit
Public Enum swFlangePositionTypes_e
    swFlangePositionTypeMaterialInside = 1
    swFlangePositionTypeMaterialOutside = 2
    swFlangePositionTypeBendOutside = 3
    swFlangePositionTypeBendCenterLine = 4
    swFlangePositionTypeBendSharp = 5
End Enum
Public Enum swBendAllowanceTypes_e
    swBendAllowanceBendTable = 1
    swBendAllowanceKFactor = 2
    swBendAllowanceDirect = 3
    swBendAllowanceDeduction = 4
End Enum
Sub DumpCustomBendAllowanceInfo _
( _
    sPadStr As String, _
    swCustBendAllow As SldWorks.CustomBendAllowance _
)
    Debug.Print sPadStr & "Type                     = " & swCustBendAllow.Type
    Debug.Print sPadStr & "BendAllowance            = " & swCustBendAllow.BendAllowance * 1000# & " mm"
    Debug.Print sPadStr & "BendDeduction            = " & swCustBendAllow.BendDeduction * 1000# & " mm"
    Debug.Print sPadStr & "BendTableFile            = " & swCustBendAllow.BendTableFile
    Debug.Print sPadStr & "KFactor                  = " & swCustBendAllow.KFactor
End Sub
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swSelMgr                As SldWorks.SelectionMgr
    Dim swSelData               As SldWorks.SelectData
    Dim swFeat                  As SldWorks.feature
    Dim swSketchBend            As SldWorks.SketchedBendFeatureData
    Dim swBendFeat              As SldWorks.BendsFeatureData
    Dim swCustBendAllow         As SldWorks.CustomBendAllowance
    Dim swFace                  As SldWorks.face2
    Dim swEnt                   As SldWorks.Entity
    Dim nFace_X                 As Double
    Dim nFace_Y                 As Double
    Dim nFace_Z                 As Double
    Dim i                       As Long
    Dim bRet                    As Boolean

    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSketchBend = swFeat.GetDefinition
    Set swCustBendAllow = swSketchBend.GetCustomBendAllowance

    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name
    '1 radian = 180º/p = 57.295779513º or approximately 57.3º
    Debug.Print "    BendAngle                  = " & swSketchBend.BendAngle * 57.3 & " deg"
    Debug.Print "    BendRadius                 = " & swSketchBend.BendRadius * 1000# & " mm"
    Debug.Print "    PositionType               = " & swSketchBend.PositionType
    Debug.Print "    ReverseDirection           = " & swSketchBend.ReverseDirection
    Debug.Print "    UseDefaultBendAllowance    = " & swSketchBend.UseDefaultBendAllowance
    Debug.Print "    UseDefaultBendRadius       = " & swSketchBend.UseDefaultBendRadius
    ' Roll back to get to fixed face
    bRet = swSketchBend.AccessSelections(swModel, Nothing): Debug.Assert bRet

    Set swFace = swSketchBend.GetFixedFace(nFace_X, nFace_Y, nFace_Z)
    Set swEnt = swFace

    Debug.Print "    Fixed Face                 = (" & nFace_X * 1000# & ", " & nFace_Y * 1000# & ", " & nFace_Z * 1000# & ") mm"

    Debug.Print "    Custom Bend Allowance:"
    DumpCustomBendAllowanceInfo "      ", swCustBendAllow

    bRet = swEnt.Select4(True, swSelData): Debug.Assert bRet

    ' Make some changes
    swSketchBend.UseDefaultBendRadius = False
    swSketchBend.BendRadius = swSketchBend.BendRadius * 1.5

    ' Apply changes
    bRet = swFeat.ModifyDefinition(swSketchBend, swModel, Nothing): Debug.Assert bRet
    End Sub
'--------------------------------------------
```
