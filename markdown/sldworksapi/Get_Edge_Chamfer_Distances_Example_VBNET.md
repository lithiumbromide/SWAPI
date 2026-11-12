---
title: "Get Edge Chamfer Distances Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Chamfer_Distances_Example_VBNET.htm"
---

# Get Edge Chamfer Distances Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
        Const DegPerRad As Double = 57.3
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeat As Feature
        Dim swFeatMgr As FeatureManager
        Dim swSelMgr As SelectionMgr
        Dim swChamfer As ChamferFeatureData2
        Dim vEdgeArr As Object
        Dim vEdge As Object
        Dim swEdge As Edge
        Dim swEnt As Entity
        Dim swSelData As SelectData
        Dim i As Integer
        Dim bRet As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Create and select chamfer feature
        bRet = swModelDocExt.SelectByID2("", "EDGE", -0.0621980171204655, 0.0394066118978458, -0.000546079442074188, True, 0, Nothing, 0)
        bRet = swModelDocExt.SelectByID2("", "EDGE", -0.0381606508724985, 0.0396345009388028, 0.0493384681956286, True, 0, Nothing, 1)
        swFeatMgr = swModel.FeatureManager
        swFeat = swFeatMgr.InsertFeatureChamfer(4, 1, 0.00254, 0.78539816339745, 0, 0, 0, 0)
        bRet = swModelDocExt.SelectByID2("Chamfer1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        swSelData = swSelMgr.CreateSelectData
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        swChamfer = swFeat.GetDefinition

        'Get chamfer information
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("  " & swFeat.Name)
        Debug.Print("    EdgeChamferAngle          = " & swChamfer.EdgeChamferAngle * DegPerRad & " degrees")
        Debug.Print("    EqualDistance             = " & swChamfer.EqualDistance)
        Debug.Print("    EdgeChamferDistance(0)    = " & swChamfer.GetEdgeChamferDistance(0) * 1000.0# & " mm")
        Debug.Print("    EdgeChamferDistance(1)    = " & swChamfer.GetEdgeChamferDistance(1) * 1000.0# & " mm")
        Debug.Print("    VertexChamferDistance(0)  = " & swChamfer.GetVertexChamferDistance(0) * 1000.0# & " mm")
        Debug.Print("    VertexChamferDistance(1)  = " & swChamfer.GetVertexChamferDistance(1) * 1000.0# & " mm")
        Debug.Print("    VertexChamferDistance(2)  = " & swChamfer.GetVertexChamferDistance(2) * 1000.0# & " mm")
        Debug.Print("    KeepFeatures              = " & swChamfer.KeepFeatures)
        Debug.Print("    GetFaceCount              = " & swChamfer.GetFaceCount)
        Debug.Print("    GetEdgeCount              = " & swChamfer.GetEdgeCount)
        Debug.Print("    Type                      = " & swChamfer.Type)
        ' ChamferFeatureData2::Type
        '   1 = Angle-Distance
        '   2 = Distance-Distance
        '   3 = Vertex
        'Roll back to get access to geometric entities
        bRet = swChamfer.AccessSelections(swModel, Nothing) : Debug.Assert(bRet)
        vEdgeArr = swChamfer.Edges

        If Not IsNothing(vEdgeArr) Then
            swModel.ClearSelection2(True)
            i = 0
            bRet = False
            For Each vEdge In vEdgeArr
                swEdge = vEdge
                swEnt = swEdge
                bRet = swEnt.Select4(True, swSelData) : Debug.Assert(bRet)
                Debug.Print("    EdgeFlip(" & i & ")              = " & swChamfer.GetIsFlipped(swEdge))
                i = i + 1
            Next
        End If

        'Roll forward
        swChamfer.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
