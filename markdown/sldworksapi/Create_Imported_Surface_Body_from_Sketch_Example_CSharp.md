---
title: "Create Imported Surface Body from Sketch Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm"
---

# Create Imported Surface Body from Sketch Example (C#)

This example shows how to create an imported body surface from a sketch.

```vb
'--------------------------------------
'
' Preconditions: A circular sketch is selected.
'
' Postconditions: A cylindrical imported surface body is created.
'
'--------------------------------------
using System;
namespace BodyFromSketchProfile
{
/// <summary>
/// Summary description for Class1
/// </summary>
class Application
{
static double ExtrudeDepth = 0.1;
/// <summary>
/// Main entry point for the application
/// </summary>
[STAThread]
static void Main(string[] args)
{
bool bRetval;
SldWorks.ISldWorks swApp;
SldWorks.IModelDoc2 swDoc;
SldWorks.IPartDoc swPart;
SldWorks.IBody2 swBody;
SldWorks.ISketch swSketch;
SldWorks.IFeature swFeature;

swApp = new SldWorks.SldWorksClass();
swDoc = swApp.IActiveDoc2;
swPart = (SldWorks.IPartDoc) swDoc;

SldWorks.ISelectionMgr swSelMgr;
swSelMgr = swDoc.ISelectionManager;
swFeature = (SldWorks.IFeature) swSelMgr.GetSelectedObject6(1,0);
swSketch = (SldWorks.ISketch) swFeature.GetSpecificFeature2();
if (swSketch != null)
{
SldWorks.IEnumSketchSegments swSegs;
swSegs = swSketch.IEnumSketchSegments();

int nFetched = 0;
int segcount = 0;
SldWorks.SketchSegment swSeg;
System.Collections.ArrayList ProfileSegs = new System.Collections.ArrayList();
System.Collections.ArrayList BodySurfaces = new System.Collections.ArrayList();
SldWorks.ISurface swSurface;

swSegs.Next(1, out swSeg, ref nFetched);
while (nFetched != 0)
{
if (swSeg.ConstructionGeometry == false)
{
swBody = swPart.ICreateNewBody2();

segcount++;
SldWorks.ISketchPoint swStartPt;
SldWorks.ISketchPoint swEndPt;
SldWorks.ICurve swCurve = null;

switch (swSeg.GetType())
{
case (int)SwConst.swSketchSegments_e.swSketchARC:
{
SldWorks.ISketchArc swSkArc;
swSkArc = (SldWorks.ISketchArc) swSeg;

SldWorks.ISketchPoint swCenterPt;
double [] normal;
double radius;

swCenterPt = swSkArc.IGetCenterPoint2();
swStartPt = swSkArc.IGetStartPoint2();
swEndPt = swSkArc.IGetEndPoint2();
normal = (double[])swSkArc.GetNormalVector();
radius = swSkArc.GetRadius();

double []center = new double[3];
double []startpt = new double[3];
double []endpt = new double[3];

center[0] = swCenterPt.X;
center[1] = swCenterPt.Y;
center[2] = swCenterPt.Z;
startpt[0] = swStartPt.X;
startpt[1] = swStartPt.Y;
startpt[2] = swStartPt.Z;
endpt[0] = swEndPt.X;
endpt[1] = swEndPt.Y;
endpt[2] = swEndPt.Z;

swCurve = swBody.IAddProfileArc(center, normal, radius, startpt, endpt);
break;
}
case (int)SwConst.swSketchSegments_e.swSketchLINE:
{
SldWorks.ISketchLine swSkLine;
swSkLine = (SldWorks.ISketchLine) swSeg;

swStartPt = swSkLine.IGetStartPoint2();
swEndPt = swSkLine.IGetEndPoint2();

double []root = new double[3];
double []dir = new double[3];

root[0] = swStartPt.X;
root[1] = swStartPt.Y;
root[2] = swStartPt.Z;

dir[0] = swEndPt.X - root[0];
dir[1] = swEndPt.Y - root[1];
dir[2] = swEndPt.Z - root[2];

swCurve = swBody.IAddProfileLine(root, dir);

break;
}
default:
System.Diagnostics.Debug.Assert(false, "Unhandled sketch segment type");
break;
}
// Have the curve and the start and end points
// Create the side of the extrusion

ProfileSegment curSeg = new ProfileSegment(swSeg, swCurve);
double []surfeval;
double []extruAxis = new double[3];

extruAxis[0] = 0.0;
extruAxis[1] = 0.0;
extruAxis[2] = 1.0;

ProfileSegs.Add(curSeg);

swSurface = swBody.ICreateExtrusionSurface((SldWorks.Curve)swCurve, extruAxis);

//Create a trimming loop for the surface
int nCurves = 4;
int []Order = {2, 2, 2, 2};
int []Dim = {2, 2, 2, 2};
int []Periodic = {0, 0, 0, 0};
int []nKnots = {4, 4, 4, 4};
int []nCtrlPts = {2, 2, 2, 2};
double []Knots = {0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1};
double []CtrlPts = new double[16];

double x = curSeg.iStartPt.X;
double y = curSeg.iStartPt.Y;
double z = curSeg.iStartPt.Z;
surfeval = (double[])swSurface.GetClosestPointOn(x, y, z);
CtrlPts[0] = surfeval[3];
CtrlPts[1] = surfeval[4];
CtrlPts[14] = surfeval[3];
CtrlPts[15] = surfeval[4];

x = curSeg.iEndPt.X;
y = curSeg.iEndPt.Y;
z = curSeg.iEndPt.Z;
surfeval = (double[])swSurface.GetClosestPointOn(x, y, z);
CtrlPts[2] = surfeval[3];
CtrlPts[3] = surfeval[4];
CtrlPts[4] = surfeval[3];
CtrlPts[5] = surfeval[4];

x = curSeg.iEndPt.X;
y = curSeg.iEndPt.Y;
z = curSeg.iEndPt.Z;
surfeval = (double[])swSurface.GetClosestPointOn(x, y, z + ExtrudeDepth);
CtrlPts[6] = surfeval[3];
CtrlPts[7] = surfeval[4];
CtrlPts[8] = surfeval[3];
CtrlPts[9] = surfeval[4];

x = curSeg.iStartPt.X;
y = curSeg.iStartPt.Y;
z = curSeg.iStartPt.Z;
surfeval = (double[])swSurface.GetClosestPointOn(x, y, z + ExtrudeDepth);
CtrlPts[10] = surfeval[3];
CtrlPts[11] = surfeval[4];
CtrlPts[12] = surfeval[3];
CtrlPts[13] = surfeval[4];

swSurface.AddTrimmingLoop(nCurves, Order, Dim, Periodic, nKnots, nCtrlPts, Knots, CtrlPts);

bRetval = swBody.CreateTrimmedSurface();
bRetval = swBody.CreateBodyFromSurfaces();
}
swSegs.Next(1, out swSeg, ref nFetched);
}
}
}// Main
}// Application
class ProfileSegment
{
public SldWorks.ISketchSegment iSkSeg;
public SldWorks.ICurve iCurve;
public SldWorks.ISketchPoint iStartPt;
public SldWorks.ISketchPoint iEndPt;
public ProfileSegment(SldWorks.ISketchSegment swSkSeg, SldWorks.ICurve swCurve)
{
iSkSeg = swSkSeg;
iCurve = swCurve;

switch (iSkSeg.GetType())
{
case (int)SwConst.swSketchSegments_e.swSketchARC:
{
SldWorks.ISketchArc swSkArc;
swSkArc = (SldWorks.ISketchArc) iSkSeg;

iStartPt = swSkArc.IGetStartPoint2();
iEndPt = swSkArc.IGetEndPoint2();
break;
}

case (int)SwConst.swSketchSegments_e.swSketchLINE:
{
SldWorks.ISketchLine swSkLine;
swSkLine = (SldWorks.ISketchLine) iSkSeg;

iStartPt = swSkLine.IGetStartPoint2();
iEndPt = swSkLine.IGetEndPoint2();

break;
}
default:
System.Diagnostics.Debug.Assert(false, "Unhandled sketch segment type");
break;
}
}
 }
class Vector
{
private
double []coords = new double[3];

public Vector(double x, double y, double z)
{
coords[0] = x; coords[1] = y; coords[2] = z;
}
}
}// BodyFromSketchProfile
```
