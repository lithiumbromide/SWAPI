---
title: "Tessellate a Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Tessellate_a_Body_Example_VB.htm"
---

# Tessellate a Body Example (VBA)

This example shows how to tessellate a body.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Tessellates the body.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------------
Option Explicit
```

```vb
     Sub Main()
        Dim errors As Long
        Dim warnings As Long
        Dim swApp As SldWorks.SldWorks
        Dim swModel As ModelDoc2
        Dim swPart As PartDoc
        Dim b As Integer
        Dim nBodyType As Integer
        Dim swFace As Face2
        Dim swTessellation As Tessellation
        Dim bResult As Boolean
        Dim iNumVertices As Integer
        Dim iNumFacets As Integer
        Dim aFacetIds As Variant
        Dim aFinIds As Variant
        Dim aVertexIds As Variant
        Dim aVertexCoords1 As Variant
        Dim aVertexCoords2 As Variant
        Dim iFacetIdIdx As Integer
        Dim iFinIdx As Integer
        Dim vBodies As Variant

        Set swApp = Application.SldWorks
        ' Get the active document
         Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\drive shaft plate.sldprt", swDocumentTypes_e.swDocPART, 0, "", errors, warnings)
        ' Get the document title
         Debug.Print swModel.GetTitle()
        ' Cast down to a part
         Set swPart = swModel
        ' Get bodies
         vBodies = swPart.GetBodies2(swBodyType_e.swAllBodies, False)
        ' Loop through array
        Dim swBody As Body2
        For b = 0 To UBound(vBodies)
            ' Get a body
            Set swBody = vBodies(b)
            ' Now call a method on a body
             nBodyType = swBody.[GetType]()
            If nBodyType = swBodyType_e.swSolidBody Then
                 Set swFace = Nothing
                 Set swTessellation = Nothing
                 bResult = False
                ' Pass in null so the whole body will be tessellated
                Set swTessellation = swBody.GetTessellation(Empty)
                ' Set up the Tessellation object
                swTessellation.NeedFaceFacetMap = True
                swTessellation.NeedVertexParams = True
                swTessellation.NeedVertexNormal = True
                ' Set option to improve quality of data returned
                swTessellation.ImprovedQuality = True
                Debug.Print ("Tessellation is configured for higher-quality data.")
                ' How to handle matches across common edges
                swTessellation.MatchType = swTesselationMatchType_e.swTesselationMatchFacetTopology
                ' Do the tessellation
                bResult = swTessellation.Tessellate()
                ' Get the number of vertices and facets
                 iNumVertices = swTessellation.GetVertexCount()
                Debug.Print ("Vertex count: " & iNumVertices)
                 iNumFacets = swTessellation.GetFacetCount()
                Debug.Print ("Facet count: " & iNumFacets)
                ' Speed things up
                swModel.SetAddToDB (True)
                swModel.SetDisplayWhenAdded (False)
                ' Insert sketch
                swModel.Insert3DSketch2 (False)
                ' Now get the facet data per face
                Set swFace = swBody.GetFirstFace()
                While Not swFace Is Nothing
                    aFacetIds = swTessellation.GetFaceFacets(swFace)
                    For iFacetIdIdx = 0 To UBound(aFacetIds)
                        aFinIds = swTessellation.GetFacetFins(aFacetIds(iFacetIdIdx))
                        ' There should always be three fins per facet
                        For iFinIdx = 0 To 2
                            aVertexIds = swTessellation.GetFinVertices(aFinIds(iFinIdx))
                            ' Should always be two vertices per fin
                            aVertexCoords1 = swTessellation.GetVertexPoint(aVertexIds(0))
                            aVertexCoords2 = swTessellation.GetVertexPoint(aVertexIds(1))

                            ' Create a line
                            swModel.CreateLine2 aVertexCoords1(0), aVertexCoords1(1), aVertexCoords1(2), aVertexCoords2(0), aVertexCoords2(1), aVertexCoords2(2)
                        Next
                    Next
                    Set swFace = swFace.GetNextFace()
                Wend
                ' Close sketch
                swModel.Insert3DSketch2 (True)
                ' Clear selection for next pass
                swModel.ClearSelection2 (True)
                ' Restore settings
                swModel.SetAddToDB (False)
                swModel.SetDisplayWhenAdded (True)
            End If
        Next
        Exit Sub
    End Sub
```
