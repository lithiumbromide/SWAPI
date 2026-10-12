---
title: "Is Selected Feature a Boundary Box Sketch (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Is_Selected_Feature_a_Boundary_Box_Sketch_Example_CSharp.htm"
---

# Is Selected Feature a Boundary Box Sketch (C#)

This example shows how to determine if a sketch is a boundary box sketch.

//----------------------------------------------------------
// Preconditions:
// 1. Open `public_documents`**\samples\tutorial\api\2012-sm.sldprt**.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Unsuppresses the **Flat**-**Pattern1** feature.
// 2. Selects the **Flat-Pattern1**'s boundary box sketch feature.
// 3. Gets whether the selected sketch is a boundary box sketch.
// 4. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;

namespace IsBoundaryBoxSketchSketchCSharp.csproj
{
partial class SolidWorksMacro
{
public void Main()
{

ModelDoc2 swModel;
ModelDocExtension swModelDocExt;
SelectionMgr swSelMgr;
Feature swFeature;
Sketch swSketch;
bool status = false;

// Open a sheet metal part
swModel = (ModelDoc2)swApp.**ActiveDoc**;

// Select the flat-pattern feature
swModelDocExt = (ModelDocExtension)swModel.**Extension**;
status = swModelDocExt.**SelectByID2**("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, false, 0, null, 0);

// Unsuppress the flat-pattern feature
status = swModel.**EditUnsuppress2**();
swModel.**ClearSelection2**(true);

// Select the flat-pattern feature's boundary box feature
status = swModelDocExt.**SelectByID2**("Bounding-Box1", "SKETCH", 0, 0, 0, false, 0, null, 0);
swSelMgr = (SelectionMgr)swModel.**SelectionManager**;
swFeature = (Feature)swSelMgr.**GetSelectedObject6**(1, -1);
swSketch = (Sketch)swFeature.**GetSpecificFeature2**();

// Print to the Immediate window if the just-selected feature is a boundary box
Debug.Print("Selected sketch a boundary box sketch? " + swSketch.**IsBoundaryBoxSketch**());
}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>
public SldWorks swApp;

}
}
