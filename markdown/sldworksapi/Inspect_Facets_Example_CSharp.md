---
title: "Inspect Facets of Graphics and Mesh Bodies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Inspect_Facets_Example_CSharp.htm"
---

# Inspect Facets of Graphics and Mesh Bodies Example (C#)

This example shows how to inspect facets, facet edges, and facet vertexes after importing graphics and mesh bodies.

// ===================================================

// Preconditions:

// 1. Copy `Public_Documents`**\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\Part1.PLY** to **c:\temp**.

// 2. Open the Immediate window.

// Postconditions:

// 1. Press F5 five times, inspecting the Immediate window after each press.

// 2. The part is imported first as a graphics body and then as a mesh body.

// 3. The macro tests facets, facet edges, and facet vertexes after each import.

// ==================================================

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System.Diagnostics;

namespace Macro1_CSharp

{

public partial class SolidWorksMacro

{

private ModelDoc2 swModelDoc;

public void Main()

{

swModelDoc = null;

TestGraphicsBody();

TestBodies();

swModelDoc = null;

swApp.CloseDoc("Part1");

TestMeshBody();

TestBodies();

swModelDoc = null;

swApp.CloseDoc("Part1");

}

public void TestGraphicsBody()

{

Debug.Print("Importing Part1.PLY as a graphics body...");

Debug.Print("");

bool boolstatus;

boolstatus = swApp.**SetUserPreferenceIntegerValue**((int)swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, (int)swImportStlVrmlModelType_e.swImportStlVrmlModelType_Graphics);

boolstatus = swApp.**SetUserPreferenceIntegerValue**((int)swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, 0);

boolstatus = swApp.**LoadFile2**(@"c:\temp\Part1.PLY", "r");

swModelDoc = (ModelDoc2)swApp.ActiveDoc;

SelectGraphicsBody();

}

public void TestMeshBody()

{

Debug.Print("Importing Part1.PLY as a mesh body...");

Debug.Print("");

bool boolstatus;

boolstatus = swApp.**SetUserPreferenceIntegerValue**((int)swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, (int)swImportStlVrmlModelType_e.swImportStlVrmlModelType_Surface);

boolstatus = swApp.**SetUserPreferenceIntegerValue**((int)swUserPreferenceIntegerValue_e.swImportStlVrmlModelType, 1);

swApp.**SetUserPreferenceToggle**((int)swUserPreferenceToggle_e.swVrmlStlImportAsPSMesh, true);

boolstatus = swApp.**LoadFile2**(@"c:\temp\Part1.PLY", "r");

swModelDoc = (ModelDoc2)swApp.ActiveDoc;

SelectMeshBody();

}

public void SelectGraphicsBody()

{

Debugger.Break();

Debug.Print("Getting the graphics body, Graphic (Closed) -1...");

bool boolstatus;

boolstatus = swModelDoc.Extension.SelectByID2("Graphic (Closed) -1", "MESH BODY FEATURE", -0.0932538825377272d, 0.091d, 0.033742378078639d, false, 0, null, 0);

SelectionMgr swSelMgr;

swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

int lSelType;

lSelType = swSelMgr.GetSelectedObjectType3(1, -1);

if (lSelType == (int)swSelectType_e.swSelGRAPHICSBODY)

{

Debug.Print("lSelType = swSelGRAPHICSBODY");

}

Feature swFeature;

swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);

if (swFeature == null)

{

Debug.Print("swFeature is Nothing");

}

else if (lSelType == (int)swSelectType_e.swSelGRAPHICSBODY)

{

Debug.Print("Select GraphicsBody success");

Body2 swBody;

swBody = (Body2)swFeature.**GetSpecificFeature2**();

if (swBody == null)

{

Debug.Print("swBody Is Nothing");

}

else

{

Debug.Print("Getting Body success");

int lBodyType;

lBodyType = swBody.**GetType**();

if (lBodyType == (int)swBodyType_e.swGraphicsBody)

{

GraphicsBody swGraphicsBody;

swGraphicsBody = (GraphicsBody)swBody.**GetGraphicsBody**();

if (swGraphicsBody == null)

{

Debug.Print("Graphics body object is Nothing");

}

else

{

Debug.Print("GetGraphicsBody success");

Body2 swBodyFromGraphics;

swBodyFromGraphics = (Body2)swGraphicsBody.**GetBody**();

if (swBodyFromGraphics == null)

{

Debug.Print("swGraphicsBody.GetBody failed");

}

else

{

Debug.Print("swGraphicsBody.GetBody success");

}

}

}

}

}

Debug.Print("Selecting facet, facet edge, and facet vertex objects in graphics body...");

swModelDoc.ClearSelection2(true);

boolstatus = swModelDoc.Extension.SelectByID2("Unknown", "MESHFACETREF", -0.130140285581291d, 0.0909999999999798d, 0.0526687725669035d, false, 0, null, 0);

lSelType = swSelMgr.GetSelectedObjectType3(1, -1);

if (lSelType == (int)swSelectType_e.swSelFACETS)

{

Debug.Print("Facet selected");

}

else

{

Debug.Print("Object selected not of type facet");

}

swModelDoc.ClearSelection2(true);

boolstatus = swModelDoc.Extension.SelectByID2("Unknown", "MESHFINREF", -0.0701858537194084d, 0.0909999999999798d, 0.0513894806662165d, false, 0, null, 0);

lSelType = swSelMgr.GetSelectedObjectType3(1, -1);

if (lSelType == (int)swSelectType_e.swSelMESHFACETEDGES)

{

Debug.Print("Facet edge selected");

}

else

{

Debug.Print("Object selected not of type facet edge");

}

swModelDoc.ClearSelection2(true);

boolstatus = swModelDoc.Extension.SelectByID2("Unknown", "MESHVERTEXREF", -0.117127148857435d, 0.0909999999999513d, 0.099920771345694d, false, 0, null, 0);

lSelType = swSelMgr.GetSelectedObjectType3(1, -1);

if (lSelType == (int)swSelectType_e.swSelMESHFACETVERTICES)

{

Debug.Print("Facet vertex selected");

}

else

{

Debug.Print("Object selected not of type facet vertex");

}

Debug.Print("");

}

public void SelectMeshBody()

{

Debugger.Break();

Debug.Print("Getting mesh body, Surface-Imported5...");

bool boolstatus;

boolstatus = swModelDoc.Extension.SelectByID2("Surface-Imported5", "SURFACEBODY", -0.0955822368965755d, 0.0910000000000082d, 0.0336061875443647d, false, 0, null, 0);

SelectionMgr swSelMgr;

swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

int lSelType;

lSelType = swSelMgr.GetSelectedObjectType3(1, -1);

if (lSelType == (int)swSelectType_e.swSelSURFACEBODIES)

{

Body2 swBody;

swBody = (Body2)swSelMgr.GetSelectedObject6(1, -1);

int lBodyType;

lBodyType = swBody.**GetType**();

if (lBodyType == (int)swBodyType_e.swMeshBody)

{

Debug.Print("Select MeshBody success");

MeshBody swMeshBody;

swMeshBody = (MeshBody)swBody.**GetMeshBody**();

if (swMeshBody == null)

{

Debug.Print("Mesh body object is Nothing");

}

else

{

Debug.Print("Mesh body retrieved");

Body2 swMBody;

swMBody = (Body2)swMeshBody.**GetBody**();

if (swMBody == null)

{

Debug.Print("swMeshBody.GetBody failed");

}

else

{

Debug.Print("swMeshBody.GetBody success");

}

}

}

}

Debug.Print("");

}

public void TestBodies()

{

Debugger.Break();

Debug.Print("Testing facets, facet edges, and facet vertexes...");

bool bFilter;

bFilter = swApp.GetSelectionFilter((int)swSelectType_e.swSelMESHFACETEDGES);

swApp.SetSelectionFilter((int)swSelectType_e.swSelMESHFACETEDGES, bFilter == false);

bFilter = swApp.GetSelectionFilter((int)swSelectType_e.swSelMESHFACETEDGES);

int[] vFilters;

vFilters = (int[])swApp.GetSelectionFilters();

int j;

if (vFilters.Length > 0)

{

var loopTo = vFilters.GetUpperBound(0);

for (j = 0; j <= loopTo; j++)

{

int lCurFilter;

lCurFilter = vFilters[j];

if (lCurFilter == (int)swSelectType_e.swSelGRAPHICSBODY)

{

Debug.Print("Selection filter is swSelGRAPHICSBODY");

}

else if (lCurFilter == (int)swSelectType_e.swSelFACETS)

{

Debug.Print("Selection filter is swSelFACETS");

}

else if (lCurFilter == (int)swSelectType_e.swSelMESHFACETEDGES)

{

Debug.Print("Selection filter is swSelMESHFACETEDGES");

}

else if (lCurFilter == (int)swSelectType_e.swSelMESHFACETVERTICES)

{

Debug.Print("Selection filter is swSelMESHFACETVERTICES");

}

else

{

Debug.Print("Selection filter is other than facet/facet edge/facet vertex");

}

}

}

var lSelFilters = new int[1];

object vSelFilters;

lSelFilters[0] = (int)swSelectType_e.swSelMESHFACETVERTICES;

// lSelFilters(1) = swSelectType_e.swSelFACETS

vSelFilters = lSelFilters;

swApp.SetSelectionFilters(vSelFilters, false);

bool bApplySelFilters;

bApplySelFilters = swApp.GetApplySelectionFilter();

bool bOppSelFilter;

bOppSelFilter = bApplySelFilters == false;

swApp.SetApplySelectionFilter(bOppSelFilter);

swApp.SetApplySelectionFilter(false);

swModelDoc = (ModelDoc2)swApp.ActiveDoc;

PartDoc swPartDoc;

swPartDoc = (PartDoc)swModelDoc;

object[] vBodies;

vBodies = (object[])swPartDoc.GetBodies2(-1, false);

SelectionMgr swSelMgr;

swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

int lSelType;

Body2 swCurBod;

if (vBodies.Length > 0)

{

int i;

var loopTo1 = vBodies.GetUpperBound(0);

for (i = 0; i <= loopTo1; i++)

{

Debug.Print("");

swCurBod = (Body2)vBodies[i];

int lCurBodyType;

lCurBodyType = swCurBod.**GetType**();

if (lCurBodyType == (int)swBodyType_e.swMeshBody)

{

Debug.Print("Testing mesh body");

}

else if (lCurBodyType == (int)swBodyType_e.swGraphicsBody)

{

Debug.Print("Testing graphics body");

}

else

{

Debug.Print("Some other body type");

}

swCurBod.Select2(false, null);

swCurBod.DeSelect();

bool bIsVisible;

bIsVisible = swCurBod.**Visible**;

Debug.Print("Visible is " + bIsVisible);

string sBodyName;

sBodyName = swCurBod.**Name**;

Debug.Print("Name is \"" + sBodyName + "\"");

bool bIsMesh;

bIsMesh = swCurBod.**IsMeshBody**();

Debug.Print("IsMeshBody returned " + bIsMesh);

bool bIsGraphics;

bIsGraphics = swCurBod.**IsGraphicsBody**();

Debug.Print("IsGraphicsBody method returned " + bIsGraphics);

MeshBody swThisMeshBody;

swThisMeshBody = (MeshBody)swCurBod.**GetMeshBody**(); //

if (swThisMeshBody == null)

{

Debug.Print("");

}

else

{

Body2 swThisBodyFromMesh;

swThisBodyFromMesh = (Body2)swThisMeshBody.**GetBody**();

if (swThisBodyFromMesh is object)

{

Debug.Print("swThisMeshBody.GetBody returned an IBody2.");

}

else

{

Debug.Print("swThisMeshBody.GetBody returned Nothing.");

}

Debug.Print("Getting facet, facet edge, and facet vertex objects in this mesh body...");

int lFacetCount;

lFacetCount = swThisMeshBody.**GetFacetCount**();

Debug.Print("Facet count is " + lFacetCount);

object[] vMFacets;

vMFacets = (object[])swThisMeshBody.**GetFacets**();

int lMFacetIndex;

var loopTo2 = vMFacets.GetUpperBound(0);

for (lMFacetIndex = 0; lMFacetIndex <= loopTo2; lMFacetIndex++)

{

Debug.Print("");

Debug.Print("Facet " + (lMFacetIndex + 1));

Facet swCurMFacet;

swCurMFacet = (Facet)vMFacets[lMFacetIndex];

Body2 swBodyFromCurMFacet;

swBodyFromCurMFacet = (Body2)swCurMFacet.**GetBody**();

object[] vEdges;

object[] vVerts;

vEdges = (object[])swCurMFacet.**GetFacetEdges**();

int lEdgesIndex;

var loopTo3 = vEdges.GetUpperBound(0);

for (lEdgesIndex = 0; lEdgesIndex <= loopTo3; lEdgesIndex++)

{

Edge swCurEdge;

swCurEdge = (Edge)vEdges[lEdgesIndex];

if (swCurEdge == null)

{

Debug.Print("Edge object is Nothing");

}

else

{

Debug.Print("Edge retrieved");

}

}

vVerts = (object[])swCurMFacet.**GetFacetVertices**();

int lVertsIndex;

var loopTo4 = vVerts.GetUpperBound(0);

for (lVertsIndex = 0; lVertsIndex <= loopTo4; lVertsIndex++)

{

Vertex swCurVert;

swCurVert = (Vertex)vVerts[lVertsIndex];

if (swCurVert == null)

{

Debug.Print("Vertex object is Nothing");

}

else

{

Debug.Print("Vertex retrieved");

}

}

swCurMFacet.Select(false, null);

lSelType = swSelMgr.GetSelectedObjectType3(1, -1);

if (lSelType == (int)swSelectType_e.swSelFACETS)

{

Debug.Print("Facet selected");

}

else

{

Debug.Print("Object not of type Facet");

}

}

}

GraphicsBody swThisGraphicsBody;

swThisGraphicsBody = (GraphicsBody)swCurBod.**GetGraphicsBody**();

if (swThisGraphicsBody == null)

{

Debug.Print("");

}

else

{

Body2 swThisBodyFromGraphics;

swThisBodyFromGraphics = (Body2)swThisGraphicsBody.**GetBody**();

if (swThisBodyFromGraphics is object)

{

Debug.Print("swThisGraphicsBody.GetBody returned an IBody2.");

}

else

{

Debug.Print("swThisGraphicsBody.GetBody returned Nothing.");

}

Debug.Print("Getting facet, facet edge, and facet vertex objects in this graphics body...");

int lGFacetCount;

lGFacetCount = swThisGraphicsBody.**GetFacetCount**();

Debug.Print("Facet count is " + lGFacetCount);

object[] vFacets;

vFacets = (object[])swThisGraphicsBody.GetFacets();

int lFacetIndex;

var loopTo5 = vFacets.GetUpperBound(0);

for (lFacetIndex = 0; lFacetIndex <= loopTo5; lFacetIndex++)

{

Debug.Print("");

Debug.Print("Facet " + (lFacetIndex + 1));

Facet swFacet;

swFacet = (Facet)vFacets[lFacetIndex];

Body2 swFacetBody;

swFacetBody = (Body2)swFacet.**GetBody**();

if (swFacetBody == null)

{

Debug.Print("swFacet.GetBody failed");

}

else

{

Debug.Print("swFacet.GetBody returned an IBody2");

}

object[] vGEdges;

vGEdges =(object[]) swFacet.**GetFacetEdges**();

int lFacetEdgesCount;

lFacetEdgesCount = vGEdges.GetUpperBound(0) + 1;

int lFacetEdgesIndex;

var loopTo6 = vGEdges.GetUpperBound(0);

for (lFacetEdgesIndex = 0; lFacetEdgesIndex <= loopTo6; lFacetEdgesIndex++)

{

Edge swFacetEdge;

swFacetEdge = (Edge)vGEdges[lFacetEdgesIndex];

if (swFacetEdge == null)

{

Debug.Print("Edge object is Nothing");

}

else

{

Debug.Print("Edge retrieved");

}

}

object[] vGVerts;

vGVerts = (object[])swFacet.**GetFacetVertices**();

int lFacetVertsCount;

lFacetVertsCount = vGVerts.GetUpperBound(0) + 1;

int lFacetVertsIndex;

var loopTo7 = vGVerts.GetUpperBound(0);

for (lFacetVertsIndex = 0; lFacetVertsIndex <= loopTo7; lFacetVertsIndex++)

{

Vertex swFacetVert;

swFacetVert = (Vertex)vGVerts[lFacetVertsIndex];

if (swFacetVert == null)

{

Debug.Print("Vertex object is Nothing");

}

else

{

Debug.Print("Vertex retrieved");

}

}

swFacet.Select(false, null);

lSelType = swSelMgr.GetSelectedObjectType3(1, -1);

if (lSelType == (int)swSelectType_e.swSelFACETS)

{

Debug.Print("Facet selected");

}

else

{

Debug.Print("Object not of type Facet");

}

}

}

}

}

Debug.Print("");

}

// The SldWorks swApp variable is pre-assigned for you.

public SldWorks swApp;

}

}
