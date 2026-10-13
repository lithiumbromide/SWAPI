---
title: "Tessellate a Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Tessellate_a_Body_Example_VBNET.htm"
---

# Tessellate a Body Example (VB.NET)

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
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Partial Class SolidWorksMacro
    Public Sub Main()
        Dim errors As Integer
        Dim warnings As Integer
        ' Get the active document
        Dim swModel As ModelDoc2 = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\drive shaft plate.sldprt", swDocumentTypes_e.swDocPART, 0, "", errors, warnings)
        ' Get the document title
        Dim title As [String] = swModel.GetTitle()
        ' Cast down to a part
        Dim swPart As PartDoc = DirectCast(swModel, PartDoc)
        ' Variant is returned, which can be dealt with as an object
        ' Variant represents an array of references
        Dim vBodies As System.Object
        Dim aBodies As System.Array
        ' Get bodies
        vBodies = swPart.GetBodies2(CInt(swBodyType_e.swAllBodies), False)
        ' Cast to an array of bodies
        aBodies = DirectCast(vBodies, System.Array)
        Dim iNumBodies As Integer = aBodies.Length
        Dim iNumSolidBodies As Integer = 0
        Dim iNumSheetBodies As Integer = 0
        ' Loop through array
        Dim swBody As Body2
        For b As Integer = 0 To iNumBodies - 1
            ' Get a body and apply cast
            swBody = DirectCast(aBodies.GetValue(b), Body2)
            ' Now call a method on a body
            Dim nBodyType As Integer = swBody.[GetType]()
            If nBodyType = CInt(swBodyType_e.swSheetBody) Then
                iNumSheetBodies += 1
            End If
            If nBodyType = CInt(swBodyType_e.swSolidBody) Then
                iNumSolidBodies += 1
                Dim swFace As Face2 = Nothing
                Dim swTessellation As Tessellation = Nothing
                Dim bResult As Boolean = False
                ' Pass in null so the whole body will be tessellated
                swTessellation = DirectCast(swBody.GetTessellation(Nothing), Tessellation)
                ' Set up the Tessellation object
                ' Required data
                swTessellation.NeedFaceFacetMap = True
                swTessellation.NeedVertexParams = True
                swTessellation.NeedVertexNormal = True
                ' Set option to improve quality of data returned
                swTessellation.ImprovedQuality = True
                Debug.Print("Tessellation is configured for higher data quality.")
                ' How to handle matches across common edges
                swTessellation.MatchType = CInt(swTesselationMatchType_e.swTesselationMatchFacetTopology)
                ' Do the tessellation
                bResult = swTessellation.Tessellate()
                ' Get the number of vertices and facets
                Dim iNumVertices As Integer = swTessellation.GetVertexCount()
                Debug.Print("Vertex count: " & iNumVertices)
                Dim iNumFacets As Integer = swTessellation.GetFacetCount()
                Debug.Print("Facet count: " & iNumFacets)
                ' Now get the facet data per face
                Dim aFacetIds As Integer()
                Dim iNumFacetIds As Integer
                Dim aFinIds As Integer()
                Dim aVertexIds As Integer()
                Dim aVertexCoords1 As Double()
                Dim aVertexCoords2 As Double()
                ' Speed things up
                swModel.SetAddToDB(True)
                swModel.SetDisplayWhenAdded(False)
                ' Insert sketch
                swModel.Insert3DSketch2(False)
                ' Loop over faces
                swFace = DirectCast(swBody.GetFirstFace(), Face2)
                While swFace IsNot Nothing
                    aFacetIds = DirectCast(swTessellation.GetFaceFacets(swFace), Integer())
                    iNumFacetIds = aFacetIds.Length
                    For iFacetIdIdx As Integer = 0 To iNumFacetIds - 1
                        aFinIds = DirectCast(swTessellation.GetFacetFins(aFacetIds(iFacetIdIdx)), Integer())
                        ' There should always be three fins per facet
                        For iFinIdx As Integer = 0 To 2
                            aVertexIds = DirectCast(swTessellation.GetFinVertices(aFinIds(iFinIdx)), Integer())
                            ' Should always be two vertices per fin
                            aVertexCoords1 = DirectCast(swTessellation.GetVertexPoint(aVertexIds(0)), Double())
                            aVertexCoords2 = DirectCast(swTessellation.GetVertexPoint(aVertexIds(1)), Double())
                            ' Create a line
                            swModel.CreateLine2(aVertexCoords1(0), aVertexCoords1(1), aVertexCoords1(2), aVertexCoords2(0), aVertexCoords2(1), aVertexCoords2(2))
                        Next
                    Next
                    swFace = DirectCast(swFace.GetNextFace(), Face2)
                End While
                ' Close sketch
                swModel.Insert3DSketch2(True)
                ' Clear selection for next pass
                swModel.ClearSelection2(True)
                ' Restore settings
                swModel.SetAddToDB(False)
                swModel.SetDisplayWhenAdded(True)
            End If
        Next
        Exit Sub
    End Sub

    Public swApp As SldWorks
End Class
```
