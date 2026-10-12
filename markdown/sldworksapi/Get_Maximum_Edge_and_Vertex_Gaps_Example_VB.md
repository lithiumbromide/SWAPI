---
title: "Get Maximum Edge and Vertex Gaps Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Maximum_Edge_and_Vertex_Gaps_Example_VB.htm"
---

# Get Maximum Edge and Vertex Gaps Example (VBA)

This example returns the same data returned by the Tools > Check dialog box when the check boxes, Maximum edge gap and Maximum vertex gap, are selected.

This example shows how to iterate over each edge and vertex in a part to obtain:

* Whether an edge or vertex is:

* tolerant (distance to neighbor is greater than 5.0E-9 mm).

* exact (distance to neighbor is less than or equal to 5.0E-9 mm).

* Gap size (or tolerance) in mm of each edge or vertex.

* Maximum edge and vertex gaps (or tolerances) in mm for the part.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\assemblymates\head.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window for tolerance data for all edges
 ' and vertexes.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2
    Dim swPart                  As SldWorks.PartDoc
    Dim vBodyArr                As Variant
    Dim vBody                   As Variant
    Dim swBody                  As SldWorks.Body2
    Dim vEdgeArr                As Variant
    Dim vEdge                   As Variant
    Dim swEdge                  As SldWorks.Edge
    Dim vVertexArr              As Variant
    Dim vVertex                 As Variant
    Dim swVertex                As SldWorks.Vertex
    Dim swFaultEnt              As SldWorks.FaultEntity
    Dim bRet                    As Boolean
    Dim tol                     As Double
    Dim swTanEnt                As SldWorks.Entity

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Debug.Print "File = " & swModel.GetPathName

    vBodyArr = swPart.GetBodies2(swAllBodies, True)
    For Each vBody In vBodyArr
        Set swBody = vBody
        Debug.Print "  Body[" & swBody.GetType & "] --> " & swBody.GetSelectionId
        vEdgeArr = swBody.GetEdges
        vVertexArr = swBody.GetVertices

        Dim maxEdgeGap As Double
        maxEdgeGap = 0#
        For Each vEdge In vEdgeArr
            ' Find maximum edge gap
            Set swEdge = vEdge
            bRet = swEdge.IsTolerant(tol)
            If maxEdgeGap < tol Then
                maxEdgeGap = tol
            End If
                If (Not (bRet = False)) Then
                    Debug.Print "Edge is tolerant:  "
                    Debug.Print "        Tolerance = " & tol
                    Set swTanEnt = swEdge
                    bRet = swTanEnt.Select4(True, Nothing)

                Else
                    Debug.Print "Edge is not tolerant:  Tolerance = " & tol
                End If
            Set swFaultEnt = swEdge.Check
        Next vEdge
        Debug.Print ""
        Debug.Print "Maximum edge gap is " & maxEdgeGap
        Debug.Print ""

        Dim maxVertexGap As Double
        maxVertexGap = 0#

        For Each vVertex In vVertexArr
            ' Find maximum vertex gap
            Set swVertex = vVertex
            bRet = swVertex.IsTolerant(tol)

            If maxVertexGap < tol Then
                maxVertexGap = tol
            End If

            If (Not (bRet = False)) Then
                Debug.Print "Vertex is tolerant:  "
                Debug.Print "       Tolerance = " & tol
                Set swTanEnt = swVertex
                bRet = swTanEnt.Select4(True, Nothing)
            Else
                Debug.Print "Vertex is not tolerant:  Tolerance = " & tol
            End If
        Next vVertex
        Debug.Print ""
        Debug.Print "Maximum vertex gap is " & maxVertexGap
        Debug.Print ""

    Next vBody
End Sub
```
