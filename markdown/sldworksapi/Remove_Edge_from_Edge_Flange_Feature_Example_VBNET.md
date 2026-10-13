---
title: "Remove Edge from Edge Flange Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Remove_Edge_from_Edge_Flange_Feature_Example_VBNET.htm"
---

# Remove Edge from Edge Flange Feature Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Sub Main()

        Dim swDocument As PartDoc
        Dim swSelectionManager As SelectionMgr
        Dim swEdgeFlangeData As EdgeFlangeFeatureData
        Dim swFeature As Feature
        Dim lNumEdges As Long
        Dim aEdgesToRemove() As Edge
        Dim lIdx As Long
        Dim bStatus As Boolean
        Dim lNumEdgesToRemove As Long
        Dim vEdgesToRemove As Object
        Dim vEdges As Object
        Dim nStatus As swEdgeFlangeError_e
        Dim modDocExt As ModelDocExtension

        swDocument = swApp.ActiveDoc
        swSelectionManager = swDocument.SelectionManager

        modDocExt = swDocument.Extension
        bStatus = modDocExt.SelectByID2("Edge-Flange1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionManager.GetSelectedObject6(1, 0)

        swDocument.ClearSelection2(True)

        swEdgeFlangeData = swFeature.GetDefinition
        swEdgeFlangeData.AccessSelections(swDocument, Nothing)
        vEdges = swEdgeFlangeData.Edges
        lNumEdges = UBound(vEdges) - LBound(vEdges) + 1
        Debug.Print("Number of edges in edge flange = " & swEdgeFlangeData.GetEdgeCount())
        '
        ' Select number of edges to remove.
        '
        lNumEdgesToRemove = 1

        vEdgesToRemove = Nothing

        If (lNumEdgesToRemove >= 1) Then
            ReDim aEdgesToRemove(lNumEdgesToRemove - 1)
            For lIdx = 0 To (lNumEdgesToRemove - 1)
                aEdgesToRemove(lIdx) = vEdges(lIdx)
            Next lIdx
            vEdgesToRemove = aEdgesToRemove
        End If

        nStatus = swEdgeFlangeData.RemoveEdges(vEdgesToRemove)
        Debug.Print("Edge removal error code = " & swEdgeFlangeError2String(nStatus))
        bStatus = swFeature.ModifyDefinition(swEdgeFlangeData, swDocument, Nothing)
        Debug.Print("Status of modify definition = " & bStatus)
```

```
        swEdgeFlangeData.AccessSelections(swDocument, Nothing)
        vEdges = Nothing

        vEdges = swEdgeFlangeData.Edges
        If (Not IsNothing(vEdges)) Then
            lNumEdges = UBound(vEdges) - LBound(vEdges) + 1
            Debug.Print("Number of edges in edge flange = " & lNumEdges)
        Else
            Debug.Print("Number of edges in edge flange = 0")
        End If
        swEdgeFlangeData.ReleaseSelectionAccess()

    End Sub

    Private Function swEdgeFlangeError2String(ByVal nStatus As swEdgeFlangeError_e) As String

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

    End Function

    Public swApp As SldWorks

End Class
```
