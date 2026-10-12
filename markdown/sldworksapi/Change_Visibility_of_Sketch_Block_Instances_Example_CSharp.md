---
title: "Change Visibility of Sketch Block Instances (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Visibility_of_Sketch_Block_Instances_Example_CSharp.htm"
---

# Change Visibility of Sketch Block Instances (C#)

This example shows how to hide and show sketch block instances in a drawing document.
//-------------------------------------------------
// Preconditions:
// 1. Drawing document containing a sketch block
// with one or more sketch block instances is open.
// 2. The sketch block is selected in the FeatureManager
// design tree.
//
// Postconditions: All sketch block instances are hidden if visible, or
// shown if hidden.
//-------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Windows.Forms;

namespace VisibleSketchBlockInstanceCSharp.csproj
{
partial class SolidWorksMacro
{
public void Main()
{
ModelDoc2 swModelDoc;
SelectionMgr swSelMgr;
Feature swFeature;
SketchBlockDefinition swBlockDefinition;
SketchBlockInstance swBlockInstance;
object[] blocks = null;
int i = 0;

swModelDoc = (ModelDoc2)swApp.**ActiveDoc**;
swSelMgr = (SelectionMgr)swModelDoc.**SelectionManager**;

// Block feature is selected in FeatureManager design tree
swFeature = (Feature)swSelMgr.**GetSelectedObject6**(1, -1);
if (swFeature == null)
{
MessageBox.Show("Select a sketch block in the FeatureManager design tree, then rerun the macro.");
}
else
{
swBlockDefinition = (SketchBlockDefinition)swFeature.**GetSpecificFeature2**();
Debug.Print("Feature type : " + swFeature.**GetTypeName2**());
if ((swBlockDefinition != null))
{
blocks = (object[])swBlockDefinition.**GetInstances**();
for (i = blocks.GetLowerBound(0); i <= blocks.GetUpperBound(0); i++)
{

swBlockInstance = (SketchBlockInstance)blocks[i];
Debug.Print("Sketch block instance: " + (i + 1));
Debug.Print(" Angle : " + swBlockInstance.**Angle**);
Debug.Print(" Scale : " + swBlockInstance.**Scale2**);

// Hide or show the sketch block instance
long status = 0;
status = swBlockInstance.**Visible**;
switch (status)
{
case (int)swAnnotationVisibilityState_e.swAnnotationHidden:
swBlockInstance.**Visible** = (int)swAnnotationVisibilityState_e.swAnnotationVisible;
Debug.Print(" Was hidden, now visible.");
break;
case (int)swAnnotationVisibilityState_e.swAnnotationVisible:
swBlockInstance.**Visible** = (int)swAnnotationVisibilityState_e.swAnnotationHidden;
Debug.Print(" Was visible, now hidden.");
break;
case (int)swAnnotationVisibilityState_e.swAnnotationHalfHidden:
MessageBox.Show("This block is half hidden.");
break;
case (int)swAnnotationVisibilityState_e.swAnnotationVisibilityUnknown:
MessageBox.Show("Failed to determine visibility of this block.");
break;

}
}
}

blocks = null;

}
}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>
public SldWorks swApp;

}
}
