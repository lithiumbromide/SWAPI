---
title: "Get Edge Chamfer Distances Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Chamfer_Distances_Example_VB.htm"
---

# Get Edge Chamfer Distances Example (VBA)

This example shows how to get the distances of the edges and vertices for the chamfer feature.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Creates a chamfer feature.
' 3. Examine the Immediate window for the chamfer data.
'
' NOTE: Because this part document is used elsewhere, do not
' save any changes.
'---------------------------------------------------------------------------
Option Explicit
```

```
Sub main()

    ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
    Const DegPerRad As Double = 57.3
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swFeat As SldWorks.Feature
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swChamfer As SldWorks.ChamferFeatureData2
    Dim vEdgeArr As Variant
    Dim vEdge As Variant
    Dim swEdge As SldWorks.Edge
    Dim swEnt As SldWorks.Entity
    Dim swSelData As SldWorks.SelectData
    Dim i As Long
    Dim bRet As Boolean
    Dim errors As Long
    Dim warnings As Long
    Dim fileName As String
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Create and select chamfer feature
    bRet = swModelDocExt.SelectByID2("", "EDGE", -6.21980171204655E-02, 3.94066118978458E-02, -5.46079442074188E-04, True, 0, Nothing, 0)
    bRet = swModelDocExt.SelectByID2("", "EDGE", -3.81606508724985E-02, 3.96345009388028E-02, 4.93384681956286E-02, True, 0, Nothing, 1)
    Set swFeatMgr = swModel.FeatureManager
    Set swFeat = swFeatMgr.InsertFeatureChamfer(4, 1, 0.00254, 0.78539816339745, 0, 0, 0, 0)
    bRet = swModelDocExt.SelectByID2("Chamfer1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swChamfer = swFeat.GetDefinition
```

```
    'Get chamfer information
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name
    Debug.Print "    EdgeChamferAngle          = " & swChamfer.EdgeChamferAngle * DegPerRad & " degrees"
    Debug.Print "    EqualDistance             = " & swChamfer.EqualDistance
    Debug.Print "    EdgeChamferDistance(0)    = " & swChamfer.GetEdgeChamferDistance(0) * 1000# & " mm"
    Debug.Print "    EdgeChamferDistance(1)    = " & swChamfer.GetEdgeChamferDistance(1) * 1000# & " mm"
    Debug.Print "    VertexChamferDistance(0)  = " & swChamfer.GetVertexChamferDistance(0) * 1000# & " mm"
    Debug.Print "    VertexChamferDistance(1)  = " & swChamfer.GetVertexChamferDistance(1) * 1000# & " mm"
    Debug.Print "    VertexChamferDistance(2)  = " & swChamfer.GetVertexChamferDistance(2) * 1000# & " mm"
    Debug.Print "    KeepFeatures              = " & swChamfer.KeepFeatures
    Debug.Print "    GetFaceCount              = " & swChamfer.GetFaceCount
    Debug.Print "    GetEdgeCount              = " & swChamfer.GetEdgeCount
    Debug.Print "    Type                      = " & swChamfer.Type
        ' ChamferFeatureData2::Type
        '   1 = Angle-Distance
        '   2 = Distance-Distance
        '   3 = Vertex
    'Roll back to get access to geometric entities
    bRet = swChamfer.AccessSelections(swModel, Nothing): Debug.Assert bRet
    vEdgeArr = swChamfer.Edges

    If Not IsEmpty(vEdgeArr) Then
        swModel.ClearSelection2 True
        i = 0
        bRet = False
        For Each vEdge In vEdgeArr
            Set swEdge = vEdge
            Set swEnt = swEdge
            bRet = swEnt.Select4(True, swSelData): Debug.Assert bRet
            Debug.Print "    EdgeFlip(" & i & ")              = " & swChamfer.GetIsFlipped(swEdge)
            i = i + 1
        Next
    End If
```

```
    'Roll forward
    swChamfer.ReleaseSelectionAccess
```

```
End Sub
```
