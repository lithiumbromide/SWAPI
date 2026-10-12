---
title: "Select Edges of All Holes on Face Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm"
---

# Select Edges of All Holes on Face Example (C#)

This example shows how to select the edges on all circular holes on a face.

**NOTE:** A circular hole can be defined in a many ways; for example, a circle inside an extruded sketch or a circle that is part of a cut-extrude feature. Thus, there is no ready way to detect a hole solely based on the feature information. However, by directly examining the geometry and topology of the model, it is possible to deduce holes. This code uses many of the geometry- and topology-related objects and methods to traverse a face and look for circular holes.

//------------------------------------------------------------------
// Preconditions: Verify that the specified part to open exists.
//
// Postconditions:
// 1. Opens the specified part document.
// 2. Changes the view orientation to **Back**.
// 3. Selects a face.
// 4. Examines the geometry and topology of the selected face and
// identifies the holes in the face.
// 5. Deselects the face.
// 6. Selects all edges of all circular holes on the face.
// 7. Examine the graphics area.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CoEdgeCSharp.csproj
{
public partial class SolidWorksMacro
{
public void Main()
{
ModelDoc2 swModel = default(ModelDoc2);
ModelDocExtension swModelDocExt = default(ModelDocExtension);
SelectionMgr swSelMgr = default(SelectionMgr);
SelectData swSelData = default(SelectData);
Face2 swFace = default(Face2);
string fileName = null;
int errors = 0;
int warnings = 0;
bool bRet = false;

fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\gear- caddy.sldprt";
swModel = (ModelDoc2)swApp.**OpenDoc6**(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
swModel.**ShowNamedView2**("*Back", 2);
swModelDocExt = (ModelDocExtension)swModel.**Extension**;
bRet = swModelDocExt.**SelectByID2**("", "FACE", 0.0290197084065686, 0.0111645373580202, 0, false, 0, null, 0);
swSelMgr = (SelectionMgr)swModel.**SelectionManager**;
swFace = (Face2)swSelMgr.**GetSelectedObject6**(1, -1);
swSelData = (SelectData)swSelMgr.**CreateSelectData**();
swModel.**ClearSelection2**(true);
SelectHoleEdges(swFace, swSelData);

}
public double[] GetFaceNormalAtMidCoEdge(CoEdge swCoEdge)
{
Face2 swFace = default(Face2);
Surface swSurface = default(Surface);
Loop2 swLoop = default(Loop2);
double[] varParams = null;
double[] varPoint = null;
double dblMidParam = 0;
double[] dblNormal = new double[3];
bool bFaceSenseReversed = false;

varParams = (double[])swCoEdge.**GetCurveParams**();
if (varParams[6] > varParams[7])
{
dblMidParam = (varParams[6] - varParams[7]) / 2 + varParams[7];
}
else
{
dblMidParam = (varParams[7] - varParams[6]) / 2 + varParams[6];
}
varPoint = (double[])swCoEdge.**Evaluate**(dblMidParam);

// Get the face of the given coedge
// Check for the sense of the face
swLoop = (Loop2)swCoEdge.**GetLoop**();
swFace = (Face2)swLoop.**GetFace**();
swSurface = (Surface)swFace.**GetSurface**();
bFaceSenseReversed = swFace.**FaceInSurfaceSense**();
varParams = (double[])swSurface.**EvaluateAtPoint**(varPoint[0], varPoint[1], varPoint[2]);
if (bFaceSenseReversed)
{
// Negate the surface normal as it is opposite from the face normal
dblNormal[0] = -varParams[0];
dblNormal[1] = -varParams[1];
dblNormal[2] = -varParams[2];
}
else
{
dblNormal[0] = varParams[0];
dblNormal[1] = varParams[1];
dblNormal[2] = varParams[2];
}
return dblNormal;

}

public double[] GetTangentAtMidCoEdge(CoEdge swCoEdge)
{
double[] varParams = null;
double dblMidParam = 0;
double[] dblTangent = new double[3];
varParams = (double[])swCoEdge.**GetCurveParams**();
if (varParams[6] > varParams[7])
{
dblMidParam = (varParams[6] - varParams[7]) / 2.0 + varParams[7];
}
else
{
dblMidParam = (varParams[7] - varParams[6]) / 2.0 + varParams[6];
}
varParams = (double[])swCoEdge.**Evaluate**(dblMidParam);
dblTangent[0] = varParams[3];
dblTangent[1] = varParams[4];
dblTangent[2] = varParams[5];
return dblTangent;

}

public double[] GetCrossProduct(double[] varVec1, double[] varVec2)
{
double[] dblCross = new double[3];

dblCross[0] = varVec1[1] * varVec2[2] - varVec1[2] * varVec2[1];
dblCross[1] = varVec1[2] * varVec2[0] - varVec1[0] * varVec2[2];
dblCross[2] = varVec1[0] * varVec2[1] - varVec1[1] * varVec2[0];
return dblCross;

}

public bool VectorsAreEqual(double[] varVec1, double[] varVec2)
{
bool functionReturnValue = false;
double dblMag = 0;
double dblDot = 0;
double[] dblUnit1 = new double[3];
double[] dblUnit2 = new double[3];
dblMag = Math.Pow((varVec1[0] * varVec1[0] + varVec1[1] * varVec1[1] + varVec1[2] * varVec1[2]), 0.5);
dblUnit1[0] = varVec1[0] / dblMag;
dblUnit1[1] = varVec1[1] / dblMag;
dblUnit1[2] = varVec1[2] / dblMag;
dblMag = Math.Pow((varVec2[0] * varVec2[0] + varVec2[1] * varVec2[1] + varVec2[2] * varVec2[2]), 0.5);
dblUnit2[0] = varVec2[0] / dblMag;
dblUnit2[1] = varVec2[1] / dblMag;
dblUnit2[2] = varVec2[2] / dblMag;
dblDot = dblUnit1[0] * dblUnit2[0] + dblUnit1[1] * dblUnit2[1] + dblUnit1[2] * dblUnit2[2];
dblDot = Math.Abs(dblDot - 1.0);
// Compare within a tolerance
//1.0e-10
if (dblDot < 1E-10)
{
functionReturnValue = true;
}
else
{
functionReturnValue = false;
}
return functionReturnValue;

}

public void SelectHoleEdges(Face2 swFace, SelectData swSelData)
{
Loop2 swThisLoop = default(Loop2);
CoEdge swThisCoEdge = default(CoEdge);
CoEdge swPartnerCoEdge = default(CoEdge);
Entity swEntity = default(Entity);
double[] varThisNormal = null;
double[] varPartnerNormal = null;
double[] varCrossProduct = null;
double[] varTangent = null;
object[] vEdgeArr = null;
Edge swEdge = default(Edge);
Curve swCurve = default(Curve);
bool bRet = true;
int count = 0;
bool bCount = true;

swThisLoop = (Loop2)swFace.**GetFirstLoop**();
while ((swThisLoop != null))
{
// Hole is inner loop
// Circular or elliptical hole has only one edge
bRet = swThisLoop.**IsOuter**();
count = swThisLoop.**GetEdgeCount**();
if (count != 1)
{
bCount = false;
}
else
{
bCount = true;
}
if ((bRet == false) && (bCount == true))
{
swThisCoEdge = (CoEdge)swThisLoop.**GetFirstCoEdge**();
swPartnerCoEdge = (CoEdge)swThisCoEdge.**GetPartner**();
varThisNormal = (double[])GetFaceNormalAtMidCoEdge(swThisCoEdge);
varPartnerNormal = (double[])GetFaceNormalAtMidCoEdge(swPartnerCoEdge);
if (!VectorsAreEqual(varThisNormal, varPartnerNormal))
{
// There is a sufficient change between the two faces to determine
// what kind of transition is being made
varCrossProduct = (double[])GetCrossProduct(varThisNormal, varPartnerNormal);
varTangent = (double[])GetTangentAtMidCoEdge(swThisCoEdge);
if (VectorsAreEqual(varCrossProduct, varTangent))
{
// Hole
vEdgeArr = (object[])swThisLoop.**GetEdges**();
Debug.Assert(0 < vEdgeArr.Length);
swEdge = (Edge)vEdgeArr[0];
swCurve = (Curve)swEdge.**GetCurve**();
// Ignore elliptical holes
if (swCurve.**IsCircle**())
{
swEntity = (Entity)swEdge;
bRet = swEntity.**Select4**(true, swSelData);
Debug.Assert(bRet);
}
}
}
}

// Move on to the next
swThisLoop = (Loop2)swThisLoop.**GetNext**();
}
}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>
public SldWorks swApp;
}
}
