---
title: "Inspect Facets of Graphics and Mesh Bodies Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Inspect_Facets_Example_VBNET.htm"
---

# Inspect Facets of Graphics and Mesh Bodies Example (VB.NET)

This example shows how to inspect facets, facet edges, and facet vertexes after importing graphics and mesh bodies.

'===================================================

'Preconditions:

'1. Copy `Public_Documents`**\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\Part1.PLY** to **c:\temp**.

'2. Open the Immediate window.

'Postconditions:

'1. Press F5 five times, inspecting the Immediate window after each press.

'2. The part is imported first as a graphics body and then as a mesh body.

'3. The macro tests facets, facet edges, and facet vertexes after each import.

'==================================================

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports System.Diagnostics

Partial Class SolidWorksMacro

Dim swModelDoc As ModelDoc2

Sub main()

swModelDoc = Nothing

TestGraphicsBody()

TestBodies()

swModelDoc = Nothing

swApp.CloseDoc("Part1")

TestMeshBody()

TestBodies()

swModelDoc = Nothing

swApp.CloseDoc("Part1")

End Sub

Sub TestGraphicsBody()

Debug.Print("Importing Part1.PLY as a graphics body...")

Debug.Print("")

Dim boolstatus As Boolean

boolstatus = swApp.**SetUserPreferenceIntegerValue**(swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Graphics)

boolstatus = swApp.**SetUserPreferenceIntegerValue**(swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, 0)

boolstatus = swApp.**LoadFile2**("c:\temp\Part1.PLY", "r")

swModelDoc = swApp.ActiveDoc

SelectGraphicsBody()

End Sub

Sub TestMeshBody()

Debug.Print("Importing Part1.PLY as a mesh body...")

Debug.Print("")

Dim boolstatus As Boolean

boolstatus = swApp.**SetUserPreferenceIntegerValue**(swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, swImportStlVrmlModelType_e.swImportStlVrmlModelType_Surface)

boolstatus = swApp.**SetUserPreferenceIntegerValue**(swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, 1)

swApp.SetUserPreferenceToggle(swUserPreferenceToggle_e.swVrmlStlImportAsPSMesh, True)

boolstatus = swApp.**LoadFile2**("c:\temp\Part1.PLY", "r")

swModelDoc = swApp.ActiveDoc

SelectMeshBody()

End Sub

Sub SelectGraphicsBody()

Stop

Debug.Print("Getting the graphics body, Graphic (Closed) -1...")

Dim boolstatus As Boolean

boolstatus = swModelDoc.Extension.SelectByID2("Graphic (Closed) -1", "MESH BODY FEATURE", -0.0932538825377272, 0.091, 0.033742378078639, False, 0, Nothing, 0)

Dim swSelMgr As SelectionMgr

swSelMgr = swModelDoc.SelectionManager

Dim lSelType As Integer

lSelType = swSelMgr.GetSelectedObjectType3(1, -1)

If lSelType = swSelectType_e.swSelGRAPHICSBODY Then

Debug.Print("lSelType = swSelGRAPHICSBODY")

End If

Dim swFeature As Feature

swFeature = swSelMgr.GetSelectedObject6(1, -1)

If swFeature Is Nothing Then

Debug.Print("swFeature is Nothing")

ElseIf lSelType = swSelectType_e.swSelGRAPHICSBODY Then

Debug.Print("Select GraphicsBody success")

Dim swBody As Body2

swBody = swFeature.GetSpecificFeature2

If swBody Is Nothing Then

Debug.Print("swBody Is Nothing")

Else

Debug.Print("Getting Body success")

Dim lBodyType As Integer

lBodyType = swBody.GetType

If lBodyType = swBodyType_e.swGraphicsBody Then

Dim swGraphicsBody As GraphicsBody

swGraphicsBody = swBody.**GetGraphicsBody**

If swGraphicsBody Is Nothing Then

Debug.Print("Graphics body object is Nothing")

Else

Debug.Print("GetGraphicsBody success")

Dim swBodyFromGraphics As Body2

swBodyFromGraphics = swGraphicsBody.**GetBody**

If swBodyFromGraphics Is Nothing Then

Debug.Print("swGraphicsBody.GetBody failed")

Else

Debug.Print("swGraphicsBody.GetBody success")

End If

End If

End If

End If

End If

Debug.Print("Selecting facet, facet edge, and facet vertex objects in graphics body...")

swModelDoc.ClearSelection2(True)

boolstatus = swModelDoc.Extension.SelectByID2("Unknown", "MESHFACETREF", -0.130140285581291, 0.0909999999999798, 0.0526687725669035, False, 0, Nothing, 0)

lSelType = swSelMgr.GetSelectedObjectType3(1, -1)

If lSelType = swSelectType_e.swSelFACETS Then

Debug.Print("Facet selected")

Else

Debug.Print("Object selected not of type facet")

End If

swModelDoc.ClearSelection2(True)

boolstatus = swModelDoc.Extension.SelectByID2("Unknown", "MESHFINREF", -0.0701858537194084, 0.0909999999999798, 0.0513894806662165, False, 0, Nothing, 0)

lSelType = swSelMgr.GetSelectedObjectType3(1, -1)

If lSelType = swSelectType_e.swSelMESHFACETEDGES Then

Debug.Print("Facet edge selected")

Else

Debug.Print("Object selected not of type facet edge")

End If

swModelDoc.ClearSelection2(True)

boolstatus = swModelDoc.Extension.SelectByID2("Unknown", "MESHVERTEXREF", -0.117127148857435, 0.0909999999999513, 0.099920771345694, False, 0, Nothing, 0)

lSelType = swSelMgr.GetSelectedObjectType3(1, -1)

If lSelType = swSelectType_e.swSelMESHFACETVERTICES Then

Debug.Print("Facet vertex selected")

Else

Debug.Print("Object selected not of type facet vertex")

End If

Debug.Print("")

End Sub

Sub SelectMeshBody()

Stop

Debug.Print("Getting mesh body, Surface-Imported5...")

Dim boolstatus As Boolean

boolstatus = swModelDoc.Extension.SelectByID2("Surface-Imported5", "SURFACEBODY", -0.0955822368965755, 0.0910000000000082, 0.0336061875443647, False, 0, Nothing, 0)

Dim swSelMgr As SelectionMgr

swSelMgr = swModelDoc.SelectionManager

Dim lSelType As Integer

lSelType = swSelMgr.GetSelectedObjectType3(1, -1)

If lSelType = swSelectType_e.swSelSURFACEBODIES Then

Dim swBody As Body2

swBody = swSelMgr.GetSelectedObject6(1, -1)

Dim lBodyType As Integer

lBodyType = swBody.**GetType**

If lBodyType = swBodyType_e.swMeshBody Then

Debug.Print("Select MeshBody success")

Dim swMeshBody As MeshBody

swMeshBody = swBody.**GetMeshBody**

If swMeshBody Is Nothing Then

Debug.Print("Mesh body object is Nothing")

Else

Debug.Print("Mesh body retrieved")

Dim swMBody As Body2

swMBody = swMeshBody.**GetBody**

If swMBody Is Nothing Then

Debug.Print("swMeshBody.GetBody failed")

Else

Debug.Print("swMeshBody.GetBody success")

End If

End If

End If

End If

Debug.Print("")

End Sub

Sub TestBodies()

Stop

Debug.Print("Testing facets, facet edges, and facet vertexes...")

Dim bFilter As Boolean

bFilter = swApp.GetSelectionFilter(swSelectType_e.swSelMESHFACETEDGES)

swApp.SetSelectionFilter(swSelectType_e.swSelMESHFACETEDGES, (bFilter = False))

bFilter = swApp.GetSelectionFilter(swSelectType_e.swSelMESHFACETEDGES)

Dim vFilters() As Integer

vFilters = swApp.GetSelectionFilters

Dim j As Integer

If vFilters.Length > 0 Then

For j = 0 To UBound(vFilters)

Dim lCurFilter As Integer

lCurFilter = vFilters(j)

If lCurFilter = swSelectType_e.swSelGRAPHICSBODY Then

Debug.Print("Selection filter is swSelGRAPHICSBODY")

ElseIf lCurFilter = swSelectType_e.swSelFACETS Then

Debug.Print("Selection filter is swSelFACETS")

ElseIf lCurFilter = swSelectType_e.swSelMESHFACETEDGES Then

Debug.Print("Selection filter is swSelMESHFACETEDGES")

ElseIf lCurFilter = swSelectType_e.swSelMESHFACETVERTICES Then

Debug.Print("Selection filter is swSelMESHFACETVERTICES")

Else

Debug.Print("Selection filter is other than facet/facet edge/facet vertex")

End If

Next j

End If

Dim lSelFilters(0) As Integer

Dim vSelFilters As Object

lSelFilters(0) = swSelectType_e.swSelMESHFACETVERTICES

'lSelFilters(1) = swSelectType_e.swSelFACETS

vSelFilters = lSelFilters

swApp.SetSelectionFilters(vSelFilters, False)

Dim bApplySelFilters As Boolean

bApplySelFilters = swApp.GetApplySelectionFilter

Dim bOppSelFilter As Boolean

bOppSelFilter = (bApplySelFilters = False)

swApp.SetApplySelectionFilter(bOppSelFilter)

swApp.SetApplySelectionFilter(False)

swModelDoc = swApp.ActiveDoc

Dim swPartDoc As PartDoc

swPartDoc = swModelDoc

Dim vBodies() As Object

vBodies = swPartDoc.**GetBodies2**(-1, False)

Dim swSelMgr As SelectionMgr

swSelMgr = swModelDoc.SelectionManager

Dim lSelType As Integer

Dim swCurBod As Body2

If vBodies.Length > 0 Then

Dim i As Integer

For i = 0 To UBound(vBodies)

Debug.Print("")

swCurBod = vBodies(i)

Dim lCurBodyType As Integer

lCurBodyType = swCurBod.**GetType**

If lCurBodyType = swBodyType_e.swMeshBody Then

Debug.Print("Testing mesh body")

ElseIf lCurBodyType = swBodyType_e.swGraphicsBody Then

Debug.Print("Testing graphics body")

Else

Debug.Print("Some other body type")

End If

swCurBod.Select2(False, Nothing)

swCurBod.DeSelect()

Dim bIsVisible As Boolean

bIsVisible = swCurBod.**Visible**

Debug.Print("Visible is " & bIsVisible)

Dim sBodyName As String

sBodyName = swCurBod.**Name**

Debug.Print("Name is """ & sBodyName & """")

Dim bIsMesh As Boolean

bIsMesh = swCurBod.**IsMeshBody**

Debug.Print("IsMeshBody returned " & bIsMesh)

Dim bIsGraphics As Boolean

bIsGraphics = swCurBod.**IsGraphicsBody**

Debug.Print("IsGraphicsBody method returned " & bIsGraphics)

Dim swThisMeshBody As MeshBody

swThisMeshBody = swCurBod.**GetMeshBody**

If swThisMeshBody Is Nothing Then

Debug.Print("")

Else

Dim swThisBodyFromMesh As Body2

swThisBodyFromMesh = swThisMeshBody.**GetBody**

If Not swThisBodyFromMesh Is Nothing Then

Debug.Print("swThisMeshBody.GetBody returned an IBody2.")

Else

Debug.Print("swThisMeshBody.GetBody returned Nothing.")

End If

Debug.Print("Getting facet, facet edge, and facet vertex objects in this mesh body...")

Dim lFacetCount As Integer

lFacetCount = swThisMeshBody.**GetFacetCount**

Debug.Print("Facet count is " & lFacetCount)

Dim vMFacets() As Object

vMFacets = swThisMeshBody.**GetFacets**

Dim lMFacetIndex As Integer

For lMFacetIndex = 0 To UBound(vMFacets)

Debug.Print("")

Debug.Print("Facet " & lMFacetIndex + 1)

Dim swCurMFacet As Facet

swCurMFacet = vMFacets(lMFacetIndex)

Dim swBodyFromCurMFacet As Body2

swBodyFromCurMFacet = swCurMFacet.**GetBody**

Dim vEdges() As Object

Dim vVerts() As Object

vEdges = swCurMFacet.**GetFacetEdges**

Dim lEdgesIndex As Integer

For lEdgesIndex = 0 To UBound(vEdges)

Dim swCurEdge As Edge

swCurEdge = vEdges(lEdgesIndex)

If swCurEdge Is Nothing Then

Debug.Print("Edge object is Nothing")

Else

Debug.Print("Edge retrieved")

End If

Next lEdgesIndex

vVerts = swCurMFacet.**GetFacetVertices**

Dim lVertsIndex As Integer

For lVertsIndex = 0 To UBound(vVerts)

Dim swCurVert As Vertex

swCurVert = vVerts(lVertsIndex)

If swCurVert Is Nothing Then

Debug.Print("Vertex object is Nothing")

Else

Debug.Print("Vertex retrieved")

End If

Next lVertsIndex

swCurMFacet.Select(False, Nothing)

lSelType = swSelMgr.GetSelectedObjectType3(1, -1)

If lSelType = swSelectType_e.swSelFACETS Then

Debug.Print("Facet selected")

Else

Debug.Print("Object not of type Facet")

End If

Next lMFacetIndex

End If

Dim swThisGraphicsBody As GraphicsBody

swThisGraphicsBody = swCurBod.**GetGraphicsBody**

If swThisGraphicsBody Is Nothing Then

Debug.Print("")

Else

Dim swThisBodyFromGraphics As Body2

swThisBodyFromGraphics = swThisGraphicsBody.**GetBody**

If Not swThisBodyFromGraphics Is Nothing Then

Debug.Print("swThisGraphicsBody.GetBody returned an IBody2.")

Else

Debug.Print("swThisGraphicsBody.GetBody returned Nothing.")

End If

Debug.Print("Getting facet, facet edge, and facet vertex objects in this graphics body...")

Dim lGFacetCount As Integer

lGFacetCount = swThisGraphicsBody.**GetFacetCount**

Debug.Print("Facet count is " & lGFacetCount)

Dim vFacets() As Object

vFacets = swThisGraphicsBody.**GetFacets**

Dim lFacetIndex As Integer

For lFacetIndex = 0 To UBound(vFacets)

Debug.Print("")

Debug.Print("Facet " & lFacetIndex + 1)

Dim swFacet As Facet

swFacet = vFacets(lFacetIndex)

Dim swFacetBody As Body2

swFacetBody = swFacet.**GetBody**

If swFacetBody Is Nothing Then

Debug.Print("swFacet.GetBody failed")

Else

Debug.Print("swFacet.GetBody returned an IBody2")

End If

Dim vGEdges() As Object

vGEdges = swFacet.**GetFacetEdges**

Dim lFacetEdgesCount As Integer

lFacetEdgesCount = UBound(vGEdges) + 1

Dim lFacetEdgesIndex As Integer

For lFacetEdgesIndex = 0 To UBound(vGEdges)

Dim swFacetEdge As Edge

swFacetEdge = vGEdges(lFacetEdgesIndex)

If swFacetEdge Is Nothing Then

Debug.Print("Edge object is Nothing")

Else

Debug.Print("Edge retrieved")

End If

Next lFacetEdgesIndex

Dim vGVerts() As Object

vGVerts = swFacet.**GetFacetVertices**

Dim lFacetVertsCount As Integer

lFacetVertsCount = UBound(vGVerts) + 1

Dim lFacetVertsIndex As Integer

For lFacetVertsIndex = 0 To UBound(vGVerts)

Dim swFacetVert As Vertex

swFacetVert = vGVerts(lFacetVertsIndex)

If swFacetVert Is Nothing Then

Debug.Print("Vertex object is Nothing")

Else

Debug.Print("Vertex retrieved")

End If

Next lFacetVertsIndex

swFacet.Select(False, Nothing)

lSelType = swSelMgr.GetSelectedObjectType3(1, -1)

If lSelType = swSelectType_e.swSelFACETS Then

Debug.Print("Facet selected")

Else

Debug.Print("Object not of type Facet")

End If

Next lFacetIndex

End If

Next i

End If

Debug.Print("")

End Sub

''' <summary>

''' The SldWorks swApp variable is pre-assigned for you.

''' </summary>

Public swApp As SldWorks

End Class
