---
title: "Remove Edge from Edge Flange Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Edge_from_Edge_Flange_Feature_Example_VB.htm"
---

# Remove Edge from Edge Flange Feature Example (VBA)

This example shows how to remove an edge from an edge flange feature in a sheet metal part.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\SM1-remove-edges.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Removes an edge from Edge-Flange1.
' 2. Examine the Immediate window.
'
' NOTE: Because the model is used elsewhere, do not save changes.
' ---------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp               As SldWorks.SldWorks
    Dim swDocument          As SldWorks.PartDoc
    Dim swSelectionManager  As SldWorks.SelectionMgr
    Dim swEdgeFlangeData    As SldWorks.EdgeFlangeFeatureData
    Dim swFeature           As SldWorks.Feature
    Dim lNumEdges           As Long
    Dim aEdgesToRemove()    As SldWorks.Edge
    Dim lIdx                As Long
    Dim bStatus             As Boolean
    Dim lNumEdgesToRemove   As Long
    Dim vEdgesToRemove      As Variant
    Dim vEdges              As Variant
    Dim nStatus             As SwConst.swEdgeFlangeError_e
```

```
    Set swApp = Application.SldWorks
    Set swDocument = swApp.ActiveDoc
    Set swSelectionManager = swDocument.SelectionManager
```

```
    bStatus = swDocument.Extension.SelectByID2("Edge-Flange1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionManager.GetSelectedObject6(1, 0)
```

```
    swDocument.ClearSelection2 True
```

```
    Set swEdgeFlangeData = swFeature.GetDefinition
    swEdgeFlangeData.AccessSelections swDocument, Nothing
    Debug.Print "Number of edges: " & swEdgeFlangeData.GetEdgeCount
    vEdges = swEdgeFlangeData.Edges
    lNumEdges = UBound(vEdges) - LBound(vEdges) + 1
```

```
    '
    ' Select number of edges to remove
    '
    Select Case (1)
        Case 1
            ' Remove one edge
            lNumEdgesToRemove = 1
```

```
        Case 2
            ' Remove all edges
            lNumEdgesToRemove = lNumEdges
```

```
        Case 3
            ' Remove no edges
            lNumEdgesToRemove = 0
```

```
    End Select
```

```
    vEdgesToRemove = Empty
```

```
    If (lNumEdgesToRemove >= 1) Then
        ReDim aEdgesToRemove(lNumEdgesToRemove - 1)
        For lIdx = 0 To (lNumEdgesToRemove - 1)
            Set aEdgesToRemove(lIdx) = vEdges(lIdx)
        Next lIdx
        vEdgesToRemove = aEdgesToRemove
    End If
```

```
    nStatus = swEdgeFlangeData.RemoveEdges(vEdgesToRemove)
    Debug.Print "Edge removal error code = " & swEdgeFlangeError2String(nStatus)
```

```
    bStatus = swFeature.ModifyDefinition(swEdgeFlangeData, swDocument, Nothing)
    Debug.Print "Status of modify definition = " & bStatus
```

```
    swEdgeFlangeData.AccessSelections swDocument, Nothing
```

```
    vEdges = Empty
    vEdges = swEdgeFlangeData.Edges
```

```
    If (Not IsEmpty(vEdges)) Then
        lNumEdges = UBound(vEdges) - LBound(vEdges) + 1
        Debug.Print "Number of edges in edge flange = " & lNumEdges
    Else
        Debug.Print "Number of edges in edge flange = 0"
    End If
```

```
    swEdgeFlangeData.ReleaseSelectionAccess
```

```
End Sub
```

```
Private Function swEdgeFlangeError2String(ByVal nStatus As SwConst.swEdgeFlangeError_e) As String
```

```
    Select Case (nStatus)
        Case 0
            swEdgeFlangeError2String = "no error"
        Case swEdgeFlangeError_e.swEdgeFlangeError_EdgeAlreadyExists
            swEdgeFlangeError2String = "edge already exists"
        Case swEdgeFlangeError_e.swEdgeFlangeError_EdgeNotSpecified
            swEdgeFlangeError2String = "edge not specified"
        Case swEdgeFlangeError_e.swEdgeFlangeError_NumberOfEdgesAndSketchesNotEqual
            swEdgeFlangeError2String = "number mismatch"
        Case swEdgeFlangeError_e.swEdgeFlangeError_SketchNotSpecified
            swEdgeFlangeError2String = "sketch not specified"
        Case Else
            swEdgeFlangeError2String = "unknown error"
    End Select
```

```
End Function
```
